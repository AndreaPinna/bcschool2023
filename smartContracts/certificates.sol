// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract certification{

    struct certificate{
        uint8 grade;
        address professor;
        uint timestamp;
        bytes signature;

    }


    uint price = 1 ether / 1000;
    address owner;
    mapping (address => bool) attendance;
    mapping (address => bool) professors;
    mapping (address => certificate) certificates;

     constructor(){
        owner = msg.sender;
    }
    modifier onlyOwner(){
        require(msg.sender == owner, "only the owner");
        _;
    }

    function addMe() public payable{
        require(!attendance[msg.sender], "you are already registered");
        require(msg.value == price, "invalid amount");
        attendance[msg.sender]=true;
    }


    function checkAttendance(address attendee) public view returns (bool){
        return attendance[attendee];
    }

    function addProfesor(address professor) public onlyOwner{
        professors[professor] = true;

    }

/*
    function saveCertificate(bytes memory signature, address attendee, uint8 grade) public {
        require(professors[msg.sender], "invalid professor" );
        certificates[attendee].grade = grade;
        certificates[attendee].professor = msg.sender;
        certificates[attendee].timestamp = block.timestamp;

    }
*/
    // add a function to allow the owner to get the contract balance.


}