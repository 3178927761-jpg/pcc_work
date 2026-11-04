class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def spend(self, amount):
        self.balance -= amount
        return self.balance >= 0


def buy_items(wallet, prices):
    bought = []
    skipped = 0
    i = 0
    while i < len(prices):
        price = prices[i]
        if wallet.spend(price):
            bought.append(price)
        else:
            skipped += 1
        i += 1
    return bought, skipped


def main():
    wallet = Wallet(100)
    bought, skipped = buy_items(wallet, [30, 50, 40, 10])
    print("买到：", bought)
    print("余额：", wallet.balance)
    print("跳过：", skipped)


if __name__ == "__main__":
    main()
