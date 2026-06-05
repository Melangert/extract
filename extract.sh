#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export PYTHONPATH="$SCRIPT_DIR"

python3 -c "
import sys
sys.argv = ['extract'] + sys.argv[1:]
from extract.cli import main
main()
" "$@"