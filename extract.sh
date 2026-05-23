#!/bin/bash
CALL_DIR=$(pwd)
export PYTHONPATH=/home/kevin/Documents/extract
python3 -c "
import sys, os
sys.argv = ['extract'] + sys.argv[1:]
from extract.cli import main
main()
" "$@"
