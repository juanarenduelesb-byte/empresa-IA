"""Acceso a datos con el cliente de la identidad. Defensa doble: filtro explícito aquí y RLS en PostgreSQL."""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from varios.procesos.motor import RIESGOS, Identidad

from .modelos import EventoAuditoria, Solicitud


class NoEncontrado(LookupError):
    pass


@dataclass
class Repositorio:
    sesion: Session
    quien: Identidad

    @property
    def cliente_id(self) -> uuid.UUID:
        return uuid.UUID(self.quien.tenant)

    def crear_solicitud(self, autor_id: uuid.UUID, titulo: str, descripcion: str = "", riesgo: str = "bajo",
                        **_ignorado: object) -> Solicitud:
        """Cualquier `cliente_id` que venga en los datos se ignora: manda la identidad."""
        if riesgo not in RIESGOS:
            raise ValueError(f"Riesgo desconocido: {riesgo}")
        sol = Solicitud(cliente_id=self.cliente_id, autor_id=autor_id, titulo=titulo, descripcion=descripcion,
                        riesgo=riesgo)
        self.sesion.add(sol)
        self.sesion.flush()
        self.registrar("alta", f"solicitud:{sol.id}", None, sol.estado, "Alta de la solicitud")
        return sol

    def solicitud(self, solicitud_id: uuid.UUID) -> Solicitud:
        sol = self.sesion.scalar(
            select(Solicitud).where(Solicitud.id == solicitud_id, Solicitud.cliente_id == self.cliente_id)
        )
        if sol is None:
            raise NoEncontrado(str(solicitud_id))
        return sol

    def solicitudes(self) -> list[Solicitud]:
        consulta = select(Solicitud).where(Solicitud.cliente_id == self.cliente_id).order_by(Solicitud.creado_en)
        return list(self.sesion.scalars(consulta))

    def registrar(self, accion: str, objeto: str, antes: str | None, despues: str | None, motivo: str,
                  clave: str | None = None, **datos: object) -> EventoAuditoria:
        ev = EventoAuditoria(cliente_id=self.cliente_id, actor=self.quien.usuario, accion=accion, objeto=objeto,
                             antes=antes, despues=despues, motivo=motivo, clave_idempotencia=clave, datos=datos)
        self.sesion.add(ev)
        self.sesion.flush()
        return ev

    def buscar_conocimiento(self, consulta: str, limite: int = 10) -> list[dict]:
        """Búsqueda de texto con permisos (RLS) y cita obligatoria: fichas sin fuente no se devuelven."""
        filas = self.sesion.execute(
            text(
                """
                SELECT f.id, f.codigo, f.titulo, f.estado, f.cliente_id,
                       ts_rank(f.busqueda, q) AS relevancia,
                       json_agg(json_build_object('codigo', fu.codigo, 'titulo', fu.titulo, 'url', fu.url,
                                                  'cita', ff.cita) ORDER BY fu.codigo) AS fuentes
                FROM ficha_conocimiento f
                CROSS JOIN websearch_to_tsquery('spanish', :consulta) q
                JOIN ficha_fuente ff ON ff.ficha_id = f.id
                JOIN fuente fu ON fu.id = ff.fuente_id
                WHERE f.busqueda @@ q AND f.estado NOT IN ('deprecated', 'raw')
                  AND (f.cliente_id IS NULL OR f.cliente_id = :cliente)
                GROUP BY f.id, q
                ORDER BY relevancia DESC, f.codigo
                LIMIT :limite
                """
            ),
            {"consulta": consulta, "cliente": self.cliente_id, "limite": limite},
        ).mappings()
        return [dict(f) for f in filas]
