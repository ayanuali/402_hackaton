# Architecture

## System Overview

The Autonomous Payment Agent consists of three main components:

1. **Smart Contracts** - On-chain payment rules and x402 execution
2. **Agent Backend** - Python service that monitors and executes payments
3. **CLI Interface** - User interaction layer

## Smart Contracts

### PaymentAgent.sol

Stores user-defined payment rules with the following properties:
- Token address
- Recipient
- Amount
- Interval (time between executions)
- Condition (description)
- Active status

Functions:
- `createRule()` - User creates new payment rule
- `executePayment()` - Agent executes payment when conditions met
- `deactivateRule()` - User cancels rule
- `isExecutable()` - Check if rule can be executed

### X402Executor.sol

Handles gasless payment execution using x402 protocol:
- Uses EIP-3009 `transferWithAuthorization`
- User signs authorization once
- Agent executes with user's signature
- Agent pays gas fees

## Agent Backend

### agent.py

Main monitoring loop:
1. Checks each monitored user's rules
2. Identifies executable rules (interval passed, balance sufficient)
3. Executes payment via smart contract
4. Logs results

### x402_executor.py

Handles x402-specific signature creation and execution:
- Generates nonces
- Creates EIP-712 signatures
- Submits x402 transactions

### cli.py

Command-line interface for:
- Creating payment rules
- Viewing existing rules
- Starting monitoring service

## Flow

### Setup Flow

1. User deploys contracts
2. User creates payment rule via CLI
3. User approves token spending
4. Agent begins monitoring

### Execution Flow

1. Agent checks if rule is executable
2. If yes, agent builds transaction
3. Agent executes payment
4. Payment transfers tokens from user to recipient
5. Rule's lastExecution timestamp updates

### x402 Flow

1. User signs x402 authorization offline
2. Agent submits authorization + signature
3. x402 contract executes transfer
4. Agent pays gas, user pays nothing
