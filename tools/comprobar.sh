#!/usr/bin/env bash
# Comprobaciones antes de subir (las mismas que CI). Sale con error si algo falla.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/brain_build.py oficina/brain.json >/dev/null
ruff check src migrations tests tools/pg_local.py
python3 -m pytest -q
python3 tools/check_repo.py
python3 tools/org_gen.py --check
python3 tools/agentes_gen.py --check
echo "Todo en verde."
