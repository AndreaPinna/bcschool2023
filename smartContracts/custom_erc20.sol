// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.7;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";

contract SchoolToken is ERC20 {
    address owner;
    error notTheOwner(address _address);
    constructor() ERC20("BCSCHOOL", "BST")  {
        owner = msg.sender;
    }

    modifier onlyOwner(){
        if (msg.sender != owner) revert notTheOwner(msg.sender);
        _;
    }

    function mint(address recipient, uint256 quantity) public onlyOwner{
        _mint(recipient,quantity);
    }
}