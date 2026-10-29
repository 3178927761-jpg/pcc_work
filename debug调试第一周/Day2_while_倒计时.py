"""
Day 2 ｜ while 循环：倒计时
============================================================
任务
    让 countdown(5) 从 5 开始倒数，返回 [5, 4, 3, 2, 1]。

现在的输出
    倒计时： [4, 3, 2, 1, 0]

修好后的输出
    倒计时： [5, 4, 3, 2, 1]

规则
    不要改 main() 里的 5，也不要改 print 文案。
    只修 countdown() 里的 bug。

今天练什么
    在 while 那一行打断点，每按一次 F10，就在纸上记一次：
    进入循环时 n 是多少，result 里有什么。

提示（卡住再看，从 1 开始）
    1. 第一次进入 while 时，n 是 5 还是 4？
    2. 循环条件检查发生在“进入循环之前”，你的两行代码谁先谁后？
    3. result 的第一个数现在是 4，它应该是几？少掉的这个数去哪了？
"""


def countdown(start):
    result = []
    n = start
    while n > 0:
        n -= 1
        result.append(n)
    return result


def main():
    print("倒计时：", countdown(5))


if __name__ == "__main__":
    main()
