# Pending transactions script

This Python script is intended to retrieve from distant blockchain node information about pending transactions. It uses Web3.py library that is derived from original Web3.js library to interact with EVM network using Python programming language. When executed the script connects to the specified node, then gets the list of current pending transactions and prints transaction info.

# Setting up environment
Python programming language version 3.6 or higher should be installed in your system. Web3.py module also needs to be installed as well as other dependencies, listed in file **requirements.txt**. You can use `pip` utility to install all these dependencies from the file. But first of all it is strongly recommended to enable `virtualenv` cause in case of troubles with dependencies installation you may get broken working environment.

Clone this repository to your working directory. Then go to the directory, open the command line and run the following commands:

1. Install virtualenv if not yet installed

  `pip install virtualenv`

2. Create virtual environment

  `virtualenv -p python3 ~/.venv-py3`

3. Activate virtual environment

  `source ~/.venv-py3/bin/activate`
  
  When activated, your command prompt will look like this:
  
  `(.venv-py3) user@mycomputer:~/$`

> **Note!** Each new terminal session requires you to reactivate your virtualenv

4. Install necessary requirements

  `pip install -r requirements.txt`

# Running the script

Open the directory in your terminal and run the following command:

`(.venv-py3) user@mycomputer:~/mydir$ python3 web3test.py -n https://polygon-mainnet.provider.com/your-api-key -o pending_trans.txt`

> **Note!** The command prompt above starts with `(.venv-py3)` indicating that we are working in the virtual environment. This will be omitted for brevity in the following code snippets.

`web3test.py` script connects to the provider node, specified with `-n` key and writes the data to the file, specified with `-o` key.

<details><summary>Example:</summary>
<p>

Pending transactions

Transaction data
=================
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
* `-n <node>` - where <node> is the URL to remote provider node, that should be a node in the Polygon network
> Working with other providers was not tested, but supposedly the script should work with other EVM based networks
* `-t` - if set instead of `-n`, then default test Polygon node of [Alchemy.com](https://www.alchemy.com/layer2/polygon) network will be used
>Either `-n` or `-t` key must be provided 
* `-o` <filename> - where <filename> is the name of file to write data about pending transactions. If there is no such file, it will be created. If the key is omitted, the data will be sent to stdout

If some necessary keys are not specified in the command line, an error message will be displayed:
```
Usage: web3test.py -n|-t <node address> [-o <filename>]
```