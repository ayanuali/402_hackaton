# Testing Guide

## 1. Test Smart Contracts Locally (No Testnet Needed)

Run Hardhat tests against local blockchain:

```bash
# Compile contracts
npm run compile

# Run tests
npm test
```

This tests:
- Creating payment rules
- Executing payments
- Rule validation
- Access control

## 2. Test Agent Locally

We'll use Hardhat's local network to test the agent:

```bash
# Terminal 1: Start local blockchain
npx hardhat node

# Terminal 2: Deploy contracts to local network
npx hardhat run scripts/deploy.js --network localhost

# Terminal 3: Run agent against local network
cd agent
python agent.py
```

## 3. Manual Testing with CLI

Test the full flow locally:

```bash
cd agent
python cli.py
```

Options:
1. Create payment rule
2. List rules
3. Start monitoring

## 4. Testnet Testing (After Deployment)

Once deployed to Cronos testnet:

1. Create real payment rule
2. Monitor agent logs
3. Verify execution on explorer
4. Check transactions

## Test Scenarios

### Scenario 1: Recurring Payment
- Create rule: Pay 10 USDC every 60 seconds
- Wait 60 seconds
- Verify payment executed

### Scenario 2: Conditional Payment
- Create rule with condition
- Trigger condition
- Verify payment executed

### Scenario 3: Insufficient Balance
- Create rule for 1000 USDC (more than balance)
- Verify agent doesn't execute
- Check error handling

## Quick Test Commands

```bash
# Check contract compilation
npm run compile

# Run all tests
npm test

# Deploy to local hardhat network
npx hardhat node
npx hardhat run scripts/deploy.js --network localhost

# Check balance
python3 scripts/check_balance.py

# Test CLI
cd agent && python cli.py
```
