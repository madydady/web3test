# Pending transactions script

This Python script is intended to retrieve from distant blockchain node information about pending transactions. It uses Web3.py library that is derived from original Web3.js library to interact with EVM network using Python programming language. When executed the script connects to the specified node, then gets the list of current pending transactions and prints transaction info.

# Setting up environment
This is a Python script so Python programming language version 3.6 or higher should be installed in your system. Web3.py module also needs to be installed. Web3 library uses some dependencies for proper work. These dependencies are listed in *requirements.txt* file. You can use `pip` utility to install all these dependencies from the file. But first of all it is strongly recommended to enable `virtualenv` cause in case of troubles with dependencies installation you may get broken working environment.

Open the command line and run:

1. Install virtualenv if not yet installed

  `pip install virtualenv`

2. Create virtual environment

  `virtualenv -p python3 ~/.venv-py3`

3. Activate virtual environment

  `source ~/.venv-py3/bin/activate`
  
  When activated your command promt will look like this:
  
  `(.venv-py3) user@mycomputer:~/$`

> **Note!** Each new terminal session requires you to reactivate your virtualenv

4. Install necessary requirements

  `pip install -r requirements.txt`

# Running the script


