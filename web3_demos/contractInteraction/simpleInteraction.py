# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

from web3 import Web3
import json
import metaTransaction

# connect to sepolia
w3 = Web3(Web3.HTTPProvider('https://endpoints.omniatech.io/v1/eth/sepolia/public'))

# Load account private key from crypted local file
with open("../private_keys/key_user.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

# create the contract local instance (storage.sol)
with open("storage_abi.json", "r") as file:
    ABI = json.load(file)
contractAddress = '0x3F11Cba2A361B4ba3F0B0bCe6366e1ea80552db9'
contractInstance = w3.eth.contract(address=contractAddress, abi=ABI)

# use the metaTransaction to call the function  store

receipt = metaTransaction.metaTransaction(w3,account1,contractInstance,0, 'store', 150)
print(receipt)

print(contractInstance.functions.retrieve().call() )

