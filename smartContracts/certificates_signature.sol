// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "https://github.com/Normalities/OpenZepplin-contracts/blob/master/contracts/utils/cryptography/SignatureChecker.sol";

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


    // To run this function, a professor must sign offline the hash of the encodedPaked of attendee and grade,
    // and transmit it together with the attendee data to the contract owner, who actually creates the transaction.
    function createCertificate(address professor, bytes memory signature, address attendee, uint8 grade) public onlyOwner{
        require(professors[professor], "invalid professor");
        require(attendance[attendee], "invalid attendee");

        bytes32 hash = keccak256(abi.encodePacked(attendee, grade));
        require(checkSignature(professor, hash, signature), "invalid signature");
        saveCertificate(professor, signature, attendee, grade);
    }


    // this function uses the Openzeppelin library for signature verififaction, in a easier way.
    function checkSignature(address signer, bytes32 hash, bytes memory signature) private view returns(bool)
    {
        return SignatureChecker.isValidSignatureNow(signer, hash, signature);
    }




    function saveCertificate(address professor, bytes memory signature, address attendee, uint8 grade) private {
        certificates[attendee].grade = grade;
        certificates[attendee].professor = professor;
        certificates[attendee].timestamp = block.timestamp;
        certificates[attendee].signature = signature;
    }

    // add a function to allow the owner to get the contract balance.


}