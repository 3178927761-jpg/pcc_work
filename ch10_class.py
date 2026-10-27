class Cutecate:
    def __init__(self,cate_name,cate_age,cate_color):   # 通过__init__这个构造方法可以定义对象拥有哪些属性
        self.name = cate_name
        self.age =cate_age
        self.color = cate_color

    def speak(self):
        print("喵"*self.age)  # 实现方法调用结果，根据属性的不同而改变

    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

cat1 = Cutecate("Jojo",2,"橙色")
# 通过class名字后面加括号可以调用__init__来创建对象，并且把对应属性进行赋值
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
cat1.speak() #调用类方法，用对象.方法名，括号里放上参数进行调用
# 和构造方法一样，不需要手动将self传入，方法自然可以接收更多参数
cat1.think("现在去抓沙发还是去撕纸箱")



class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐厅名：{self.restaurant_name}")
        print(f"菜系:{self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅开始营业")
taotaoju = Restaurant("陶陶居","粤菜")
print(taotaoju.restaurant_name)
print(taotaoju.cuisine_type)
taotaoju.describe_restaurant()
taotaoju.open_restaurant()






class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"餐厅名：{self.restaurant_name}")
        print(f"菜系:{self.cuisine_type}")
    def open_restaurant(self):
        print("餐厅开始营业")
    def set_number_served(self,number_served):
        self.number_served = number_served
    def increament_number_served(self,increament_number):
        self.number_served += increament_number
taotaoju = Restaurant("陶陶居","粤菜")
print(taotaoju.restaurant_name)
print(taotaoju.cuisine_type)
print(taotaoju.number_served)
taotaoju.describe_restaurant()
taotaoju.open_restaurant()
taotaoju.set_number_served(500)
taotaoju.increament_number_served(20)
print(taotaoju.number_served)




