"""
Day 5 ｜ 类 + 方法 + while：零花钱购物
============================================================
任务
    钱包初始 100 元，按顺序尝试买 [30, 50, 40, 10]。
    规则：
      - 买得起：扣钱，记录到 bought；
      - 买不起：跳过，不扣钱，skipped 加 1。

现在的输出
    买到： [30, 50]
    余额： -30
    跳过： 2

修好后的输出
    买到： [30, 50, 10]
    余额： 10
    跳过： 1

规则
    不要改 main() 里的 100 和价格表，也不要改 print 文案。
    不要改 buy_items() 里的 while 结构；bug 在 Wallet 类里。

今天练什么（重点：F11 单步进入方法）
    1. 在 buy_items() 的 if wallet.spend(price): 这一行打断点；
    2. F5 启动，停在断点后按 F11，进入 spend() 方法内部；
    3. WATCH 里加 self.balance、amount；
    4. 重点看第三次：想买 40 元时，钱包里只有 20 元，进入方法后余额变成了多少？
    5. 左侧 CALL STACK 里应该能看到 buy_items 调用了 spend。

提示（卡住再看，从 1 开始）
    1. 买 40 元那次，spend() 返回 True 还是 False？
    2. 返回 False 之前，self.balance 已经被改成了多少？
    3. 如果 40 元没买成、余额仍然是 20，最后的 10 元还能买吗？
       现在为什么没买到它？
"""


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
