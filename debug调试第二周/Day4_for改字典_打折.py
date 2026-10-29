"""
Day 4 ｜ for 遍历字典并修改值：打折
============================================================
任务
    把价格 >= 100 的商品打 8 折（乘 0.8），其他商品不变。
    返回修改后的 prices。

现在的输出
    打折后： {'apple': 5, 'headphones': 120, 'keyboard': 200, 'cable': 30}

修好后的输出
    打折后： {'apple': 5, 'headphones': 96.0, 'keyboard': 160.0, 'cable': 30}

规则
    不要改 main() 里的价格，也不要改 print 文案。
    只修 discount_prices()，只改一处。

今天练什么
    在 if price >= 100 那一行打断点，WATCH 里加 name、price、prices。
    当循环走到 headphones 时，按 F10 执行完 price = price * 0.8，然后分别看：
      - price 现在是多少？
      - prices["headphones"] 现在是多少？
    它们还是同一个值吗？

提示（卡住再看，从 1 开始）
    1. headphones 的 price 确实变成了 96.0，但字典里的值变了吗？
    2. for name, price in prices.items() 每次解包出来的 price，
       是一个“指向字典内部的引用”，还是一个普通的局部变量？
    3. 给 price 赋值，改的是局部变量；要改字典，应该给 prices[?] 赋值？
"""


def discount_prices(prices):
    for name, price in prices.items():
        if price >= 100:
            price = price * 0.8
    return prices


def main():
    prices = {
        "apple": 5,
        "headphones": 120,
        "keyboard": 200,
        "cable": 30,
    }
    print("打折后：", discount_prices(prices))


if __name__ == "__main__":
    main()
