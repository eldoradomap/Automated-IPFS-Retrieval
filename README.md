# Project Title: IPFS Automation and Retrieval

## Description

This project contains Python scripts that demonstrate the integration of blockchain and IPFS (InterPlanetary File System). It includes functionality to monitor the Fuji blockchain transactions for a specific address, decode transaction input to extract an IPFS CID (Content Identifier), and download the corresponding file from IPFS. It also provides the Solidity script for deploying the CID hash to the blockchain.

## Features

- **Monitor Blockchain Transactions**: Watches for new transactions involving a specified address.
- **Decode Transaction Input**: Extracts and decodes the `input` field from transactions to find an IPFS CID.
- **Download from IPFS**: Downloads files from IPFS using the extracted CID.

## Requirements

- Python 3.x
- Access to an Ethereum node (e.g., via Infura)
- Access to an IPFS node or gateway
- Python packages: `requests`, `web3`, `eth-abi`

## Installation

1. Clone the repository:

   ```bash
   git clone http://Automated-IPFS-Retrieval
   ```

   2. Navigate to the project directory:

   ```bash
   cd Automated-IPFS-Retrieval/
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Publish the cidHasher.sol script to the blockchain using EVM Version paris, and Injected Provider you can do this very easily by using https://remix.ethereum.org/ Please make sure that you are using the Fuji Testnet in your Web3 wallet.

2. Update the `file_path`, `web3`, `contract_address`, `account`, `private_key`, `save_path`, `address` in the scripts with your specific details.

3. To start monitoring for transactions, run:

   ```bash
   python3 Automated-IPFS.py
   ```

4. To start monitoring for new CIDs posted to the blockchain, run:

   ```
   python3 Automated-Grab.py
   ```

## Configuration

- **Ethereum Node**: Set the `rpc_url` in the script to point to your Ethereum node or Infura endpoint.
- **Monitored Address**: Change the `address` variable to the Fuji address you want to monitor.
- **IPFS Gateway**: The default IPFS gateway is set to `https://gateway.pinata.cloud/ipfs/`. You can change it in the `download_file_from_ipfs` function.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

Include information about the project's license here.
