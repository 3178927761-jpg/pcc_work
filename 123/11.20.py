# 矩阵计算：矩阵如何求导数，机器学习或者深度学习，优化模型的求解都是通过求导数来进行的
import torch

x = torch.arange(4.0)        # [0., 1., 2., 3.]
x.requires_grad_(True)       # 告诉 PyTorch：这个张量要算梯度

y = 2 * torch.dot(x, x)      # y = 2 * (x0² + x1² + x2² + x3²)
y.backward()                 # 反向传播，自动求导

print(x.grad)               

# 自动求导
x = torch.arange(4.0)
print(x)

# 计算y关于x的梯度之前，需要一个地方来存储梯度
x.requires_grad_(True) # 等价于：x = torch.arange(4.0, requires_grad=True)
print("x.grad 初始值:", x.grad)   # 默认值是None；y关于x的梯度存储在grad里
# 来计算y
y = 2 * torch.dot(x, x)
print("y =", y)                  

# 调用反向传播函数来自动计算y关于x每个分量的梯度
y.backward()                      # 反向传播，自动求导
print("x.grad =", x.grad)         

print("梯度是否正确:", x.grad == 4 * x)

# 计算x的另一个函数
# 默认情况下，PyTorch会累积梯度，需要清楚之前的值
x.grad.zero_()                    # 将零写进梯度里，即清空之前的梯度，否则会累加
y = x.sum()
y.backward()
print("x.grad =", x.grad)   

# 对非标量调用backward需要传gradient参数，该参数指定微分方程关于self的梯度
# 求偏导数的和，所以传递一个1的梯度
x.grad.zero_()
y = x * x
# 等价于y.backward(torch.ones(len(x)))
y.sum().backward() # y.sum()变成标量，再进行求导
print("x.grad =", x.grad) 

# 将某些计算移动到记录的计算图之外
x.grad.zero_()
y = x * x 
u = y.detach()                    # u作为常数处理；detach() 就是把这个数的“来历”抹掉，只留下这个数本身
z = u * x

z.sum().backward()
print("z对x的梯度 == u:", x.grad == u)   

x.grad.zero_()
y.sum().backward()                # 在y上调用反向传播函数，得到梯度是2*x
print("y对x的梯度 == 2*x:", x.grad == 2 * x)  

def f(a):
    b = a * 2
    while b.norm() < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c
a = torch.randn(size=(),requires_grad=True) #randn是生成什么数，size=()是生成几个、什么形状
# size=()表示零维张量，也就是一个标量，它没有形状，就是一个数
d = f(a)
d.backward()
print(a.grad == d / a)
# 梯度的意思是：a变一点点，d跟着变多少倍



