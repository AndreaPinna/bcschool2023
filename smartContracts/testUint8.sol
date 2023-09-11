// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.1;
contract Test_uint8 {
    uint8 public little;
    constructor() {
        little = 250;
    }
    function increment() public{
        little += 1;
	}
   function assign5() public{
        little = 5;
    }

   function decrement() public{
        little -= 1;
	}
}
