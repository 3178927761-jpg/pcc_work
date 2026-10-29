"""
Day 5 ｜ 类 + 方法 + while：账户手续费
============================================================
任务
    账户初始 100 元，每成功取款一次收 2 元手续费。
    按顺序尝试取 [50, 48, 100]：
      - 只有“取款金额 + 手续费 <= 余额”才成功；
      - 成功：扣掉金额和手续费，记入受理列表；
      - 失败：余额和手续费都不能变。

现在的输出
    受理： [50, 48]
    余额： -2
    手续费： 4

修好后的输出
    受理： [50]
    余额： 48
    手续费： 2

规则
    不要改 main() 里的 100、2 和金额列表，也不要改 print 文案。
    不要改 process() 里的 while 结构；bug 在 withdraw() 的余额判断里。

今天练什么（重点：连续 F11 进入两层方法）
    1. 在 main() 的 accepted = account.process([50, 48, 100]) 这一行打断点；
    2. F5 启动，停住后按 F11，进入 process()；
    3. 在 process() 里按 F10，走到 if self.withdraw(amounts[i]): 这一行；
    4. 再按 F11，进入 withdraw()；
    5. WATCH 里加 amount、self.fee、self.balance；
    6. 重点看第二次取 48 元：余额只有 48，金额 48 真的够吗？加上手续费呢？
    7. CALL STACK 里应该能看到 main -> process -> withdraw。

提示（卡住再看，从 1 开始）
    1. 第二次取 48 元时，amount > self.balance 是 False，所以程序认为这笔取款能成功。
       但实际要扣掉的总数是多少？
    2. 条件只比较了 amount 和 balance，漏掉了哪个变量？
    3. 第二次取 48 元本来应该失败；现在余额和手续费有没有被改？
"""


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
