class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self,name,breed,color,age):
        print("__init__执行")
        print("self:::",id(self))
        self.name = name
        self.breed = breed
        self.color = color
        self.age =age

    # 方法
    def bark(self):
        print("self:::",self)
        print(f"{self.name}正在狂吠")

    def bite(self,person):
        print(f"{self.name}咬{person}")

    def fetch(self):
        print(f"{self.name}捡球")

    def show_info(self):
        print(f"名字：{self.name},品种：{self.breed},颜色：{self.color},年龄：{self.age}")

# (1)
# alex.init_prop(name="李杰",breed="斗牛犬",color="黄色",age=5)
#
# alex.bark()
# alex.show_info()
# (2)
# 类实例化步骤
# 1.开辟空间
# 2.调用__init__(实例空间地址)
# 3.将实例空间地址作为类的实例子化的返回值
alex = Dog(name="李杰",breed="斗牛犬",color="黄色",age=5)
print("alex:::",id(alex))
alex.show_info()