# Deployment Guide

## Step 1: Get Testnet CRO

1. Your wallet address: `0xF1c4528A415792c12862CccB8FFfBF4003F8cD5c`
2. Go to: https://cronos.org/faucet
3. Paste address and request tokens
4. Check balance: `python3 scripts/check_balance.py`

## Step 2: Deploy Smart Contracts

Once you have CRO:

```bash
npm run compile
npm run deploy:testnet
```

Save the deployed contract addresses and add them to `.env`:
```
PAYMENT_AGENT_ADDRESS=0x...
X402_EXECUTOR_ADDRESS=0x...
```

## Step 3: Deploy Python Agent (Railway)

### Option A: Railway (Recommended)

1. Sign up at https://railway.app
2. Connect GitHub repo
3. Create new project from repo
4. Add environment variables:
   - PRIVATE_KEY
   - CRONOS_RPC
   - PAYMENT_AGENT_ADDRESS
   - X402_EXECUTOR_ADDRESS
   - MONITORED_USERS
5. Deploy

### Option B: Run Locally

```bash
cd agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python agent.py
```

## Step 4: Deploy Frontend (Vercel)

1. Go to https://vercel.com
2. Import GitHub repo
3. Set root directory to `frontend`
4. Deploy

Your site will be live at: `https://autonomous-payment-agent.vercel.app`

## Step 5: Test End-to-End

1. Create payment rule via CLI:
   ```bash
   cd agent
   python cli.py
   ```

2. Monitor agent logs (Railway dashboard or local terminal)

3. Verify payment execution on Cronos explorer

## Deployment Checklist

- [ ] Testnet wallet funded with CRO
- [ ] Contracts deployed to Cronos testnet
- [ ] Contract addresses saved to .env
- [ ] Python agent running on Railway
- [ ] Frontend deployed on Vercel
- [ ] Test payment rule created
- [ ] Test payment executed successfully
- [ ] Transactions verified on explorer

## Useful Links

- Cronos Testnet Explorer: https://explorer.cronos.org/testnet
- Railway Dashboard: https://railway.app/dashboard
- Vercel Dashboard: https://vercel.com/dashboard
- GitHub Repo: https://github.com/ayanuali/402_hackaton

## Troubleshooting

**Contract deployment fails:**
- Check you have enough CRO for gas
- Verify RPC endpoint is working
- Try again with higher gas price

**Agent not executing:**
- Check MONITORED_USERS is set correctly
- Verify contract addresses are correct
- Check agent has ETH for gas
- View logs in Railway dashboard

**Frontend not loading:**
- Check build logs in Vercel
- Verify all dependencies installed
- Try local build first: `npm run build`
