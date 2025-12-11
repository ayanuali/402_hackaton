# Railway Deployment Guide

## Prerequisites

Before deploying to Railway, you need:

1. Railway account (https://railway.app)
2. Deployed smart contracts on Cronos testnet
3. Private key with some CRO for gas
4. User addresses to monitor

## Environment Variables

Set these in Railway dashboard:

```
PRIVATE_KEY=your_private_key_here
CRONOS_RPC=https://evm-t3.cronos.org
PAYMENT_AGENT_ADDRESS=0x938C237a5A1F753fc1770960c31f1FD26D548bAc
MONITORED_USERS=0xUserAddress1,0xUserAddress2
```

**Important:**
- `PRIVATE_KEY`: Wallet that will execute payments (pays gas)
- `PAYMENT_AGENT_ADDRESS`: Your deployed PaymentAgent contract
- `MONITORED_USERS`: Comma-separated list of user addresses to monitor
- `CRONOS_RPC`: Cronos testnet RPC endpoint

## Deployment Steps

### Option 1: Deploy from GitHub

1. Push your code to GitHub
2. Connect Railway to your repository
3. Railway will auto-detect the configuration from `railway.json`
4. Set environment variables in Railway dashboard
5. Deploy!

### Option 2: Deploy via Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link project
railway link

# Set environment variables
railway variables set PRIVATE_KEY=your_key_here
railway variables set CRONOS_RPC=https://evm-t3.cronos.org
railway variables set PAYMENT_AGENT_ADDRESS=0x938C237a5A1F753fc1770960c31f1FD26D548bAc
railway variables set MONITORED_USERS=0xUser1,0xUser2

# Deploy
railway up
```

## Configuration Files

- `railway.json`: Railway deployment config
- `nixpacks.toml`: Python build configuration
- `Procfile`: Process definition
- `runtime.txt`: Python version specification
- `agent/requirements.txt`: Python dependencies

## Monitoring

After deployment, check Railway logs:

```bash
railway logs
```

You should see:
```
Agent initialized
Monitoring wallet: 0x...
Contract: 0x938C237a5A1F753fc1770960c31f1FD26D548bAc
Starting monitoring for N users
Check interval: 60 seconds
```

## Troubleshooting

### Build Fails

**Issue**: Python dependencies fail to install
**Fix**: Check `nixpacks.toml` has correct Python version (3.11)

**Issue**: Missing environment variables
**Fix**: Verify all required env vars are set in Railway dashboard

### Runtime Fails

**Issue**: "No users to monitor" error
**Fix**: Set `MONITORED_USERS` environment variable with valid addresses

**Issue**: "Invalid private key" error
**Fix**: Ensure `PRIVATE_KEY` is a valid hex string (with or without 0x prefix)

**Issue**: Contract call failures
**Fix**: Verify `PAYMENT_AGENT_ADDRESS` is correct and deployed on testnet

### Agent Not Executing

**Issue**: Agent runs but doesn't execute payments
**Fix**:
- Ensure monitored users have active payment rules
- Check rules are actually executable (interval passed)
- Verify agent wallet has enough CRO for gas
- Check contract is approved to spend user tokens

## Cost Estimation

Railway pricing:
- Starter plan: $5/month
- Pro plan: $20/month

For hackathon:
- Use Starter plan (sufficient for demo)
- Agent uses minimal resources
- Main cost is gas on Cronos (paid from agent wallet)

## Security Notes

⚠️ **Never commit private keys to git**
- Use Railway's environment variables
- Keep separate testnet/mainnet keys
- Use a dedicated wallet for the agent

## Next Steps

After successful deployment:
1. Monitor logs to verify agent is running
2. Test payment execution with a test rule
3. Verify transactions on Cronos explorer
4. Update project documentation with Railway URL
