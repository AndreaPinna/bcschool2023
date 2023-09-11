// // SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.1;

contract Moneybox{
    uint256 deposits;
    address payable owner;
    constructor(){
        owner = payable(msg.sender);
    }
    function deposit() public payable {
        if (msg.value > 0) {
            deposits += 1;
        }
    }
    function withdrawal() public {
        owner.transfer(address(this).balance);
    }
    function getDeposits() public view returns(uint256 num_deposits){
        return deposits;
    }
}