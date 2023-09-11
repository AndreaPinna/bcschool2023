// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.1;

contract SaveValue {
	uint16 public myValue;
    uint16 public numWriting;
	constructor() {
		myValue = 10;
	}


    function incrementNumWriting() private{
        numWriting +=1;
    }

    function writeValue(uint16 _valore) public{
        incrementNumWriting();
        myValue = _valore;
    }
}