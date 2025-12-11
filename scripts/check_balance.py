#!/usr/bin/env python3

import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('CRONOS_RPC')))
address = os.getenv('WALLET_ADDRESS')

balance_wei = w3.eth.get_balance(address)
balance_cro = w3.from_wei(balance_wei, 'ether')

print(f"Address: {address}")
print(f"Balance: {balance_cro} CRO")

if balance_cro > 0:
    print("\nReady to deploy!")
else:
    print("\nNo balance. Get testnet CRO from: https://cronos.org/faucet")
