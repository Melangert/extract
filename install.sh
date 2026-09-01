#!/bin/bash
# Installation script for extract tool

# Get the absolute path of the script directory
INSTALL_DIR=$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)
TARGET_BIN="/usr/local/bin/extract"

echo "Installing extract..."

# Check for sudo privileges
if ! command -v sudo &> /dev/null; then
    echo "Error: sudo is not installed. Please install sudo or run as root."
    exit 1
fi

# Create the symbolic link
# -s: symbolic
# -f: force (overwrite existing)
if sudo ln -sf "$INSTALL_DIR/extract.sh" "$TARGET_BIN"; then
    echo "Successfully linked extract to $TARGET_BIN"
else
    echo "Error: Failed to create symbolic link. Did you enter the correct sudo password?"
    exit 1
fi

echo "------------------------------------------------------------------"
echo "Installation complete!"
echo "You can now use the 'extract' command from anywhere in your terminal."
echo ""
echo "IMPORTANT: Run the following command to install all necessary"
echo "dependencies (7zip, cpio, etc.) for all supported formats:"
echo ""
echo "  extract --setup"
echo "------------------------------------------------------------------"
