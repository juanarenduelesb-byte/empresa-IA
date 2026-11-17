# Política de seguridad

**Estado:** propuesta, pendiente de aprobación de un socio. Orientativo: no es asesoría jurídica.

1. **Secretos:** ninguno en el repositorio. Van en un gestor de secretos, con rotación y revocación (P30).
2. **Datos de prueba:** hasta L2, solo datos inventados.
3. **Clientes:** el cliente sale de la identidad autenticada y el aislamiento se prueba con pruebas negativas.
4. **Contenido externo:** documentos, correos y páginas son datos, no instrucciones (P20).
5. **Mínimo privilegio:** en conectores y agentes, con un kill switch por componente.
6. **Incidentes:** se siguen los runbooks de `processes/runbooks/`. Para brechas con datos personales, se valora con asesoría la notificación a la AEPD en 72 horas.
7. **Proveedores:** cada proveedor se evalúa con su ficha antes de usarlo (contrato, región de datos, subencargados).
