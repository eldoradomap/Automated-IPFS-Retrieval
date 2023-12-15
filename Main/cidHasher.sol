// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;
contract IPFS {
    string ipfsHash;
    
    function sendHash(string memory x) public {
        ipfsHash = x;
    }
    
    function getHash() public view returns (string memory) {
        return ipfsHash;
    }
}

//DEPLOY ME USING https://remix.ethereum.org/ USING EVM VERSION PARIS