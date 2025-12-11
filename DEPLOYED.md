# Deployed Contracts

## Cronos Testnet Deployment

**Network:** Cronos EVM Testnet
**Chain ID:** 338
**Explorer:** https://explorer.cronos.org/testnet

### Contract Addresses

**PaymentAgent:**
`0x938C237a5A1F753fc1770960c31f1FD26D548bAc`
https://explorer.cronos.org/testnet/address/0x938C237a5A1F753fc1770960c31f1FD26D548bAc

**X402Executor:**
`0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6`
https://explorer.cronos.org/testnet/address/0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6

**Testnet USDC:**
`0xc21223249CA28397B4B6541dfFaEcC539BfF0c59`

### Deployment Wallet

**Address:** `0xF1c4528A415792c12862CccB8FFfBF4003F8cD5c`
**Balance:** 50 CRO

### Next Steps

1. Test creating payment rule
2. Monitor agent execution
3. Verify transactions on explorer
4. Deploy frontend to Vercel
5. Deploy agent to Railway

### Verification

Check deployment:
```bash
python3 scripts/check_balance.py
```

View on explorer:
- PaymentAgent: https://explorer.cronos.org/testnet/address/0x938C237a5A1F753fc1770960c31f1FD26D548bAc
- X402Executor: https://explorer.cronos.org/testnet/address/0x93d296EE43EEB00A7DE563d35B2c84283DEA47f6

### Test Payment Rule

Create a test rule:
```bash
cd agent
python cli.py
```

Monitor execution:
```bash
python agent.py
```

## Status

- [x] Contracts deployed to testnet
- [x] Addresses saved to .env
- [ ] Payment rule created
- [ ] Agent monitoring active
- [ ] Frontend deployed
- [ ] Agent hosted on Railway
