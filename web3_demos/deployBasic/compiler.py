# Andrea Pinna - Università di Cagliari
# Blockchain School 2023
# AA 2022-23
# CC-BY

import solcx
solcx.install_solc('0.8.18')

def compile(contractInfo):
    """Returns ABI and Bytecode of a specific contract in a solidity file
     present in the folder /solidity """

    if type(contractInfo) == type([]):
        if len(contractInfo)>1:
            contractFileName=contractInfo[0]
            contractName = contractInfo[1]
    else:
        contractFileName = contractInfo
        contractName = ""
    with open("solidity/"+contractFileName+".sol","r") as sc_file:
        sc = ''
        lines = sc_file.readlines()
        for line in lines:
            sc = sc+line
    #print(sc)

    if not contractName:
        contract_id, contract_interface = solcx.compile_source(sc, output_values=['abi', 'bin']).popitem()
    else:
        contracts = solcx.compile_source(sc, output_values=['abi', 'bin'])
        contract_interface = contracts["<stdin>:"+contractName]

    abi = contract_interface['abi']
    bytecode = contract_interface['bin']
    return (abi, bytecode)

