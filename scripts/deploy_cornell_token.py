from brownie import accounts, config, CornellToken
from scripts.helper import get_account


initial_supply = 10**21  # 1000 ether
token_name = "CornellToken"
token_symbol = "CT"


def main():
    account = get_account()
    print(account)
    CT = CornellToken.deploy(initial_supply, {"from": account})
    print("*** Token Name ===> {} <=== ***".format(CT.name()))
