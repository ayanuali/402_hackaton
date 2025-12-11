import os
import sys
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
from agent import PaymentAgent

load_dotenv()

def create_payment_rule():
    agent = PaymentAgent()

    print("\n=== Create Payment Rule ===")
    token = input("Token address (USDC): ").strip()
    recipient = input("Recipient address: ").strip()
    amount = int(input("Amount (in smallest units): "))
    interval = int(input("Interval (seconds): "))
    condition = input("Condition description: ").strip()

    try:
        tx = agent.contract.functions.createRule(
            token,
            recipient,
            amount,
            interval,
            condition
        ).build_transaction({
            'from': agent.account.address,
            'nonce': agent.w3.eth.get_transaction_count(agent.account.address),
            'gas': 200000,
            'gasPrice': agent.w3.eth.gas_price
        })

        signed_tx = agent.account.sign_transaction(tx)
        tx_hash = agent.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = agent.w3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"\nRule created successfully!")
        print(f"Transaction: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")

def list_rules():
    agent = PaymentAgent()
    user = input("User address: ").strip()

    rule_count = agent.contract.functions.ruleCount(user).call()
    print(f"\n{user} has {rule_count} rules:")

    for i in range(rule_count):
        rule = agent.contract.functions.getRule(user, i).call()
        is_exec = agent.contract.functions.isExecutable(user, i).call()

        print(f"\nRule {i}:")
        print(f"  Token: {rule[0]}")
        print(f"  Recipient: {rule[1]}")
        print(f"  Amount: {rule[2]}")
        print(f"  Interval: {rule[3]}s")
        print(f"  Active: {rule[4]}")
        print(f"  Condition: {rule[5]}")
        print(f"  Executable: {is_exec}")

def monitor_rules():
    agent = PaymentAgent()
    users = input("User addresses (comma-separated): ").strip().split(',')
    users = [u.strip() for u in users]

    print(f"\nMonitoring {len(users)} users...")
    agent.monitor_loop(users)

def main():
    print("=== Autonomous Payment Agent CLI ===")
    print("1. Create payment rule")
    print("2. List rules")
    print("3. Start monitoring")
    print("4. Exit")

    choice = input("\nSelect option: ").strip()

    if choice == '1':
        create_payment_rule()
    elif choice == '2':
        list_rules()
    elif choice == '3':
        monitor_rules()
    elif choice == '4':
        sys.exit(0)
    else:
        print("Invalid option")

if __name__ == '__main__':
    main()
