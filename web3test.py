#import necessary classes from Web3 library
from web3 import Web3, HTTPProvider
#import of middleware to solve issue with extraData size when working with POA chain 
from web3.middleware import geth_poa_middleware

#import time

#establishing HTTP connection to polygon chain node
w3 = Web3(HTTPProvider('https://polygon-mainnet.g.alchemy.com/v2/e4b0Vb2-0nI4twIPq_IBq3MiPMM3pqq_'))
#using middleware to work with POA extraData blocks 97 bytes long instaed of usuall 32 bytes block
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#filter to retrieve only transactions with status pending 
filt = w3.eth.filter('pending')

# while True:
#     for event in filt.get_new_entries():
#         #print(event)
#         print(w3.eth.get_filter_changes(filt.filter_id))
#     time.sleep(1)

#print transaction info for every item in retrieved transactions 
for item in w3.eth.get_filter_changes(filt.filter_id):
	for transaction in w3.eth.get_transaction(item).items():
		print (transaction)