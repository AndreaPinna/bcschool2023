// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;
contract Target{
    function checkCaller() public view returns(bool check) {
        return msg.sender == tx.origin;
    }
}

contract Caller{
    function callTarget(address _targetAddress) public view returns(bytes memory){
        // create the function payload (no argumnents)
        bytes memory payload = abi.encodeWithSignature("checkCaller()");
        // execute the call
        (bool success, bytes memory result) = _targetAddress.staticcall(payload);
        return result;
	}
}