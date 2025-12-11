#!/bin/bash

echo "=== Testing Autonomous Payment Agent ==="
echo ""

echo "Step 1: Compiling contracts..."
npm run compile
if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi
echo "✓ Contracts compiled"
echo ""

echo "Step 2: Running tests..."
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed!"
    exit 1
fi
echo "✓ All tests passed"
echo ""

echo "=== Local Testing Complete ==="
echo ""
echo "Next steps:"
echo "1. Get testnet CRO from https://cronos.org/faucet"
echo "2. Deploy to testnet: npm run deploy:testnet"
echo "3. Test on actual network"
