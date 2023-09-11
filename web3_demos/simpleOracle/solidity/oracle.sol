// SPDX-License-Identifier: MIT
// Andrea Pinna - Università di Cagliari
// Progetto e Sviluppo di Applicazioni Blockchain
// AA 2022-23

pragma solidity ^0.8.0;
contract MyOracle {
    address owner;
    string data;
    uint256 lastUpdate;

    event dataRequest(address);

    constructor(){
        owner = msg.sender;
    }

    function get() public view returns(string memory, uint256){
        return(data, lastUpdate);
    }

    function request() public {
        emit dataRequest(msg.sender);
    }


    function update(string memory _data) public {
        require(owner == msg.sender, "only the contract creator");
        data = _data;
        lastUpdate = block.timestamp;
    }
}
