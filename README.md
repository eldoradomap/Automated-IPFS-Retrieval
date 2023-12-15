# Project Title: Ethereum and IPFS Integration Script

## Description

This project contains Python scripts that demonstrate the integration of Ethereum blockchain and IPFS (InterPlanetary File System). It includes functionality to monitor Ethereum blockchain transactions for a specific address, decode transaction input to extract an IPFS CID (Content Identifier), and download the corresponding file from IPFS.

## Features

- **Monitor Ethereum Transactions**: Watches for new transactions involving a specified Ethereum address.
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
   git clone https://your-repository-url
   ```

2. Navigate to the project directory:

   ```bash
   cd path-to-your-project
   ```

3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the `rpc_url`, `address`, and other placeholders in the scripts with your specific details.

2. To start monitoring Ethereum transactions, run:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of the script you wish to run.

## Configuration

- **Ethereum Node**: Set the `rpc_url` in the script to point to your Ethereum node or Infura endpoint.
- **Monitored Address**: Change the `address` variable to the Ethereum address you want to monitor.
- **IPFS Gateway**: The default IPFS gateway is set to `https://ipfs.io/ipfs/`. You can change it in the `download_file_from_ipfs` function.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

Include information about the project's license here.
