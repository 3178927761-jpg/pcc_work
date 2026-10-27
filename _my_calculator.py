# assert（断言） 后面可以跟上任何布尔表达式，也就是值为True或者False的表达式
# assert后面的表达式最终求值出来的结果为True，那么无事发生，继续运行后面的代码
# assert len("Hi")==2
# assert后面的表达式如果求值出来为False，就会产生AssertionError(断言错误)
# assert 1+2>6
# pytest 测试库安装
# 新建测试文件，文件名很重要，pytest库会自动寻找文件名test_开头或以_test结尾且后缀为.py的文件
# 为了调用要测试的功能，要在测试文件里把要测试的函数或类也引入进来
# 如果测试文件和被测试文件位于同一文件夹下，引入的语法是from 文件名 import 函数名（类名）

from my_calculator import my_adder

def test_positive_with_positive():
    assert my_adder(3,5)==8

def test_negative_with_positive():
    assert my_adder(-3,5)==3


# fixture 装饰器，本质上也是函数或类，可以添加额外功能，好处是我们不需要额外修改已有的代码