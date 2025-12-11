# Final Testing Guide

## After Railway Deployment

### 1. Verify Agent is Running

In Railway dashboard:
- Check "Deployments" tab - should show "Active"
- Click "View Logs" - should see agent startup messages
- Look for: "Starting monitoring for X users"

### 2. Create Test Payment Rule

```bash
cd agent
python cli.py
```

**Option 1: Create payment rule**

Enter details:
- Token address: `0xc21223249CA28397B4B6541dfFaEcC539BfF0c59` (testnet USDC)
- Recipient: `0x0000000000000000000000000000000000000001` (any test address)
- Amount: `1000000` (1 USDC with 6 decimals)
- Interval: `60` (seconds)
- Condition: `test recurring payment`

### 3. Monitor Execution

**Check Railway Logs:**
- Should see: "Found X executable rules"
- Should see: "Executing rule 0"
- Should see: "Payment executed: 0x..."

**Check Cronos Explorer:**
Visit: https://explorer.cronos.org/testnet/address/0x938C237a5A1F753fc1770960c31f1FD26D548bAc

Look for:
- RuleCreated event
- PaymentExecuted event

### 4. Verify Transaction

Click on transaction hash in logs, should show:
- Status: Success
- From: Your wallet
- To: PaymentAgent contract
- Events: PaymentExecuted

## Test Scenarios

### Scenario 1: Recurring Payment (60 seconds)
- Create rule with 60 second interval
- Wait 60 seconds
- Agent should auto-execute
- Check transaction on explorer

### Scenario 2: Instant Payment (0 seconds)
- Create rule with 0 second interval
- Agent executes immediately
- Verify on explorer

### Scenario 3: Deactivate Rule
```bash
python cli.py
# Option 2: List rules
# Note the rule ID
# Then deactivate it
```

## Troubleshooting

**Agent not executing:**
- Check Railway logs for errors
- Verify MONITORED_USERS includes your wallet
- Check you have CRO for gas
- Verify contract addresses are correct

**Transaction fails:**
- Check USDC balance (need testnet USDC)
- Verify token approval
- Check gas price

**Can't create rule:**
- Verify wallet has CRO
- Check contract address
- Try with smaller amount

## Expected Results

After successful test:
- [x] Agent running on Railway
- [x] Payment rule created
- [x] Transaction on Cronos explorer
- [x] Logs show execution
- [x] Ready for demo video

## Next: Demo Video

Once testing complete, record 5-min video showing:
1. Live frontend
2. Creating payment rule
3. Agent executing
4. Transaction on explorer
5. Brief tech overview

Then submit to DoraHacks!
