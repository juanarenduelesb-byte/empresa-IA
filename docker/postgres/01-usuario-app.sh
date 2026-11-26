#!/bin/sh
# Crea el usuario de la aplicación (sin privilegios, sujeto a RLS) con la contraseña del entorno.
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v pass="$VARIOS_APP_PASSWORD" <<'SQL'
CREATE ROLE varios_app LOGIN PASSWORD :'pass';
SQL
