# How to Test

## Quick Test (No Testnet Needed)

Run all local tests:
```bash
./scripts/test_local.sh
```

Or manually:
```bash
# Compile contracts
npm run compile

# Run tests
npm test
```

## What Gets Tested

The test suite verifies:

1. **Creating Payment Rules**
   - Users can create rules with recipient, amount, interval
   - Rule count increments correctly
   - Events are emitted

2. **Executing Payments**
   - Payments execute when conditions met
   - Tokens transfer correctly
   - Balance updates properly

3. **Interval Enforcement**
   - Can't execute same rule twice before interval passes
   - First execution works immediately
   - Second execution blocked until interval passes

4. **Rule Management**
   - Users can deactivate rules
   - Deactivated rules don't execute

## Test Output

You should see:
```
  PaymentAgent
    ✓ Should create a payment rule
    ✓ Should execute payment when conditions are met
    ✓ Should prevent early execution
    ✓ Should deactivate rule

  4 passing (291ms)
```

## Testing on Local Blockchain

Want to test the full agent? Use Hardhat's local network:

```bash
# Terminal 1: Start local blockchain
npx hardhat node

# Terminal 2: Deploy contracts locally
npx hardhat run scripts/deploy.js --network localhost

# Terminal 3: Run agent
cd agent
python agent.py
```

This runs a local blockchain on your machine (no testnet needed).

## Testing on Cronos Testnet

Once you have testnet CRO:

1. Deploy contracts:
   ```bash
   npm run deploy:testnet
   ```

2. Save contract addresses to `.env`

3. Create a test payment rule:
   ```bash
   cd agent
   python cli.py
   ```

4. Monitor execution:
   ```bash
   python agent.py
   ```

5. Check transactions on explorer:
   https://explorer.cronos.org/testnet

## Current Test Status

- [x] Smart contract tests passing
- [x] Local compilation works
- [ ] Deploy to testnet (waiting for CRO)
- [ ] End-to-end testnet flow
- [ ] Agent monitoring verified

## Troubleshooting

**Tests fail:**
- Run `npm install` first
- Make sure Node.js is installed
- Try `npm run compile` separately

**Can't deploy:**
- Check you have testnet CRO
- Verify `.env` has PRIVATE_KEY
- Check RPC endpoint is working

**Agent doesn't execute:**
- Verify contract addresses in `.env`
- Check MONITORED_USERS is set
- View agent logs for errors
