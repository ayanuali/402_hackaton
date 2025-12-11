# Railway Deployment Fixes

## Issues Found and Fixed

### 1. ✅ Python Version Updated
**Before:** `python310` in nixpacks.toml
**After:** `python311` in nixpacks.toml
**Reason:** Python 3.10 is older and may have compatibility issues with dependencies

### 2. ✅ Missing Environment Variables in .env.example
**Added:**
- `PAYMENT_AGENT_ADDRESS` - Required by simple_agent.py
- `MONITORED_USERS` - Required by simple_agent.py

**Why:** Railway deployment needs these variables, but they weren't documented

### 3. ✅ Added eth-abi Dependency
**Added:** `eth-abi==4.0.0` to requirements.txt
**Why:** Ensures ABI encoding/decoding works properly with web3.py

## Current Configuration

### Files
- `railway.json` - Railway platform config ✓
- `nixpacks.toml` - Build configuration ✓
- `Procfile` - Process definition ✓
- `runtime.txt` - Python version (3.11) ✓
- `agent/requirements.txt` - Dependencies ✓

### Required Environment Variables (Set in Railway Dashboard)
```
PRIVATE_KEY=<your_wallet_private_key>
CRONOS_RPC=https://evm-t3.cronos.org
PAYMENT_AGENT_ADDRESS=0x938C237a5A1F753fc1770960c31f1FD26D548bAc
MONITORED_USERS=<comma_separated_addresses>
```

## Testing the Fix

### Local Test
```bash
cd agent
export CRONOS_RPC=https://evm-t3.cronos.org
export PRIVATE_KEY=your_test_key
export PAYMENT_AGENT_ADDRESS=0x938C237a5A1F753fc1770960c31f1FD26D548bAc
export MONITORED_USERS=0xYourTestAddress

python3 simple_agent.py
```

### Expected Output
```
Agent initialized
Monitoring wallet: 0x...
Contract: 0x938C237a5A1F753fc1770960c31f1FD26D548bAc
User 0x... has N rules
Starting monitoring for 1 users
Check interval: 60 seconds
```

## Railway Deployment Checklist

- [x] Update Python version to 3.11
- [x] Add missing env vars to .env.example
- [x] Add eth-abi dependency
- [x] Create deployment documentation
- [ ] Set environment variables in Railway dashboard
- [ ] Push changes to GitHub
- [ ] Trigger Railway deployment
- [ ] Monitor Railway logs for successful startup
- [ ] Test payment execution

## Common Issues and Solutions

### Issue: "No users to monitor" Error
**Solution:** Set MONITORED_USERS environment variable in Railway dashboard
```
MONITORED_USERS=0xAddress1,0xAddress2,0xAddress3
```

### Issue: Build Fails with "Command not found: python"
**Solution:** Ensure nixpacks.toml specifies python311 correctly (already fixed)

### Issue: "Invalid private key"
**Solution:** Check PRIVATE_KEY format in Railway env vars (should be hex with or without 0x)

### Issue: Contract calls fail
**Solution:**
1. Verify PAYMENT_AGENT_ADDRESS is correct
2. Check contract is deployed on testnet
3. Verify RPC endpoint is accessible

## What Changed in Git

```bash
# View the changes
git diff HEAD

# Files modified:
# - nixpacks.toml (python310 → python311)
# - .env.example (added PAYMENT_AGENT_ADDRESS, MONITORED_USERS)
# - agent/requirements.txt (added eth-abi)
# - RAILWAY_DEPLOY.md (new file)
# - DEPLOYMENT_FIXES.md (new file)
```

## Next Steps

1. **Commit the fixes:**
   ```bash
   git add .
   git commit -m "fix: railway deployment configuration and dependencies"
   git push
   ```

2. **Configure Railway:**
   - Go to Railway dashboard
   - Add all required environment variables
   - Redeploy the service

3. **Verify deployment:**
   - Check Railway logs
   - Verify agent is monitoring
   - Test with a payment rule

4. **Update hackathon submission:**
   - Add Railway URL to README
   - Update HACKATHON_SUBMISSION.md
   - Document the live agent endpoint

## Contract Addresses (Cronos Testnet)

```
PaymentAgent: 0x938C237a5A1F753fc1770960c31f1FD26D548bAc
X402Executor: 0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6
```

Explorer: https://explorer.cronos.org/testnet

## Resources

- Railway Docs: https://docs.railway.app
- Nixpacks Docs: https://nixpacks.com
- Cronos Testnet: https://docs.cronos.org
