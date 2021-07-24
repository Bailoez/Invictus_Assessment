import cbpro
import constants

BUY = 'buy'
SELL = 'sell'


class TradingSystems:

    def __init__(self, cb_pro_client):
        self.client = cb_pro_client

    def trade(self, action, LimitPrice, quantity):
        if action == BUY:
            response = self.client.buy(
                price=LimitPrice,
                size=round(quantity, 8),
                order_type='limit',
                product_id='BTC-USD',
                overdraft_enables=False
            )
        elif action == SELL:
            response = self.client.sell(
                price=LimitPrice,
                size=quantity,
                order_type='limit',
                product_id='BTC-USD',
                overdraft_enables=False
            )
        print(response)

    def viewAccounts(self, accountCurrency):
        accounts = self.client.get_accounts()
        account = list(filter(lambda x: x['currency'] == accountCurrency, accounts))[0]
        return account

    def viewOrder(self, order_id):
        return self.client.get_order(order_id)

    def getCurrentPriceOfBitcoin(self):
        tick = self.client.get_product_ticker(product_id='BTC-USD')
        return tick['bid']


if __name__ == "__main__":
    auth_client = cbpro.AuthenticatedClient(constants.cbpro_pubkey,
                                            constants.cbpro_secret,
                                            constants.cbpro_passphrase,
                                            api_url="https://api-public.sandbox.pro.coinbase.com")

    tradingSystems = TradingSystems(auth_client)
    current_price = tradingSystems.getCurrentPriceOfBitcoin()
    usdBalance = tradingSystems.viewAccounts('USD')['balance']
    tradingSystems.trade(BUY, float(current_price), float(usdBalance) / float(current_price)) #used for placing trades
    #lastOrderInfo = tradingSystems.viewOrder('64da4196-40dd-41fd-9daa-79b33c07d6b7')
    print(current_price)
    print(usdBalance)
    #print(lastOrderInfo)

