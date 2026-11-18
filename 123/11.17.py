# 数据操作
# 引入torch库，torch = 张量计算器 + 自动求导引擎 + 神经网络工具箱 + GPU（图形处理器）加速
import torch
# 张量表示一个数值组成的数组，这个数组可能有多个维度
x = torch.arange(12)
print(x)
# 可以通过张量的shape属性来访问张量的形状和张量中的元素个数
print(x.shape)        
print(x.numel())      

# 要改变一个张量的形状而不改变元素的数量和元素值，可以调用reshape函数
y = x.reshape(3, 4)   # 3×4的矩阵
print(y)

# 使用全 0、全 1、其他常量或者从特定分布中随机采样的数字
print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))
print(torch.randn(3, 4))

# 通过提供包含数值的Python列表（或嵌套列表）来为所需张量中的每个元素赋予确定值
torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
print(torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]]))

torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]]).shape
print(torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]]).shape)

# 常见的标准算术运算符（+、-、*、/、**求幂运算）都可以被升级为按元素运算
a = torch.tensor([1.0, 2, 4, 8])
b = torch.tensor([2, 2, 2, 2])
print(a + b, a - b, a * b, a / b, a ** b)
torch.exp(a)
print(torch.exp(a)) # 做指数运算

# 多个张量连结在一起
# reshape：同一个张量换个形状，元素总数不变;cat：把多个张量合成一个，元素总数变多
x = torch.arange(12,dtype=torch.float32).reshape((3,4)) 
# arange(12)：0~11 的一维张量,
# dtype=torch.float32：指定成浮点型(不加的话默认是整数 int64)
# .reshape((3, 4))：排成 3 行 4 列
y = torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
# 第一个数写了2.0，整个张量就被推断成浮点型，和x一致
#cat(concatenate，连接),cat的第一个参数是一个张量元组，不是单个张量
print(torch.cat((x,y), dim=0))
# dim=0是第0维，也就是“行”这个方向：把y摞在x下面
print(torch.cat((x,y), dim=1)) 
# dim=1是第1维，也就是“列”这个方向：把y接在x的右边，逐行对齐

# 通过逻辑运算符构建二维张量
x == y
print(x == y)

# 对张量中的所有元素进行求和会产生一个只有一个元素的张量
print(x.sum())

# 即使形状不同，仍然可以通过调用广播机制来执行按元素操作
# 广播机制：如果两个张量的形状不同，PyTorch会自动地将它们的形状扩展为相同的形状，然后再进行按元素操作
a = torch.arange(3).reshape((3, 1)) 
# a的列从1扩成 2（把唯一的一列复制一份，横向铺开）
b = torch.arange(2).reshape((1, 2)) 
# b的行从1扩成3（把唯一的一行复制两份，纵向摞起来）
print(a)
print(b)
print(a + b) # 3行2列的矩阵
print(a * b) # *是“同一个位置相乘”，@是“行乘列求和”，前者靠广播对齐形状，后者靠矩阵维度匹配

# 可以用[-1]选择最后一个元素，可以用[1：3]选择第二个和第三个元素
print(x[-1])       # 最后一行
print(x[1:3])      # 第1行和第2行


# 通过指定索引来将元素写入矩阵
x[1, 2] = 9 # 将第1行第2列的元素改为9（行和列都是从0开始计数）
print(x)

# 为多个元素赋值相同的值，只需要索引所有元素，然后将它们设置为相同的值即可
x[0:2, :] = 12 # 将第0行和第1行、所有列的元素都设置为12
print(x)

# 运行一些操作可能会导致为新结果分配内存
before = id(y)
y = y + x
print('id(y):', id(y))
print('id(y) == before:', id(y) == before)

# 执行原地操作
z = torch.zeros_like(y) # 创建一个和y形状一样的全0张量
print('id(z):', id(z)) 
z[:] = y + x
print('id(z):', id(z)) # True，z的id没变，说明z指向的内存地址没变，只是里面的元素值变了

# 如果在后续计算中没有重复使用x，也可以使用x[:]=x+y或x+=y来减少操作的内存开销
before = id(x)
x += y
print('id(x):', id(x))
print('id(x) == before:', id(x) == before)

# 转换为NumPy张量
A = x.numpy() # 将PyTorch张量转换为NumPy张量  numpy.ndarray：“NumPy 数组”
B = torch.tensor(A) # 将NumPy张量转换为PyTorch张量
print(type(A)) 
print(type(B))

# 将大小为1的张量转换为Python标量
a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a)) # item()返回一个Python数值
# 张量 ↔ NumPy 用.numpy()和torch.tensor()
# 张量 → Python 数字用.item()

