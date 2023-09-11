# Andrea Pinna - Università di Cagliari
# 4th Scientific School on Blockchain & Distributed Ledger Technologies
# September 2023
# CC-BY

# Simple offline hash signer for the certificate emission example

from web3 import Web3, EthereumTesterProvider
import sys
import json

# Create a dummy connection
w3 = Web3(EthereumTesterProvider)

# Load account private key from crypted local file
with open("other files/key_user.json", "r") as file:
    data = json.load(file)
recoveredPK = w3.eth.account.decrypt(data, '1234')
account1 = w3.eth.account.from_key(recoveredPK)

print("Current signer account:", account1.address)

def signature(attendee, grade):
    #calculate data hash ->  keccak256(abi.encodePacked(student, grade)) in solidity
    dataHash=w3.solidity_keccak(['address','uint8'], [attendee,grade])
    hash_str = dataHash.hex()
    # sign the message(hash)
    signed_message = w3.eth.account.signHash(hash_str, account1.key)
    # get the signature
    sign = signed_message.signature.hex()
    print("Signature =", sign)

if __name__ == "__main__":
    attendee = sys.argv[1]
    grade = int(sys.argv[2])
    signature(attendee,grade)