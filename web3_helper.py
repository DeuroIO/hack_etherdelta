def getTransactionsByAccount(web3, myaccount, token_address,startBlockNumber=None, endBlockNumber=None):
    if endBlockNumber is None:
        endBlockNumber = web3.eth.blockNumber
        print("Using endBlockNumber: " + endBlockNumber)
    if startBlockNumber is None:
        startBlockNumber = endBlockNumber - 100
        print("Using startBlockNumber: " + startBlockNumber)
    print("Searching for transactions to/from account \"" + myaccount + "\" within blocks "  + str(startBlockNumber) + " and " + str(endBlockNumber))
    matched_transactions = []
    for i in range(startBlockNumber,endBlockNumber+1):
        block = web3.eth.getBlock(i,True)
        if block is not None and block.transactions is not None:
            transactions = block["transactions"]
            for transaction in transactions:
                if transaction["from"] == myaccount or transaction["to"] == myaccount:
                    if token_address in transaction["input"]:
                        matched_transactions.append(transaction)
    return matched_transactions