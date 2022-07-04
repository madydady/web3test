# standard python libraries used
import sys
import os

#import necessary classes from Web3 library
from web3 import Web3, HTTPProvider

#import of middleware to handle extraData size when working with POA chain 
from web3.middleware import geth_poa_middleware

# options and arguments the script is run with, where argv[0] is the script selfname
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# if script is run with -n key, the node to connect to is taken from script arguments
# if script is run with -t key, the default test node is used
# if script is run with -o key, the data is written into specified file, otherwise will be directed to stdout 
# if no key provided, the script exits with the error message
if "-n" in opts:
	node = args[0]
elif "-t" in opts:
	node = "https://polygon-mainnet.g.alchemy.com/v2/e4b0Vb2-0nI4twIPq_IBq3MiPMM3pqq_"
else:
	raise SystemExit(f"Usage: {sys.argv[0]} -n|-t <node address> [-o <filename>]")


#establishing HTTP connection to polygon chain node
w3 = Web3(HTTPProvider(node))
#using middleware to work with POA extraData blocks 97 bytes long instaed of usuall 32 bytes block
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#filter to retrieve only transactions with status pending 
filt = w3.eth.filter('pending')

# print transaction info into file if -o key provided, else direct data to stdout
if "-o" in opts:
	i = opts.index("-o") - 1
	path = [os.getcwd(), args[i]]
	path = '/'.join(path)
else:
	path = None

if path:
	with open(path, 'a') as f:
		f.write("Pending transactions\n")
		for item in w3.eth.get_filter_changes(filt.filter_id):
			f.write('\nTransaction data\n=================\n')
			for k, v in w3.eth.get_transaction(item).items():
				line = (str(k) + ":" + str(v) + "\n")
				f.write(line)
	f.close()
else: 
	print("Pending transactions")
	for item in w3.eth.get_filter_changes(filt.filter_id):
		print('\nTransaction data\n=================')
		for k, v in w3.eth.get_transaction(item).items():
			print (k, ":", v)
