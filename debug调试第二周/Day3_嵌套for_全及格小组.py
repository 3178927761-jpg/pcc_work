"""
Day 3 ｜ 嵌套 for + 标志位：第一个全及格小组
============================================================
任务
    每个小组是一个分数列表。
    返回第一个“全组都及格（>= 60）”的小组下标；没有就返回 -1。

现在的输出
    第一组： -1
    第二组： 0

修好后的输出
    第一组： 1
    第二组： 0

规则
    不要改 main() 里的两组数据，也不要改 print 文案。
    只修 first_all_pass()，只改一处（允许移动一行）。

今天练什么
    在外层 for 那一行打断点，WATCH 里加 r、c、all_pass。
    每跑完一行，先记下 all_pass 的值，再进入下一行。
    重点看：进入 r = 1 时，all_pass 是 True 还是 False？

提示（卡住再看，从 1 开始）
    1. 第一组数据里，第 0 行有 55，所以 all_pass 变成 False。
       进入第 1 行时，第 1 行其实全及格，all_pass 有没有恢复成 True？
    2. 第二组数据第 0 行全及格，为什么它反而能返回 0？
    3. all_pass 表示“当前这一行”的状态。它应该在外层循环里初始化，
       还是在外层循环开始前只初始化一次？
"""


def first_all_pass(groups, pass_line=60):
    all_pass = True
    for r in range(len(groups)):
        for c in range(len(groups[r])):
            if groups[r][c] < pass_line:
                all_pass = False
                break
        if all_pass:
            return r
    return -1


def main():
    first_group = [
        [55, 70, 80],
        [60, 65, 70],
        [90, 90, 90],
    ]
    second_group = [
        [70, 80],
        [50, 90],
    ]

    print("第一组：", first_all_pass(first_group))
    print("第二组：", first_all_pass(second_group))


if __name__ == "__main__":
    main()
