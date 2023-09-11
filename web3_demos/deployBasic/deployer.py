# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

import compiler


def deployName(w3, contractName, account, value, *params):
    (abi, bytecode) = compiler.compile(contractName)
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    transaction = contract.constructor(*params).build_transaction(
        {
            'chainId': w3.eth.chain_id,
            'from': account.address,
            "value": value,
        })

    transaction.update({'gas': w3.eth.estimate_gas(transaction)})
    #block = w3.eth.get_block('latest')
    #transaction.update({'gasPrice': int(block.baseFeePerGas * 1.01)})
    transaction.update({"nonce": w3.eth.get_transaction_count(account.address)})

    signed_tx = w3.eth.account.sign_transaction(transaction, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt



