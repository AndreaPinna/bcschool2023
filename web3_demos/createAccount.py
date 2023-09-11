# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

from web3 import Web3, EthereumTesterProvider
w3 = Web3(EthereumTesterProvider)
account = w3.eth.account.create()
print("address:",account.address)
print("private key:", account.key.hex())
