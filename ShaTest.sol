// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ShaTest {   
   function getsha256(string memory name) public pure returns(bytes32 result){
      return sha256(abi.encodePacked(name));
   }  
}
