print("Dad!!")
print("Hello"+" world"+"!")
print("He sai ‘good!'")
print('He said "good!')
print("He sai \"Let\'s go!\"")               #"\"转义符
print("Hello!\n Hi!")                        #"\n"换行
print('''君不见，黄河之水天上来，奔流到海不复回。
君不见，高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。''')               #''' '''或""" """包裹文字，python会把新的一行当成内容换行

my_love="13333333333"
print("拨打："+my_love)

my_love="18888888888"
print("拨打："+my_love)
print("\n")

my_love="13333333333"
print("当前my_love的值："+my_love)
print("=====")
my_ex=my_love  #等号左边被视为变量名，等号右边的会先被求值
print("当前my_ex的值："+my_ex)
print("当前my_love的值："+my_love)
print("=====")
my_love="18888888888"
print("当前my_ex的值："+my_ex)
print("当前my_love的值"+my_love)
print("\n")

#变量命名只能由文字、数字、下划线组成，不能有除了下划线之外的符号，不能有空格，不能数字开头
#下划线命名法：字母全部小写，不同单词用下划线分隔，user_age
#驼峰命名法：单词用首字母大写分隔,UserAge

#字符串
print("python crash course".title()) #每个首字母大写

book_name="python crash course"
new_book_name=book_name.title()
print(new_book_name)
print(book_name)

print("python crash course".upper()) #字母全转化为大写
print("Python Crash Course".lower()) #字母全转化为小写

book_name=" python crash course  "
print(book_name.lstrip())  #移除开头的空格，用lstrip，表示left strip，从左边移除

book_name=" python crash course  "
print(book_name.rstrip())  #移除结尾的空格，用rstrip，表示right strip，从右边移除

book_name=" python crash course  "
print(book_name.strip()) #开头结尾都移除空格

book_name="python crash course"
print(book_name.removeprefix("python")) #removeprefix移除前缀，如果前缀在字符串里不存在，就会返回原始字符串

book_name="pythom crash course"
print(book_name.removesuffix("rse")) #removesuffix移除后缀，如果后缀在字符串里不存在，就会返回原始字符串
print("\n")

user_name="林粒粒"
date="3月1日"
city="深圳"
weather="晴"
message=user_name+"您好，今天是"+date+"，您所在的"+\
        city+"天气为"+weather+"。"
print(message)     #反斜杠表示当前行还未结束

username="Eric"
date="10月17日"
city="长沙"
weather="阵雨"
message=f"{username}您好，今天是{date}，您所在的{city}天气为{weather}" #加前缀f，花括号里的内容会先被求值添加到字符串内容里
print(message)

import math
#math函数库，
#import math
#math.函数名(...)
print(math.sin(1))
#**表示乘方

import math
result=math.log2(8)
print(result)

#表示注释
#选中一整段代码，用ctrl+/，一整段代码前都会被自动加上井号；撤销，继续选中这整段代码，再按一次ctrl+/即可

"""
三引号也表示注释
跨行无需再加引号
"""

#数据类型
len('Hello')  #字符串str长度，空格、数字、符号都会占据一个长度，注意：完整的转义符\n才占一个长度
"Hello"[3]    #方括号里放索引就能提取该索引位置的字符，程序是从0开始数
# 整数 int，浮点数 float
# 布尔类型 bool：真 True，假 False，首字母大写
# 空值类型 NoneType：None表示完全没有值
my_wife=None
# Type函数会返回你该对象的类型,例子：Type("Hello")---<class'str'>；Type(6)---<class'int'>

# 列表(可变的)
shopping_list=["键盘","键帽"]
shopping_list.append("显示器")  #往定义好的列表里添加东西
# 方法：对象.方法名(...)  函数：函数名(对象)
print(shopping_list)

shopping_list=["键盘","显示器"]
shopping_list.remove("显示器")
print(shopping_list)

list1=["Hello"]
list1.append(66.6)
list1.append(True)
list1.append(None)
print(list1)

shopping_list=["键盘","显示器","硬盘"]
len(shopping_list)
print(len(shopping_list))

shopping_list=["键盘","显示器","硬盘"]
print(shopping_list[0])

shopping_list=["键盘","显示器","硬盘"]
shopping_list[1]="音响"  #索引为1的元素被更改
print(shopping_list)

num_list=[1,13,-7,2,96]
print(max(num_list))  # 打印列表里的最大值
print(min(num_list))  # 打印列表里的最小值
print(sorted(num_list))  #打印排序好的列表

#遍历整个列表
# for 变量名 in 可迭代对象：
temperature_list=[36.4,36.6,36.2,37.0,36.8,37.4,38.1,35.9,36.5,38.3]
for temperature in temperature_list:
        if temperature>=38:
                print(temperature)
                print("完球了")

#range：表示整数数列  range(5,10)，5是起始值，10是结束值，注意结束值不在序列范围内
#range(5,10,2)，2表示步长
#range(n):从0开始到n-1结束
for i in range(5,10):
        print(i)
for num in range(1,10,2):
        print(num)

total=0    #定义一个变量，用来储存之后1+2+3一直加到100的结果
for i in range(1,101):
        total=total+i
print(total)

""" 
if [条件]：
   [执行语句]
   [执行语句]
else：
   [执行语句]
   [执行语句]
注：==：比较运算符  ！=：不等于号
if [条件一]：
   if [条件二]：
      [语句A]
   else:
      [语句B]
else:
   [语句C]
"""
"""
if [条件一]：
   [语句A]
elif [条件二]：
     [语句B]
多个语句判断"""

""" and:只要有一个或以上是False,就返回False
# or：只要有一个或以上是True，就返回True
# not：只能用于对一个操作对象进行运算
# not--and--or（优先级，遇到括号优先括号）
"""

# 字典：键(key):值(value) 键的类型是不可变的，所以列表不能作为键
# 元组tuple=(...,...,...) 不可变，所以不能进行添加删除操作 元组可以作为字典的键 字典和列表一样，都是可变的，可以添加和移除
# del 字典名[],把键和对应的值从字典里删除



# input函数：input("这里是给用户的一些提示")，用变量去获取input函数返回的值，input一律返回字符串

user_age=int(input("请输入您的年龄："))
user_age_after_10_years=user_age+10
print("您十年后会是"+str(user_age_after_10_years)+"岁")

"""
while 条件A:
    行动B
循环次数未知"""

# def:定义函数
# return 返回对象

"""面向对象编程
类(class)和对象的关系：类是创建对象的模板，对象是类的实例
可以把类想象成制造具体对象的图纸
面向对象的特性：封装(表示写类的人将内部实现细节隐藏起来，使用类的人只通过外部接口访问和使用，接口可以被大致理解为提供使用的方法)、
继承(面向对象编程允许创建有层次的类，类可以有子类和父类，来表示从属关系)、多态(同样的接口，因为对象具体类的不同而有不同表现)"""




