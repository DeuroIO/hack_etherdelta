from web3 import Web3, HTTPProvider, IPCProvider
web3 = Web3(HTTPProvider('http://localhost:8545'))
from web3_helper import getTransactionsByAccount
#according to etherscan
#https://etherscan.io/token/generic-tokentxns2?contractAddress=0xe41d2489571d322189246dafa5ebde1f4699f498&mode=&a=0x8d12A197cB00D4747a1fe03395095ce2A5CC6819&p=508
#the first 0x trade on etherdelta is the block 4161334
start_block = 4161334

#should change this to current latest block
end_block = web3.eth.blockNumber

#zero_x contract address
myaccount = "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819"
zero_x_contract_address = "000000000000000000000000e41d2489571d322189246dafa5ebde1f4699f498"

matched_transactions = getTransactionsByAccount(web3,myaccount=myaccount,token_address=zero_x_contract_address,startBlockNumber=start_block,endBlockNumber=end_block)
matched_transactions_txt = open("matched_transactions.txt","w+")
for t in matched_transactions:
    matched_transactions_txt.write("{}\n".format(t))
matched_transactions_txt.close()