import os
import time
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

class PaymentAgent:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv('CRONOS_RPC')))
        self.account = Account.from_key(os.getenv('PRIVATE_KEY'))

        config_path = os.path.join(os.path.dirname(__file__), '../config/networks.json')
        if os.path.exists(config_path):
            with open(config_path) as f:
                self.config = json.load(f)
        else:
            self.config = {}

        self.payment_agent_address = os.getenv('PAYMENT_AGENT_ADDRESS')
        self.x402_executor_address = os.getenv('X402_EXECUTOR_ADDRESS')

        self.payment_agent_abi = self._load_abi('PaymentAgent')
        self.contract = self.w3.eth.contract(
            address=self.payment_agent_address,
            abi=self.payment_agent_abi
        )

    def _load_abi(self, contract_name):
        abi_path = os.path.join(os.path.dirname(__file__), f'../artifacts/contracts/{contract_name}.sol/{contract_name}.json')
        if not os.path.exists(abi_path):
            print(f"Warning: ABI file not found at {abi_path}")
            return []
        with open(abi_path) as f:
            artifact = json.load(f)
            return artifact['abi']

    def check_executable_rules(self, user_address):
        rule_count = self.contract.functions.ruleCount(user_address).call()
        executable_rules = []

        for rule_id in range(rule_count):
            is_executable = self.contract.functions.isExecutable(
                user_address,
                rule_id
            ).call()

            if is_executable:
                rule = self.contract.functions.getRule(user_address, rule_id).call()
                executable_rules.append({
                    'user': user_address,
                    'rule_id': rule_id,
                    'recipient': rule[1],
                    'amount': rule[2],
                    'condition': rule[5]
                })

        return executable_rules

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
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

            return {
                'success': True,
                'tx_hash': tx_hash.hex(),
                'receipt': receipt
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def monitor_loop(self, users, interval=60):
        print(f"Starting monitoring for {len(users)} users")

        while True:
            for user in users:
                executable_rules = self.check_executable_rules(user)

                if executable_rules:
                    print(f"Found {len(executable_rules)} executable rules for {user}")

                    for rule in executable_rules:
                        print(f"Executing rule {rule['rule_id']} for {user}")
                        result = self.execute_payment(user, rule['rule_id'])

                        if result['success']:
                            print(f"Payment executed: {result['tx_hash']}")
                        else:
                            print(f"Payment failed: {result['error']}")

            time.sleep(interval)

if __name__ == '__main__':
    agent = PaymentAgent()

    users_to_monitor = os.getenv('MONITORED_USERS', '').split(',')
    users_to_monitor = [u.strip() for u in users_to_monitor if u.strip()]

    if not users_to_monitor:
        print("No users to monitor. Add MONITORED_USERS to .env")
        exit(1)

    agent.monitor_loop(users_to_monitor)
