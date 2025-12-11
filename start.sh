#!/bin/bash
set -e

echo "Starting Payment Agent..."
echo "Working directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Files in /app:"
ls -la /app

exec python simple_agent.py
