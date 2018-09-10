'''
some custom exceptions.
'''

class BinanceAccountError(Exception):

    def __init__(self, expression, message):
        self.code = -7000

class ZeroDepositError(BinanceAccountError):
    def __init__(self):
        self.message = "Your Binance account balance is zero, cannot trade"
        self.code = -7001

class BalanceBelowMinimum(BinanceAccountError):
    def __init__(self):
        self.message = "The account balance is below the minimum allowable amount to trade"
        self.code = -7002

class PermissionsError(BinanceAccountError):
    def __init__(self):
        self.message = "The provided API Key and API Secret do not have sufficient permission to trade"
        self.code = -7003