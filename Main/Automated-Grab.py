import os
import requests
import json
import time
import eth_abi
from web3 import Web3

def get_latest_block_transactions(rpc_url):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", True],  # True to get full transaction objects
        "id": 1
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(rpc_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.json().get('result', {}).get('transactions', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def find_transaction_for_address(transactions, address):
    for tx in transactions:
        if tx.get('from').lower() == address.lower() or tx.get('to').lower() == address.lower():
            return tx['hash']
    return None

def get_transaction_by_hash(rpc_url, tx_hash):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionByHash",
        "params": [tx_hash],
        "id": 1
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(rpc_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def decode_sendhash_input(input_data):
    signature_hash = Web3.keccak(text='sendHash(string)').hex()[:10]
    if input_data.startswith(signature_hash):
        encoded_parameter = input_data[10:]
        decoded = eth_abi.decode(['string'], bytes.fromhex(encoded_parameter))
        return decoded[0]
    else:
        return "Input data does not match the function signature."

def download_file_from_ipfs(cid, save_path):
    ipfs_gateway = 'https://gateway.pinata.cloud/ipfs/'
    url = f"{ipfs_gateway}{cid}"
    
    try:
        response = requests.get(url, stream=True, timeout=60)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"File downloaded successfully: {save_path}")

            # Additional debugging: Check the file size
            file_size = os.path.getsize(save_path)
            print(f"Downloaded file size: {file_size} bytes")
        else:
            print(f"Error downloading file: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def monitor_address_transactions(rpc_url, address, interval=10):
    while True:
        transactions = get_latest_block_transactions(rpc_url)
        latest_tx_hash = find_transaction_for_address(transactions, address)

        if latest_tx_hash:
            print(f"Latest transaction hash for address {address}: {latest_tx_hash}")

            transaction_data = get_transaction_by_hash(rpc_url, latest_tx_hash)
            if transaction_data and 'result' in transaction_data and 'input' in transaction_data['result']:
                input_data = transaction_data['result']['input']
                cid = decode_sendhash_input(input_data)
                print(f"Decoded CID: {cid}")
                save_path = f'REPLACE_ME'  # Replace with where and what name you want the file to be saved as (be sure to include proper file extension i.e. .txt .xlsx)
                download_file_from_ipfs(cid, save_path)

        time.sleep(interval)

        time.sleep(interval)

rpc_url = 'https://api.avax-test.network/ext/bc/C/rpc' 
address = 'REPLACE_ME' # Replace with your contract address
monitor_interval = 0.5

monitor_address_transactions(rpc_url, address, monitor_interval)
