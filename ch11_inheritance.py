# 类可以有子类和父类，表示丛属关系。子类会继承父类的属性和方法
class Mammal:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breathe(self):
        print(self.name + "在呼吸...")

    def poop(self):
        print(self.name + "在拉屎...")

class Human(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)

    def read(self):
        print(self.name + "在阅读...")

class Cat(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)
# super()会返回当前类的父类，所以在子类的__init__方法里写super().__init__就会调用父类的构造函数，子类也就会有姓名、性别、眼睛数的属性了
    def scratch(self):
        print(self.name + "在抓沙发")

cat1 = Cat("Jojo","男") #由于子类没有自己的构造函数，就会调用父类的构造函数，让实例具备名字、性别、眼睛数等属性
print(cat1.name)
cat1.poop() #调用方法时，用的也会是父类的方法，如果子类有自己的poop方法的话，就会调用自己的
# 逻辑：优先看所属的类有没有该方法，没有的话，找父类的同名方法
# 通过继承成功将重复的属性和方法行移除了，并且在实例化、获得属性、调用方法时和之前一样
# 什么时候用继承：A是B ———— class A(B)




class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐厅名：{self.restaurant_name}")
        print(f"菜系:{self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅开始营业")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,flavors):
        super().__init__(restaurant_name,"甜品")
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)

so_sweet = IceCreamStand("So Sweet",["香蕉","草莓","哈密瓜","开心果"])
so_sweet.describe_restaurant()
so_sweet.show_flavors()
