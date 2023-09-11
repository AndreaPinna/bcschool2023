// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract getBalanceOF {
    function getBalanceOf(address _address) public view returns(uint){
        return _address.balance;
    }
}
