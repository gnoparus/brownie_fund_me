from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mocks, get_account
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    if (
        network.show_active() != "development"
        and network.show_active() != "ganache-local"
    ):
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1]

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # fund_me = FundMe.deploy({"from": account})
    print(f"contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
