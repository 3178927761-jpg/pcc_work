# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 方法
    def bark(self):
        print("狗狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")

# 创建类的对象的过程：类的实例化：new 类()

alex = Dog()
peiQi = Dog()

# (1) alex和peiQi的内存地址一样吗？ --不一样
print(id(alex))
print(id(peiQi))
print(alex==peiQi)
# (2)实例对象通过句点符号调用类的属性和方法
print(alex.legs_num)
print(alex.has_hair)
alex.bark()
# (3) 调用类属性一定是同一空间值
print((id(alex.legs_num)))
print((id(peiQi.legs_num)))
print((id(alex.bark)))
print(id(peiQi.bite))

# 实例属性赋值：实例对象.属性 = 值   向实例空间写入或修改属性和值
alex.name = "李杰"
alex.age = 10
print(alex.name)
peiQi.name = "武大郎"
peiQi.age = 8
print(peiQi.name)

# (1)
alex.age = 30
print(alex.age)
print(peiQi.age)

# (2)实例对象.变量  查询顺序 [实例空间，类空间，父类空间]
# alex.bark()
alex.bark = 1000
peiQi.bark()

alex.legs_num = 5
print(alex.legs_num)


# (1) self每次都代表调用的对象
"""print("alex:::",alex)
alex.bark()
peiQi.bark()

alex.bite("yuan")
alex.bite("huang")"""