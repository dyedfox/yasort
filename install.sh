#!/bin/bash

# Exit on any error
set -e

TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Clone, install, and cleanup all in one go
git clone https://github.com/dyedfox/yasort.git .

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_NAME="yasort.py"
EXECUTABLE_NAME="yasort"  # Change this to your desired command name
INSTALL_DIR="/usr/local/bin"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${YELLOW}Installing ${EXECUTABLE_NAME}...${NC}"

# Check if script exists
if [ ! -f "$SCRIPT_DIR/$SCRIPT_NAME" ]; then
    echo -e "${RED}Error: $SCRIPT_NAME not found in current directory${NC}"
    exit 1
fi

# Check if running as root for system-wide installation
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}Note: Installing to user directory (~/.local/bin) instead of system-wide${NC}"
    INSTALL_DIR="$HOME/.local/bin"
    mkdir -p "$INSTALL_DIR"
    
    # Add to PATH if not already there
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo -e "${YELLOW}Adding ~/.local/bin to PATH in ~/.bashrc${NC}"
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        echo -e "${YELLOW}Please run 'source ~/.bashrc' or restart your terminal${NC}"
    fi
fi

# Install Python dependencies if requirements.txt exists
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo -e "${YELLOW}Installing Python dependencies...${NC}"
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
fi

# Make the Python script executable
chmod +x "$SCRIPT_DIR/$SCRIPT_NAME"

# Ensure the script has a proper shebang
if ! head -n 1 "$SCRIPT_DIR/$SCRIPT_NAME" | grep -q "^#!"; then
    echo -e "${YELLOW}Adding shebang to script...${NC}"
    # Create a temporary file with shebang
    echo '#!/usr/bin/env python3' > /tmp/temp_script
    cat "$SCRIPT_DIR/$SCRIPT_NAME" >> /tmp/temp_script
    mv /tmp/temp_script "$SCRIPT_DIR/$SCRIPT_NAME"
    chmod +x "$SCRIPT_DIR/$SCRIPT_NAME"
fi

# Copy the script (same for both cases since INSTALL_DIR is already set correctly)
cp "$SCRIPT_DIR/$SCRIPT_NAME" "$INSTALL_DIR/$EXECUTABLE_NAME"

# Different messages based on installation type
if [ "$EUID" -eq 0 ]; then
    echo -e "${GREEN}Script installed system-wide to $INSTALL_DIR/$EXECUTABLE_NAME${NC}"
else
    echo -e "${GREEN}Script installed to $INSTALL_DIR/$EXECUTABLE_NAME${NC}"
fi

# Verify installation
if command -v "$EXECUTABLE_NAME" &> /dev/null; then
    echo -e "${GREEN}✓ Installation successful! You can now run: $EXECUTABLE_NAME${NC}"
else
    echo -e "${YELLOW}Installation completed, but $EXECUTABLE_NAME is not in PATH${NC}"
    echo -e "${YELLOW}You may need to restart your terminal or run: source ~/.bashrc${NC}"
fi

echo -e "${GREEN}Installation complete!${NC}"

# Cleanup
cd ~
rm -rf "$TEMP_DIR"