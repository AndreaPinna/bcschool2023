# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

# Toy example for the oracle user dApp

from web3 import Web3
import json
from web3_demos.contractInteraction import metaTransaction

from web3_demos.deployBasic.compiler import compile

# from web3_demos.middleware import construct_sign_and_send_raw_middleware

w3 = Web3(Web3.HTTPProvider('https://endpoints.omniatech.io/v1/eth/sepolia/public'))



# Initialization.
# In the following, a encrypted file containing the account of the
# user is expected.
# The smart contract address must be replaced with the
# actual smart contract deployed.


with open("../private_keys/key_user.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

abi, bytecode = compile("oracle")
mycontract = w3.eth.contract(abi=abi,address='0xDF15aF232e6e3462a07903799F5763f281252204')

#print(w3.eth.chain_id)
#print(w3.eth.get_transaction_count(account1.address))

def get():
    return mycontract.functions.get().call()

def request():
    receipt = metaTransaction.metaTransaction(w3, account1, mycontract, 0, 'request')
    return receipt['transactionHash'].hex()




