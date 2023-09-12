# Andrea Pinna - Università di Cagliari
# 4th Scientific School on Blockchain & Distributed Ledger Technologies
# September 2023
# CC-BY


# Simple transaction sender

from web3 import Web3
import json

# connect to sepolia
w3 = Web3(Web3.HTTPProvider('https://endpoints.omniatech.io/v1/eth/sepolia/public'))

# Load account private key from crypted local file
with open("other files/key_user.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

def send_transaction(fromAccount,toAddress,value):

    transaction = {
             'chainId':w3.eth.chain_id,
             'from':fromAccount.address,
             'to':toAddress,
             "value": value,
             }

    transaction.update({'gas': w3.eth.estimate_gas(transaction)})
    block = w3.eth.get_block('latest')
    transaction.update({'gasPrice': int(block.baseFeePerGas *1.01) })
    transaction.update({"nonce": w3.eth.get_transaction_count(fromAccount.address)})

    signed_tx = w3.eth.account.sign_transaction(transaction, fromAccount.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_receipt

if __name__ == "__main__":
    value = 1000
    dest = '0xB87330838482B2bF17Be31d09510dcc27abCC6E7'
    print("transaction from:", account1.address)
    print("transaction to:", dest)
    print("transaction value:", value, "wei")
    receipt= send_transaction(account1,dest,value)
    print(receipt)