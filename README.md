# Pending transactions script

This Python script retrieves information about pending transactions from a distant blockchain node. It uses *Web3.py* library to interact with EVM network using Python programming language. The script connects to the specified node, then gets the list of current pending transactions and prints transaction info.

# Setting up environment
Python programming language version 3.6 or higher should be installed in your system. *Web3.py* module also needs to be installed as well as other dependencies, listed in file **requirements.txt**. Specify this file as an argument for [pip](https://pip.pypa.io/en/stable/installation/) utility to install all necessary dependencies (see example below). But first of all it is strongly recommended to enable *virtualenv* to avoid broken working environment if something goes wrong with dependency installation.

To set up your environment, clone this repository to your working directory. Then go to the directory, open the command line and run the following commands:

1. Install *virtualenv* if not yet installed

  `pip install virtualenv`

2. Create virtual environment

  `virtualenv -p python3 ~/.venv`

3. Activate virtual environment

  `source ~/.venv/bin/activate`
  
  When activated, your command prompt will look like this:
  
  `(.venv) user@mycomputer:~/$`

> **Note!** Each new terminal session requires to reactivate virtualenv again

4. Install necessary requirements

  `pip install -r requirements.txt`

# Running the script
Once the virtualenv is activated and all requierements are installed, open the directory in your terminal and run the following command:

`(.venv) user@mycomputer:~/mydir$ python web3test.py -n https://polygon-mainnet.provider.com/your-api-key -o pending_trans.txt`

> **Note!** The command prompt above starts with `(.venv)` indicating that we are working in the virtual environment. This will be omitted for brevity in the following code snippets

`web3test.py` script connects to provider node, specified with `-n` key. For authentication purposes you should enter your API-KEY as a part of URL. You get your API-KEY, when you register at your blockchain network provider. If you don't yet have an API-KEY, you can try for testing purposes a default node. Use `-t` instead of `-n` in that case. For details see [Keys and arguments](https://github.com/madydady/web3test/blob/main/README.md#keys-and-arguments). Data is writen into the file, specified with the `-o` key. Or if no file is specified, pending transaction data will be displayed in your terminal window (or your stdout).

<details><summary>Example of pending transaction data:</summary>
<p>
Pending transactions

Transaction data

blockHash:None

blockNumber:None

from:0x0993e8c8a88Ad6f588B9BA44786ECe841daf0A14

gas:294742

gasPrice:34000000000

maxFeePerGas:34000000000

maxPriorityFeePerGas:32000000000

hash:b'.a\xdf@\xe0"\x1a\xb7\x96+:`\xb5\x96\xb4\x9e\xa1\x97\xba\x8e\'\xf1kE\\\xbf\x15\xc2a\xc2U3'

input:0x674c3d0b00000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000010000000000000000000000000006a424b0826fb195b9ed24aea37eaac65655624f0000000000000000000000000000000000000000000000000000000001e133800000000000000000000000003c2daab0af88b0c5505ccb585e04fb33d7c8014400000000000000000000000006a424b0826fb195b9ed24aea37eaac65655624f000000000000000000000000000000000000000000000000000000000000000b6a756c69616e6e6575737300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000046d65746100000000000000000000000000000000000000000000000000000000

nonce:7322

to:0x8C856f71d71e8CF4AD9A44cDC426b09e315c6A6a

transactionIndex:None

value:0

type:0x2

accessList:[]

chainId:0x89

v:0

r:b":d\xaf\xbc\x0b\x1a\xa1\xc2'\xb8%\xd6\xe7\xec\xf2\x12\xda(1'\xaa\x81#X\x13mkMUC\\\x9e"

s:b'tn\xc5.p\x00 \xbc\x84\xd9\xea\xd2@\xd4JH\xa7h\x1a*\xff\x13\x1eBX4\x85%\x81\x82\xe1\xae'
</p>
</details>

## Keys and arguments
The script can be run with the following keys:
* `-n <node>` - where *node* is an URL to the remote provider node. The script was tested for nodes in the Polygon network. Working with other providers was not tested, but supposedly it will also work with other EVM based networks;
* `-t` - if set instead of `-n`, then the default test Polygon node of [Alchemy.com](https://www.alchemy.com/layer2/polygon) network will be used;
>Either `-n` or `-t` key must be provided to run the script 
* `-o <file>` - where *file* is the name of the file to write data about pending transactions. If there is no such file, it will be created. This is an optional key - if omitted, the data will be sent to your stdout.

If some necessary keys are not specified in the command line, an error message will be displayed:
```
Usage: web3test.py -n|-t <node address> [-o <filename>]
```

# How it works
The script reads keys and arguments given in the command line and connects either to the specified remote provider node, or the default Polygon node, hosted at *polygon-mainnet.g.alchemy.com*.

## Establishing connection to Polygon chain node
Instance of a `Web3` class derived from the Web3 library is created. This Web3 object connects to provider node using `HTTPProvider`. Special middleware layer between provider and other Web3 methods is used to handle native communication with Ethereum client. The layer can modify the request and/or response between provider and Etherium cloud. This is used to avoid error, which occures when working with POA nodes with block size of 97 bytes instead of usual 32 bytes.

```
#establishing HTTP connection to Polygon chain node
w3 = Web3(HTTPProvider(node))
#using middleware to work with POA extraData blocks 97 bytes long instaed of usuall 32 bytes block
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
```

## Using filter to derive data about pending transactions
The script uses `web3.eth.filter()` method with `pending` argument to get unmined (pending) transactions that the node receives. And `w3.eth.get_filter_changes()` method to get each new pending transaction. `w3.eth.get_filter_changes()` method returns a list of dictionary objects, where each dictionary contains key-value pairs with transaction data. `w3.eth.get_transaction()` method is used to handle these dictionary objects. Each key-value pair for transaction is either printed to file (if the file path is specified), or displayed in the terminal.

```
if path:
	with open(path, 'a') as f:
		f.write("Pending transactions\n")
		for item in w3.eth.get_filter_changes(filt.filter_id):
			f.write('\nTransaction data\n=================\n')
			for k, v in w3.eth.get_transaction(item).items():
				line = (str(k) + ":" + str(v) + "\n")
				f.write(line)
	f.close()
```

Path to the file where data will be written depends on the `-o` key given in the command line arguments.

```
if "-o" in opts:
	i = opts.index("-o") - 1
	path = [os.getcwd(), args[i]]
	path = '/'.join(path)
else:
	path = None
```
