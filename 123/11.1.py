class BankAccount:
    def __init__(self, balance, fee=2):
        self.balance = balance
        self.fee = fee
        self.fees_paid = 0

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount + self.fee
        self.fees_paid += self.fee
        return True

    def process(self, amounts):
        accepted = []
        i = 0
        while i < len(amounts):
            if self.withdraw(amounts[i]):
                accepted.append(amounts[i])
            i += 1
        return accepted


def main():
    account = BankAccount(100)
    accepted = account.process([50, 48, 100])
    print("受理：", accepted)
    print("余额：", account.balance)
    print("手续费：", account.fees_paid)


if __name__ == "__main__":
    main()