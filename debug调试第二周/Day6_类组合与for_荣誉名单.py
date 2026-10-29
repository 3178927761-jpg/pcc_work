"""
Day 6 ｜ 类组合 + for + return：荣誉名单
============================================================
任务
    Course 里保存若干 Student 对象。
    返回所有分数 >= 90 的学生姓名，顺序与列表一致。

现在的输出
    荣誉名单： ['小明']

修好后的输出
    荣誉名单： ['小明', '小刚']

规则
    不要改 main() 里的学生和分数，也不要改 print 文案。
    只修 Course.honor_names()，只改一处。

今天练什么（重点：一层层进入方法）
    1. 在 main() 的 course.honor_names() 这一行打断点；
    2. F5 启动，停住后按 F11，进入 Course.honor_names()；
    3. 按 F10 走到 if student.is_honor(line): 这一行；
    4. 再按 F11，进入 Student.is_honor()；
    5. WATCH 里加 student.name、student.score、names；
    6. 看小红（88 分）那一轮：is_honor 返回 False 后，程序去了哪里？
    7. CALL STACK 里应该能看到 main -> Course.honor_names -> Student.is_honor。

提示（卡住再看，从 1 开始）
    1. 小红不是荣誉学生，程序执行 else 里的 return names。
       这时 names 里有什么？循环还能继续到小刚吗？
    2. 小刚 92 分，本来应该进入名单，为什么完全没有被检查？
    3. 如果只是想“跳过这个学生，继续看下一个”，应该用 return 还是 continue？
       return 结束的是整个方法，还是这一轮循环？
"""


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_honor(self, line=90):
        return self.score >= line


class Course:
    def __init__(self, students):
        self.students = students

    def honor_names(self, line=90):
        names = []
        for student in self.students:
            if student.is_honor(line):
                names.append(student.name)
            else:
                return names
        return names


def main():
    students = [
        Student("小明", 95),
        Student("小红", 88),
        Student("小刚", 92),
        Student("小美", 85),
    ]
    course = Course(students)
    print("荣誉名单：", course.honor_names())


if __name__ == "__main__":
    main()
