#!/bin/bash
# Inicia la estación USB y el dashboard desde cualquier carpeta.
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
PYTHON="$PROJECT_DIR/.venv/bin/python"

if [[ ! -x "$PYTHON" ]]; then
  BOOTSTRAP_PYTHON=""
  for candidate in python3.11 python3.12 python3; do
    if command -v "$candidate" >/dev/null 2>&1 &&
       "$candidate" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
      BOOTSTRAP_PYTHON="$candidate"
      break
    fi
  done
  if [[ -z "$BOOTSTRAP_PYTHON" ]]; then
    echo "Se requiere Python 3.10 o posterior; se recomienda Python 3.11." >&2
    exit 1
  fi
  echo "Preparando el entorno local .venv..."
  "$BOOTSTRAP_PYTHON" -m venv "$PROJECT_DIR/.venv"
fi

if ! "$PYTHON" -c 'import sys; sys.exit(sys.version_info < (3, 10))'; then
  echo "El entorno .venv requiere Python 3.10 o posterior." >&2
  exit 1
fi
if ! "$PYTHON" -c 'import importlib.util, sys; sys.exit(any(importlib.util.find_spec(m) is None for m in ("serial", "meshtastic", "pubsub")))'; then
  echo "Instalando dependencias de la estación..."
  "$PYTHON" -m pip install -r "$PROJECT_DIR/station/requirements.txt"
fi

exec "$PYTHON" -u "$PROJECT_DIR/tools/iniciar.py" "$@"
