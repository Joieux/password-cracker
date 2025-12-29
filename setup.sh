#!/bin/bash
# Setup script for Password Cracker

echo "=================================="
echo "Password Cracker Setup"
echo "=================================="
echo ""

# Check Python version
echo "[1/4] Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.6"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then 
    echo "✓ Python $python_version detected (3.6+ required)"
else
    echo "✗ Python 3.6+ required but $python_version found"
    exit 1
fi

# Make scripts executable
echo ""
echo "[2/4] Making scripts executable..."
chmod +x main.py
chmod +x agentic_cracker.py
chmod +x demo.py
echo "✓ Scripts are now executable"

# Run tests
echo ""
echo "[3/4] Running unit tests..."
python3 tests/test_cracker.py
if [ $? -eq 0 ]; then
    echo "✓ All tests passed"
else
    echo "✗ Some tests failed"
    exit 1
fi

# Quick functionality test
echo ""
echo "[4/4] Running quick functionality test..."
test_hash="5f4dcc3b5aa765d61d8327deb882cf99"  # MD5 of "password"
python3 main.py -H $test_hash -m dictionary -w wordlists/common.txt -t 2 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Cracker is working correctly"
else
    echo "✗ Cracker test failed"
    exit 1
fi

echo ""
echo "=================================="
echo "Setup Complete! 🎉"
echo "=================================="
echo ""
echo "Quick Start:"
echo "  ./main.py -H <hash> -m dictionary -w wordlists/common.txt"
echo "  ./agentic_cracker.py -H <hash> --context 'user info'"
echo "  ./demo.py  (to see examples)"
echo ""
echo "Documentation:"
echo "  README.md - Main documentation"
echo "  AGENTIC_README.md - AI version docs"
echo ""
