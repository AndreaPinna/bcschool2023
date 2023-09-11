# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

# this function simplify the interaction with smart contracts.

# Note: w3 is web3_demos instance.

def metaTransaction(w3, account, contract, value, function, *parameters ):
	transaction = getattr(contract.functions, function)(*parameters).build_transaction({
		"chainId": w3.eth.chain_id,
		"from": account.address,
		"value": value,
		"gasPrice" : w3.eth.gas_price})

	transaction.update({"nonce": w3.eth.get_transaction_count(account.address)})
	transaction.update({'gas': w3.eth.estimate_gas(transaction)})

	signed_tx = w3.eth.account.sign_transaction(transaction, account.key)
	tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
	return tx_receipt