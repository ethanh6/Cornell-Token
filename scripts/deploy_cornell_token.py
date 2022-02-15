from binascii import a2b_base64
from brownie import accounts, config, CornellToken
from scripts.helper import get_account
from web3 import Web3


initial_supply = Web3.toWei("1000", "ether")  # 1000 ether
token_name = "CornellToken"
token_symbol = "CT"



def main():
    account1, account2 = get_account(2)
    print(account1)
    CT = CornellToken.deploy(initial_supply, {"from": account1})

    
    # get token basic definitions
    print("Token Name = {}".format(CT.name()))
    print("Token Symbol = {}".format(CT.symbol()))
    print("Token Decimals = {}".format(CT.decimals()))
    print("Token Total Supply = {}".format(CT.totalSupply()))

    # get balance
    def print_balance(acct):
        print("Balance of account: {} = {} ETH".format(acct, Web3.fromWei(CT.balanceOf(acct), "ether")))
    print_balance(account1)
    print_balance(account2)

    # transfer
    CT.transfer(account2, Web3.toWei("300", "ether"))
    print_balance(account1)
    print_balance(account2)

    # allowance and approve
    print(CT.allowance(account1, account1))
    CT.approve(account2, 100)
    print(CT.allowance(account1, account2))

    if CT.transferFrom(account2, account1, 50):
        print_balance(account1)
        print_balance(account2)