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