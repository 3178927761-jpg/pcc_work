# 数据预处理
# 创建一个人工数据集，并存储在csv（逗号分隔值）文件
import os

os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv') # 创建一个csv文件，存储在../data/house_tiny.csv
# csv文件每一行是一个数据样本，每个entry的每个字段用逗号分隔
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n') # 列名，每一列分别是房子的数目、进房子的路是什么样的、房子的价格
    f.write('NA,Pave,127500\n')       # 第一行数据，NA表示未知的，Pave表示铺过的路，127500是房子的价格
    f.write('2,NA,106000\n')          # 第二行数据
    f.write('4,NA,178100\n')          # 第三行数据
    f.write('NA,NA,140000\n')         # 第四行数据     
    
import pandas as pd
data = pd.read_csv(data_file)
print(data) # 读取csv文件，并打印出来

# 为了处理缺失的数据，典型的方法包括插值和删除，考虑插值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2] 
# iloc(index location)：按位置选取数据，iloc[:, 0:2]表示选取所有行的第0列和第1列，iloc[:, 2]表示选取所有行的第2列
inputs = inputs.fillna(inputs.mean(numeric_only=True))
# numeric_only=True 的意思是“只对数值列求均值”，Alley这种字符串列会被跳过，不参与计算。
# fillna：用指定的值填充缺失值，input.mean()表示用每一列的均值填充缺失值
print(inputs) # 打印处理后的输入数据
print(outputs) # 打印输出数据

# 对于inputs中的类别值或离散值，将“NaN”视为一个类别
inputs = pd.get_dummies(inputs, dummy_na=True) 
# get_dummies：将类别变量转换为虚拟变量（one-hot编码），dummy_na=True表示将NaN视为一个类别
print(inputs)

# 现在inputs和outputs中的所有条目都是数值类型，它们可以转换为张量格式
import torch

x, y = torch.tensor(inputs.to_numpy(dtype=float)), torch.tensor(outputs.to_numpy(dtype=float))
print(x)
print(y)

import numpy as np

X = torch.tensor(inputs.to_numpy(dtype=np.float32))
y = torch.tensor(outputs.to_numpy(dtype=np.float32))
print(X)
print(y)
