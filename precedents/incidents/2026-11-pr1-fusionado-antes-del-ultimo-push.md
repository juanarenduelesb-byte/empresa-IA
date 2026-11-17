# Incidente: PR #1 fusionado antes del último push

- **Fecha:** noviembre de 2026 · **Detectado por:** Claude · **Gravedad:** baja
- **Qué pasó:** el PR #1 se fusionó en main mientras se subía un cambio más (la vista isométrica), que quedó solo en la rama antigua.
- **Impacto:** main estuvo un tiempo sin ese cambio.
- **Causa raíz:** no se comprobó el estado del PR antes de subir.
- **Corrección:** el cambio entró con el PR #2.
- **Acción preventiva:** antes de dar algo por publicado, comprobar que el commit está en `origin/main`.
- **Proceso:** P35.
