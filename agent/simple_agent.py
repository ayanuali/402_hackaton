import os
import time
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

# Embedded ABI (no need for compiled artifacts)
PAYMENT_AGENT_ABI = [
    {"inputs": [{"name": "user", "type": "address"}, {"name": "ruleId", "type": "uint256"}], "name": "executePayment", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "user", "type": "address"}, {"name": "ruleId", "type": "uint256"}], "name": "isExecutable", "outputs": [{"name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"name": "user", "type": "address"}], "name": "ruleCount", "outputs": [{"name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"name": "user", "type": "address"}, {"name": "ruleId", "type": "uint256"}], "name": "getRule", "outputs": [{"components": [{"name": "token", "type": "address"}, {"name": "recipient", "type": "address"}, {"name": "amount", "type": "uint256"}, {"name": "interval", "type": "uint256"}, {"name": "lastExecution", "type": "uint256"}, {"name": "active", "type": "bool"}, {"name": "condition", "type": "string"}], "name": "", "type": "tuple"}], "stateMutability": "view", "type": "function"}
]

class SimplePaymentAgent:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('CRONOS_RPC')))
        self.account = Account.from_key(os.getenv('PRIVATE_KEY'))

        self.contract = self.w3.eth.contract(
            address=os.getenv('PAYMENT_AGENT_ADDRESS'),
            abi=PAYMENT_AGENT_ABI
        )

        print(f"Agent initialized")
        print(f"Monitoring wallet: {self.account.address}")
        print(f"Contract: {os.getenv('PAYMENT_AGENT_ADDRESS')}")

    def check_and_execute(self, user_address):
        try:
            rule_count = self.contract.functions.ruleCount(user_address).call()

            if rule_count == 0:
                return

            print(f"User {user_address} has {rule_count} rules")

            for rule_id in range(rule_count):
                try:
                    is_executable = self.contract.functions.isExecutable(user_address, rule_id).call()

                    if is_executable:
                        print(f"✓ Executing rule {rule_id} for {user_address}")
                        self.execute_payment(user_address, rule_id)
                    else:
                        print(f"  Rule {rule_id} not executable yet (waiting for interval or insufficient balance)")
                except Exception as e:
                    print(f"  Rule {rule_id} check failed: {str(e)[:100]}")

        except Exception as e:
            print(f"Error checking rules: {e}")

    def execute_payment(self, user_address, rule_id):
        try:
            tx = self.contract.functions.executePayment(
                user_address,
                rule_id
            ).build_transaction({
                'from': self.account.address,
                'nonce': self.w3.eth.get_transaction_count(self.account.address),
                'gas': 200000,
                'gasPrice': self.w3.eth.gas_price
            })

            signed_tx = self.account.sign_transaction(tx)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

            print(f"Payment executed! TX: {tx_hash.hex()}")
            print(f"Explorer: https://explorer.cronos.org/testnet/tx/{tx_hash.hex()}")

        except Exception as e:
            print(f"Execution failed: {e}")

    def monitor_loop(self, users, interval=60):
        print(f"Starting monitoring for {len(users)} users")
        print(f"Check interval: {interval} seconds")

        while True:
            for user in users:
                self.check_and_execute(user)

            time.sleep(interval)

if __name__ == '__main__':
    agent = SimplePaymentAgent()

    users = os.getenv('MONITORED_USERS', '').split(',')
    users = [u.strip() for u in users if u.strip()]

    if not users:
        print("ERROR: No users to monitor. Set MONITORED_USERS in environment")
        exit(1)

    agent.monitor_loop(users, interval=60)
