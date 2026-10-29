"""
Day 6 ｜ 类 + for + return：成绩单
============================================================
任务
    统计 ScoreBoard 里及格（>= 60）的人数。

现在的输出
    及格人数： 1

修好后的输出
    及格人数： 3

规则
    不要改 main() 里的分数，也不要改 print 文案。
    只修 count_pass() 里的 bug。

今天练什么（重点：看清 return 到底结束了谁）
    1. 在 for 那一行打断点，F5 启动；
    2. 按 F11 进入 count_pass()，WATCH 里加 score、count、self.scores；
    3. 每轮记录 score 和 count；注意程序在第几个分数之后就离开了方法；
    4. 看 CALL STACK：return 之后，是回到 for 的下一轮，还是直接回到 main？

提示（卡住再看，从 1 开始）
    1. 第一次执行 return count 时，score 是几？count 是几？
    2. 列表里还有 55、90、80 没被检查，为什么循环不继续了？
    3. return 执行一次，结束的是“这一轮循环”还是“整个方法”？
"""


class ScoreBoard:
    def __init__(self, scores):
        self.scores = scores

    def count_pass(self, line=60):
        count = 0
        for score in self.scores:
            if score >= line:
                count += 1
            return count


def main():
    board = ScoreBoard([75, 55, 90, 80])
    print("及格人数：", board.count_pass())


if __name__ == "__main__":
    main()
