# 线性代数
# 标量由只有一个元素的张量表示
import torch

x = torch.tensor([3.0])
y = torch.tensor([2.0])

print(x + y,x * y,x / y,x**y)

# 可以将向量视为标量值组成的列表
x = torch.arange(4)
print(x)

# 通过张量的索引来访问任一元素
print(x[3])

# 访问张量的长度
print(len(x))

# 只有一个轴的张量，形状只有一个元素
print(x.shape)

# 通过指定的两个分量m和n来创建一个形状为m×n的矩阵
A = torch.arange(20).reshape(5,4)
print(A)
# 矩阵的转置
print(A.T)
# 对称矩阵，A等于其转置
B = torch.tensor([[1,2,3],[2,0,4],[3,4,5]])
print(B)
print(B == B.T)
# 向量是标量的推广，矩阵是向量的推广，可以构建具有更多轴的数据结构
x = torch.arange(24).reshape(2,3,4)
print(x)

# 给定具有相同形状的任何两个张量，任何按元素二元运算的结果都将是相同形状的张量
A = torch.arange(20,dtype=torch.float32).reshape(5,4)
B = A.clone() # 通过分配新内存，将A的一个副本分配给B
print(A)
print(A + B)

# 两个矩阵按元素乘法称为哈达玛积
print(A * B)

a = 2
X = torch.arange(24).reshape(2,3,4)
print(a + X)
print((a * X).shape)

# 计算其元素的和
x = torch.arange(4,dtype=torch.float32)
print(x,x.sum())
A = torch.arange(20*2).reshape(2,5,4)
print(A)
print(A.shape,A.sum()) # 表示任意形状张量的元素和,40个数相加

# 指定求和汇总张量的轴
# 演示sum()的axis参数：沿哪个维度求和，哪个维度就会“消失”
A_sum_axis0 = A.sum(axis=0) # axis=0表示沿着第0维求和，也就是把“两摞表”对应位置加起来，摞数从2变成1
print(A_sum_axis0)
print(A_sum_axis0.shape) # 原来的第0维（长度2）消失了，剩下的就是[5,4]

A_sum_axis1 = A.sum(axis=1) # axis=1表示沿着第1维（5行）求和:每一列把5行的数加起来，但两摞表分别算，互不混合
print(A_sum_axis1)
print(A_sum_axis1.shape) # 原来的第1维（长度5）消失了，剩下[2,4]

print(A.sum(axis=[0,1]))# 一次消掉两个维度：同时沿第0 维和第1维求和，等价于把两摞表共10行全部按列加起来
print((A.sum(axis=[0,1])).shape)

# 一个与求和相关的量是平均值（mean or average），整数不能求平均值！
A = torch.arange(20,dtype=torch.float32).reshape(5,4)
print(A.mean())
print(A.sum() / A.numel())

print(A.mean(axis=0)) # 按第0维求平均：两块对应位置取平均，结果形状[5,4]
print(A.sum(axis=0) / A.shape[0]) # axis=0的和÷块数(A.shape[0]就是2)，结果与A.mean(axis=0)相同

# 计算总和或均值时保持轴数不变
# axis=1是沿“5行”求和。如果直接求和，形状会从[2,5,4]变成[2,4],第1维消失了
# 加上keepdim=True，第1维不消失，而是变成长度1
sum_A = A.sum(axis=1,keepdim=True)
print(sum_A)

# 通过广播将A除以sum_A
# A形状[2,5,4]，sum_A形状[2,1,4]。两者相除时按广播规则比较
# sum_A在第1维只有1行，被“复制”成5行，于是A的每一行都除以该列的总和
print(A / sum_A)
# 结果里每一列加起来正好等于1——这就是“归一化”

# 某个轴计算A元素的累积总和
print(A.cumsum(axis=0)) # cumsum=cumulative sum，累积求和
# sum：只给一个最终结果;cumsum：把每一步累加的结果都留下来

# 点积是相同位置的按元素乘积的和
y = torch.ones(4,dtype=torch.float32)
print(x,y,torch.dot(x,y))  # dot就是点积
# 通过执行按元素乘法，然后进行求和来表示两个向量的点积
print(torch.sum(x * y))

# 矩阵向量积Ax是一个长度为m的列向量
print(A.shape,x.shape,torch.mv(A,x)) # mv就是matrix-vector的缩写(矩阵×向量)

# 矩阵的乘法AB
B = torch.ones(4,3) # A是5×4的矩阵，B是4×3的矩阵
print(B)
print(torch.mm(A,B))

# L2范数(norm)，是向量元素平方和的平方根
u = torch.tensor([3.0,-4.0])
print(torch.norm(u)) 
# L1范数，表示为向量元素的绝对值(abs)之和
print(torch.abs(u).sum())
# 矩阵的Frobenius norm是矩阵元素的平方和的平方根
print(torch.norm(torch.ones(4,9)))




