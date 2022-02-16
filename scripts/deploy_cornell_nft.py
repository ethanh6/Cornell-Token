from brownie import accounts, config, CornellNFT
from scripts.helper import get_account
from web3 import Web3


def main():
    a1, a2 = get_account(2)
    cnft = CornellNFT()
    