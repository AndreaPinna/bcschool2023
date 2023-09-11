// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.17;

//import "https://github.com/Normalities/OpenZepplin-contracts/blob/master/contracts/utils/cryptography/SignatureChecker.sol";
import "OpenZeppelin/utils/cryptography/SignatureChecker.sol";

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


    function checkAttendance(address participant) public view returns (bool){
        return attendance[participant];
    } 

    function addProfesor(address professor) public onlyOwner{
        professors[professor] = true;

    }

    
    
    function createCertificate(address professor, bytes memory signature, address student, uint8 grade) public onlyOwner{
        require(professors[professor], "invalid professor");
        require(attendance[student], "invalid student");
        
        bytes32 hash = keccak256(abi.encodePacked(student, grade));
        require(checkSignature(professor, hash, signature), "invalid signature");       
        saveCertificate(professor, signature, student, grade);
    }
    
  

    
    function hashData(address student, uint8 grade) public pure returns(bytes32)
    {
        bytes32 hash = keccak256(abi.encodePacked(student, grade));
        return hash;
    }

    function checkSignature(address signer, bytes32 hash, bytes memory signature) private view returns(bool)
    {
        return SignatureChecker.isValidSignatureNow(signer, hash, signature);    }  

    function saveCertificate(address professor, bytes memory signature, address student, uint8 grade) private {
        certificates[student].grade = grade;
        certificates[student].professor = professor;
        certificates[student].timestamp = block.timestamp;
        certificates[student].signature = signature;
    }

 
}