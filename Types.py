# 对字符串求长度
s=("Hello world!")
len(s)
print(len(s))

# 通过索引获取单个字符
print(s[0])
print(s[11])
print(s[len(s)-1])

# 布尔类型
b1=True
b2=False

# 空值类型
n=None

# type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(3.3))

# len(b1)错误，操作对象的所属类型是布尔类型bool，没有长度，len()函数支持字符串