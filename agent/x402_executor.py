import os
import time
import secrets
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_structured_data
from dotenv import load_dotenv

load_dotenv()

class X402Executor:
    def __init__(self, w3, usdc_address, x402_contract_address):
        self.w3 = w3
        self.usdc_address = usdc_address
        self.x402_contract_address = x402_contract_address

        self.x402_abi = [
            {
                "inputs": [
                    {"name": "from", "type": "address"},
                    {"name": "to", "type": "address"},
                    {"name": "amount", "type": "uint256"},
                    {"name": "validAfter", "type": "uint256"},
                    {"name": "validBefore", "type": "uint256"},
                    {"name": "nonce", "type": "bytes32"},
                    {"name": "signature", "type": "bytes"}
                ],
                "name": "executeX402Payment",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]

        self.contract = self.w3.eth.contract(
            address=x402_contract_address,
            abi=self.x402_abi
        )

    def generate_nonce(self):
        return '0x' + secrets.token_hex(32)

    def create_authorization_signature(self, from_account, to_address, amount, valid_after, valid_before, nonce):
        domain = {
            'name': 'USD Coin',
            'version': '2',
            'chainId': self.w3.eth.chain_id,
            'verifyingContract': self.usdc_address
        }

        types = {
            'TransferWithAuthorization': [
                {'name': 'from', 'type': 'address'},
                {'name': 'to', 'type': 'address'},
                {'name': 'value', 'type': 'uint256'},
                {'name': 'validAfter', 'type': 'uint256'},
                {'name': 'validBefore', 'type': 'uint256'},
                {'name': 'nonce', 'type': 'bytes32'}
            ]
        }

        message = {
            'from': from_account.address,
            'to': to_address,
            'value': amount,
            'validAfter': valid_after,
            'validBefore': valid_before,
            'nonce': nonce
        }

        structured_data = {
            'types': types,
            'primaryType': 'TransferWithAuthorization',
            'domain': domain,
            'message': message
        }

        encoded = encode_structured_data(structured_data)
        signature = from_account.sign_message(encoded)

        return signature.signature

    def execute_x402_payment(self, from_account, to_address, amount, executor_account):
        nonce = self.generate_nonce()
        valid_after = int(time.time()) - 60
        valid_before = int(time.time()) + 3600

        signature = self.create_authorization_signature(
            from_account,
            to_address,
            amount,
            valid_after,
            valid_before,
            nonce
        )

        try:
            tx = self.contract.functions.executeX402Payment(
                from_account.address,
                to_address,
                amount,
                valid_after,
                valid_before,
                nonce,
                signature
            ).build_transaction({
                'from': executor_account.address,
                'nonce': self.w3.eth.get_transaction_count(executor_account.address),
                'gas': 300000,
                'gasPrice': self.w3.eth.gas_price
            })

            signed_tx = executor_account.sign_transaction(tx)
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
