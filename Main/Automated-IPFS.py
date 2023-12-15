import hashlib
import requests
import time
import os
from web3 import Web3

def get_file_hash(file_path):
    """Compute the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def upload_to_ipfs(file_path):
    """Upload a file to IPFS using the HTTP API."""
    url = 'http://127.0.0.1:5001/api/v0/add'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()['Hash']

def send_hash_to_contract(web3, contract_address, account, private_key, ipfs_hash):
    """Send the IPFS hash to the smart contract."""
    abi = [
        {
            "inputs": [{"internalType": "string", "name": "x", "type": "string"}],
            "name": "sendHash",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getHash",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        }
    ]

    contract = web3.eth.contract(address=contract_address, abi=abi)
    nonce = web3.eth.get_transaction_count(account)
    gas_Price = web3.eth.gas_price
    txn = contract.functions.sendHash(ipfs_hash).build_transaction({
        'chainId': 43113,  # Avalanche Fuji, replace if you want to use a different chain
        'gas': 2000000,
        'gasPrice': gas_Price,
        'nonce': nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return txn_hash

def main():
    file_path = 'REPLACE_ME' # Replace with the file you want to upload
    check_interval = 5 # Time in seconds to wait between checks
    old_hash = get_file_hash(file_path) if os.path.exists(file_path) else None 

    while True:
        try:
            if old_hash is not None:
                new_hash = get_file_hash(file_path)

            if new_hash != old_hash:
                cid = upload_to_ipfs(file_path)
                print(f'File uploaded to IPFS with CID: {cid}')

                web3 = Web3(Web3.HTTPProvider('REPLACE_ME'))  # Replace with your node provider (Probably Infura)
                contract_address = Web3.to_checksum_address('REPLACE_ME') # Replace with your contract address
                account = 'REPLACE_ME'  # Replace with your account address
                private_key = 'REPLACE_ME'  # DO NOT USE A MAINNET FOR THIS TRANSACTION, replace this with your private key
                ipfs_hash = cid

                txn_hash = send_hash_to_contract(web3, contract_address, account, private_key, cid)
                print(f'Transaction hash: {txn_hash.hex()}')

                old_hash = new_hash
            else:
                print('File hash has not changed. No need to re-upload.')

            time.sleep(check_interval)

        except FileNotFoundError:
            print(f"File {file_path} not found. Will try again in {check_interval} seconds.")
            time.sleep(check_interval)
        except requests.RequestException as e:
            print(f'Error uploading to IPFS: {e}')
            time.sleep(check_interval)
        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(check_interval)

if __name__ == "__main__":
    main()
