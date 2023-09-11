# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

from web3 import Web3
import json
import deployer
import compiler

# connect to sepolia
w3 = Web3(Web3.HTTPProvider('https://endpoints.omniatech.io/v1/eth/sepolia/public'))

# Load account private key from crypted local file
with open("../private_keys/key_user.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

contractName = "storage"

# DEPLOY
receipt = deployer.deployName(w3,contractName, account1, 0)
contractAddress = receipt.contractAddress
print(receipt)
print("contract Address: ", contractAddress)

# local instance:
(contractABI, bytecode) = compiler.compile(contractName)
contractInstance = w3.eth.contract(address=contractAddress, abi=contractABI)

# to save the generated ABI.
# with open('storage_abi.json', 'w') as f:
#    json.dump(contractABI, f)

# static-call
print ( contractInstance.functions.retrieve().call() )





