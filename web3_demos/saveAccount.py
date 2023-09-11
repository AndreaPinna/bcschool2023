# Andrea Pinna - Università di Cagliari
# 4th Scientific School on Blockchain & Distributed Ledger Technologies
# September 2023
# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

# Creation of the encrypted file for account management

from web3 import Web3, EthereumTesterProvider
import json
w3 = Web3(EthereumTesterProvider)

key = input("private key: ")
password = input("password: ")
filename = input("filename: ")
accountData = w3.eth.account.encrypt(key,password)
with open("private_keys/key_user.json", "w") as file:
    file.write(json.dumps(accountData))


