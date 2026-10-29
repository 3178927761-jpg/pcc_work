"""
Day 1 ｜ for 循环：班级平均分
============================================================
任务
    让 average_score() 返回 4 位同学的平均分。

现在的输出
    平均分： 60.0

修好后的输出
    平均分： 85.0

规则
    不要改 main() 里的 scores，也不要改 print 文案。
    只修 average_score() 里的 bug。

今天练什么
    在 for 那一行打断点，用 F10 单步，观察每一轮的 i 和 total。
    WATCH 里加这三个：i、total、len(scores)。

提示（卡住再看，从 1 开始）
    1. 第一轮结束时 total 是多少？第二轮、第三轮呢？
    2. len(scores) 是几？range(len(scores) - 1) 实际会取到哪些 i？
    3. 循环结束后，total 里少了哪个分数？
"""


def average_score(scores):
    total = 0
    for i in range(len(scores) - 1):
        total += scores[i]
    return total / len(scores)


def main():
    scores = [80, 90, 70, 100]
    print("成绩：", scores)
    print("平均分：", average_score(scores))


if __name__ == "__main__":
    main()
