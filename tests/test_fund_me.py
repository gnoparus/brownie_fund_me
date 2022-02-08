from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_account()
    deploy_fund_me()
    fund_me = FundMe[0]
