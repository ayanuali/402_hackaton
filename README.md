# Autonomous Payment Agent

An AI-powered agent that automatically executes recurring and conditional payments on Cronos EVM using the x402 protocol. The agent monitors on-chain conditions and executes payments without requiring manual intervention or gas fees from users.

## Overview

This project implements an autonomous payment system where users define payment rules once, and an AI agent handles execution automatically. The system uses Cronos x402 for gasless settlement, meaning users never pay transaction fees for automated payments.

The agent runs continuously, monitoring blockchain state and executing payments when conditions are met. This enables use cases like subscription payments, scheduled transfers, milestone-based payouts, and automated treasury management.

## How It Works

The system consists of three main components:

**Smart Contracts**: On-chain logic for creating and storing payment rules. Users interact with the PaymentAgent contract to define rules specifying token, recipient, amount, and execution interval.

**Autonomous Agent**: A Python application that monitors the blockchain for executable payment rules. The agent checks conditions at regular intervals and submits transactions when rules are ready to execute.

**x402 Protocol**: Handles gasless execution by allowing the agent to pay gas fees on behalf of users. Users approve token spending once, then all subsequent payments execute without additional user interaction.

### Execution Flow

1. User creates a payment rule through the contract, specifying recipient address, token, amount, and interval
2. User approves the PaymentAgent contract to spend their tokens (one-time approval)
3. Agent continuously monitors the blockchain for executable rules
4. When a rule's interval has elapsed and the user has sufficient balance, the agent executes the payment
5. The contract transfers tokens from user to recipient, updates the rule's last execution timestamp
6. Agent continues monitoring for the next execution cycle

## Architecture

### Smart Contracts

`PaymentAgent.sol` - Main contract managing payment rules. Stores user-defined rules and enforces execution conditions.

`X402Executor.sol` - Handles x402 protocol integration for gasless transactions.

`MockERC20.sol` - Test token contract for development and testing.

### Agent Backend

`simple_agent.py` - Standalone monitoring agent that runs continuously, checking for executable rules.

`agent.py` - Full-featured agent with additional functionality for complex workflows.

`cli.py` - Command-line interface for creating rules and checking status.

### Frontend

Next.js application displaying live statistics from the blockchain. Shows total rules, active rules, and execution count by querying the PaymentAgent contract directly.

## Use Cases

**Recurring Subscriptions**: Users can set up monthly or weekly payments for services without manual intervention each period.

**Team Payroll**: Organizations can automate regular payments to contributors on a defined schedule.

**Dollar-Cost Averaging**: Automatically purchase tokens at regular intervals to implement DCA strategies.

**Milestone Payments**: Execute payments when specific on-chain conditions are met, such as project milestones.

**Treasury Automation**: Manage organizational treasuries with scheduled transfers and automated rebalancing.

## Technical Stack

- Cronos EVM for smart contract execution
- x402 protocol for gasless transactions
- Solidity for contract development
- Python for agent implementation
- ethers.js for blockchain interaction
- Next.js for frontend

## Deployment

**Live Application**: https://402-hackaton.vercel.app/

**Deployed Contracts (Cronos Testnet)**:
- PaymentAgent: `0x938C237a5A1F753fc1770960c31f1FD26D548bAc`
- X402Executor: `0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6`
- Test USDC: `0xc21223249CA28397B4B6541dfFaEcC539BfF0c59`

**Agent**: Running on Railway, monitoring testnet continuously

## Getting Started

### Prerequisites

- Node.js 18 or higher
- Python 3.9 or higher
- Cronos testnet wallet with CRO for gas

### Installation

Install contract dependencies:
```bash
npm install
```

Install agent dependencies:
```bash
cd agent
pip install -r requirements.txt
```

### Configuration

Copy the environment template:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
PRIVATE_KEY=your_wallet_private_key
CRONOS_RPC=https://evm-t3.cronos.org
PAYMENT_AGENT_ADDRESS=deployed_contract_address
```

### Deploy Contracts

Compile contracts:
```bash
npm run compile
```

Deploy to testnet:
```bash
npm run deploy:testnet
```

### Run Agent Locally

Start the monitoring agent:
```bash
cd agent
python simple_agent.py
```

Or use the CLI for interactive management:
```bash
python cli.py
```

## Project Structure

```
/contracts          Smart contract source files
/agent             Python agent implementation
/scripts           Deployment and utility scripts
/frontend          Next.js web application
/docs              Additional documentation
```

## Development

This project was built for the Cronos x402 PayTech Hackathon. It demonstrates the capabilities of autonomous agents combined with gasless transaction protocols to create seamless payment automation.

The implementation focuses on reliability and user experience. Users interact with the system once to set up rules, then the agent handles all subsequent execution without further user action.

## License

MIT
