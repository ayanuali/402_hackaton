#!/bin/bash

echo "========================================="
echo "Payment Agent Startup"
echo "========================================="
echo "Working directory: $(pwd)"
echo "Python version: $(python3 --version)"
echo ""
echo "Environment Variables:"
echo "CRONOS_RPC: ${CRONOS_RPC:0:30}..."
echo "PRIVATE_KEY: ${PRIVATE_KEY:0:10}...hidden"
echo "PAYMENT_AGENT_ADDRESS: $PAYMENT_AGENT_ADDRESS"
echo "MONITORED_USERS: $MONITORED_USERS"
echo ""
echo "Files in /app:"
ls -la /app
echo ""
echo "========================================="
echo "Starting agent..."
echo "========================================="

exec python3 simple_agent.py
