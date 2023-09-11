# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

# Toy example for a multi-thread centralized oracle service


from web3_demos.contractInteraction.metaTransaction import metaTransaction
from web3_demos.deployBasic.compiler import compile
from web3 import Web3
import json
import time
import threading
import random

w3 = Web3(Web3.HTTPProvider('https://endpoints.omniatech.io/v1/eth/sepolia/public'))


# Initialization.
# In the following, a encrypted file containing the account of the
# oracle deployer (the owner) is expected.
# The smart contract address must be replaced with the
# actual smart contract deployed.

with open("../private_keys/key_server.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

# Smart Contract
abi,bytecode = compile("oracle")
address = '0xDF15aF232e6e3462a07903799F5763f281252204'
#'0x7A9C8415eB46F5BA2770bF955571e34C0Bae6874'
oracleContract = w3.eth.contract(abi=abi,address=address)

event_filter = oracleContract.events.dataRequest.create_filter(fromBlock='latest')


def data_retrieving():
    return str(random.random())

def listening():
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)


def handle_event(event):
    print("NEW REQUEST: ", event)
    data = data_retrieving()
    print("LISTEN New Data:", data)
    print("LISTEN nonce ",w3.eth.get_transaction_count(account1.address))
    try:
        receipt = metaTransaction(w3, account1, oracleContract, 0, 'update',data)
        print(receipt['transactionHash'].hex())
    except:
        print("Transaction pending")



def update_data():
    while True:
        data = data_retrieving()
        print("UPDATE New Data:", data)
        print("UPDATE nonce", w3.eth.get_transaction_count(account1.address))
        try:
            receipt = metaTransaction(w3, account1, oracleContract, 0, 'update',data)
            print(receipt['transactionHash'].hex())
        except:
            print("Transaction pending")
        time.sleep(60)


update_thread = threading.Thread(target=update_data, args=())
listening_thread = threading.Thread(target=listening, args=())

update_thread.start()
listening_thread.start()


