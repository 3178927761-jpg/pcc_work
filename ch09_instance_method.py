class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 方法
    def bark(self):
        print("self:::",self)
        print(f"{self.name}正在狂吠")

    def bite(self,person):
        print(f"{self.name}咬{person}")

    def fetch(self):
        print(f"{self.name}捡球")

alex = Dog()
peiQi = Dog()


#(2)
alex.name = "李杰"
alex.age = 10
alex.bark()
alex.bite('yuan')
alex.fetch()


