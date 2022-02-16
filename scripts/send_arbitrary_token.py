from brownie import accounts, config, Contract, CornellToken
from scripts.helper import get_account


def main():
    account = get_account()
    erc20_address = "0x6263718E85BeBA83517A4e9Ea1CAd623F61d93eb"
    # recipient = ""
    # This will be how many tokens to send in WEI
    amount = 1000000000000000000  # 1 token
    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=CornellToken.abi)
    print(erc20)
    # tx = erc20.transfer(recipient, amount, {"from": account})
    # tx.wait(1)