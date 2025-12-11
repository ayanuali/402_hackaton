# Setup Guide

## Prerequisites

- Node.js 18+
- Python 3.9+
- Cronos testnet wallet with CRO for gas

## Installation

### Smart Contracts

```bash
npm install
```

### Python Agent

```bash
cd agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Fill in your values:

```
PRIVATE_KEY=your_private_key_here
CRONOS_RPC=https://evm-t3.cronos.org
USDC_ADDRESS=0x...
PAYMENT_AGENT_ADDRESS=0x...
X402_EXECUTOR_ADDRESS=0x...
MONITORED_USERS=0x...,0x...
```

## Deploy Contracts

Compile:
```bash
npm run compile
```

Deploy to testnet:
```bash
npm run deploy:testnet
```

Save the deployed contract addresses to your `.env` file.

## Run Agent

```bash
cd agent
source venv/bin/activate
python cli.py
```

## Testing

Run contract tests:
```bash
npm test
```

## Get Testnet Tokens

1. Get CRO from faucet: https://cronos.org/faucet
2. Get testnet USDC (if available on testnet)
