#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)
export PYTHONPATH="$SCRIPT_DIR"

if [[ "$1" == "--setup" ]]; then
    echo "Setting up dependencies for extract..."

    # Detect package manager
    if command -v apt-get &> /dev/null; then
        PKG_MGR="apt-get"
        SYS_DEPS="p7zip-full cpio rpm2cpio binutils"
        INSTALL_CMD="sudo apt-get update && sudo apt-get install -y"
    elif command -v pacman &> /dev/null; then
        PKG_MGR="pacman"
        SYS_DEPS="p7zip cpio rpm-tools binutils"
        INSTALL_CMD="sudo pacman -S --noconfirm"
    elif command -v dnf &> /dev/null; then
        PKG_MGR="dnf"
        SYS_DEPS="p7zip cpio rpm2cpio binutils"
        INSTALL_CMD="sudo dnf install -y"
    elif command -v zypper &> /dev/null; then
        PKG_MGR="zypper"
        SYS_DEPS="p7zip cpio rpm2cpio binutils"
        INSTALL_CMD="sudo zypper install -y"
    elif command -v apk &> /dev/null; then
        PKG_MGR="apk"
        SYS_DEPS="p7zip cpio rpm2cpio binutils"
        INSTALL_CMD="sudo apk add"
    else
        echo "Error: No supported package manager found."
        echo "------------------------------------------------------------------"
        echo "Manual Installation Guide:"
        echo "Please install the following tools manually using your system's package manager:"
        echo "  - 7-Zip (p7zip or p7zip-full)"
        echo "  - CPIO (cpio)"
        echo "  - RPM2CPIO (rpm2cpio or rpm-tools)"
        echo "  - Binutils (binutils)"
        echo "------------------------------------------------------------------"
        exit 1
    fi

    echo "Detected package manager: $PKG_MGR"
    echo "Installing system dependencies: $SYS_DEPS..."
    $INSTALL_CMD $SYS_DEPS

    echo "Installing Python dependencies..."
    python3 -m pip install --user rarfile zstandard

    echo "Setup complete! You can now use extract with all supported formats."
    exit 0
fi

python3 -c "
import sys
sys.argv = ['extract'] + sys.argv[1:]
from extract.cli import main
main()
" "$@"
