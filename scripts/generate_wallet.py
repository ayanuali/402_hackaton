#!/usr/bin/env python3

from eth_account import Account
import secrets

def generate_wallet():
    # Generate random private key
    private_key = "0x" + secrets.token_hex(32)

    # Create account from private key
    account = Account.from_key(private_key)

    print("=" * 60)
    print("NEW CRONOS TESTNET WALLET GENERATED")
    print("=" * 60)
    print()
    print("Address:", account.address)
    print()
    print("Private Key:", private_key)
    print()
    print("=" * 60)
    print("IMPORTANT: Save these securely!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Save private key to .env file")
    print("2. Get testnet CRO: https://cronos.org/faucet")
    print("3. Import to Metamask (optional):")
    print("   - Network: Cronos Testnet")
    print("   - RPC: https://evm-t3.cronos.org")
    print("   - Chain ID: 338")
    print()

if __name__ == "__main__":
    generate_wallet()
