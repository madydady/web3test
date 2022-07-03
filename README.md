# Getting pending transactions

This Python script is intended to retrieve from distant blockchain node information about pending transactions. It uses Web3.py library that is derived from original Web3.js library to interact with Etherium using Python programming language. When executed the script connects to the node, then gets the list of current pending transactions and prints transactions info.

# Setting up environment
This is a Python script so Python programming language version 3.6 or higher should be installed in your system. Web3.py module also needs to be installed. Web3 library uses some dependencies for proper work.  

These dependencies are listed in *requirements.txt* file. You can use pip utility to install all these dependencies from the file. Open the command line and run:

pip install -r requirements.txt

