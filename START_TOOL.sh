#!/bin/bash
# Mac/Linux script to start the Midnight Consolidation Tool
# Double-click this file or run: ./START_TOOL.sh

echo ""
echo "============================================================"
echo "Starting Midnight Consolidation Tool..."
echo "============================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed!"
    echo ""
    echo "Please install Python 3:"
    echo "  Mac: Install from https://www.python.org/downloads/"
    echo "  Linux: sudo apt-get install python3"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# Start the tool
python3 START_TOOL.py
