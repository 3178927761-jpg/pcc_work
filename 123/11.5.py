print("[1] 程序开始")

class Animal:
    print("[2] 定义 Animal 类")

    def __init__(self, name):
        print("[3] Animal.__init__")
        self.name = name

    def speak(self):
        print("[4] Animal.speak →", self.name)

class Dog(Animal):
    print("[5] 定义 Dog 类")

    def __init__(self, name):
        print("[6] Dog.__init__ 开始")
        super().__init__(name)      # 父类在这一行才执行
        print("[7] Dog.__init__ 结束")

    def speak(self):
        print("[8] Dog.speak →", self.name)
        super().speak()             # 父类方法在这一行才执行

print("[9] 创建一只狗")
d = Dog("旺财")

print("[10] 调用 speak()")
d.speak()

print("[11] 程序结束")