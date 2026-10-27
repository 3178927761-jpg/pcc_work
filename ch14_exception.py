# 异常类型
# number_list = [56,23,-5,96]
# number_list[4]  用长度范围之外的索引对列表取值 → IndexError 索引错误

# print(56/(12-15+3)) 用数字除以0 → ZeroDivisionError 除零错误

# f = open("./hi.txt","r")  打开的文件不存在 → FileExistsError 找不到文件错误

# "yoo" * "hi"  两个字符串做乘法 → TypeError 类型错误





# 捕捉异常：通过try/except语句去捕捉异常
# try：换行后缩进的代码块里放上觉得可能会产生报错的代码
# except后跟上想捕捉的错误名字：换行后缩进的代码块里面放上那类错误发生后你想相应执行的操作
# except：这个语句会捕捉所有的错误类型
# try/except语句去捕捉异常，从上往下运行，如果第一个except语句就捕捉到了对应错误，后面except语句都不会执行了
# except后面还可以跟上两个语句:else和finally
# else：缩进的代码块里放上当try里面的语句没有产生任何错误时要执行的语句
# finally：缩进的代码块里放上无论错误发生与否最终都会被执行的语句
# finally 厉害在于无论错误被某个except语句捕捉还是没有任何错误产生还是出现了未捕捉到的错误，里面的代码最终都会被执行




user_input1 = input("请输入第一个数字：")
user_input2 = input("请输入第二个数字：")
try:
    result = int(user_input1) + int(user_input2)
except ValueError:
    print("请输入合理的数字。")
else:
    print(result)
