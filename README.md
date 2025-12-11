# Autonomous Payment Agent

AI agent for handling recurring and conditional payments on Cronos EVM using x402.

## What it does

Set up payment rules once, the agent executes them automatically:
- Recurring subscriptions (pay monthly, weekly, etc)
- Conditional payments (pay when event happens on-chain)
- Automated DCA into tokens
- Team payouts based on milestones

Uses x402 for gasless settlement and Crypto.com AI Agent SDK for natural language interaction.

## Stack

- Cronos EVM (testnet and mainnet)
- x402 payment protocol
- Crypto.com AI Agent SDK
- Solidity smart contracts
- Python backend

## Status

In development for Cronos x402 PayTech Hackathon.

## Quick Start

### Install Dependencies

```bash
npm install
cd agent && pip install -r requirements.txt
```

### Configure

```bash
cp .env.example .env
# Edit .env with your private key and RPC endpoint
```

### Deploy Contracts

```bash
npm run deploy:testnet
```

### Run Agent

```bash
cd agent
python cli.py
```

## Documentation

- [Setup Guide](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)

## Use Cases

**Recurring Payments**
- Subscription services
- Rent/lease payments
- Employee salaries

**Conditional Payments**
- Milestone-based payouts
- Automated DCA strategies
- Liquidity rebalancing

**Team Operations**
- Pay contributors when PR merges
- Reward completion of on-chain actions
- Automate treasury management

## How It Works

1. User creates payment rule (recipient, amount, interval)
2. User approves token spending once
3. Agent monitors on-chain state
4. When conditions met, agent executes payment via x402
5. User pays no gas (x402 handles it)

Built for Cronos x402 PayTech Hackathon.
