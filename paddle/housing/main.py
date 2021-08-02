# -*- coding: utf-8 -*

# 使用Python和Numpy来构建神经网络-波士顿房价预测
# https://www.paddlepaddle.org.cn/tutorials/projectdetail/1925542
#
# 手动计算梯度:

import numpy as np
import json
import os

np.set_printoptions(precision=4,suppress=True)

current_work_dir = os.path.dirname(__file__)
print(current_work_dir)
os.chdir(current_work_dir)

def load_data():
    # 前N列为指标，最后一列为价格
    datafile = './housing.data'
    data = np.fromfile(datafile, sep=' ')
    print(data)

    # 读入之后的数据被转化成1维array，其中array的第0-13项是第一条数据，第14-27项是第二条数据，以此类推.... 
    # 这里对原始数据做reshape，变成N x 14的形式
    feature_names = [ 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE','DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]
    feature_num = len(feature_names)
    data = data.reshape([data.shape[0] // feature_num, feature_num])

    # x = data[0]
    # print(x.shape)
    # print(x)

    # 划分数据集，80%用作训练集，20%用作测试集
    ratio = 0.8
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]
    print(training_data.shape)

    # 数据归一化处理

    ## 计算train数据集的最大值，最小值，平均值
    # maximums, minimums, avgs = training_data.max(axis=0), training_data.min(axis=0), training_data.sum(axis=0) / training_data.shape[0]
    maximums, minimums = training_data.max(axis=0), training_data.min(axis=0)
    # print(maximums, minimums, avgs)
    ## 对数据进行归一化处理
    ## 为什么要归一化处理? 这是为了后边在进行梯度下降时，让所有变量变化的步长保持一致
    for i in range(feature_num):
        #print(maximums[i], minimums[i], avgs[i])
        data[:, i] = (data[:, i] - minimums[i]) / (maximums[i] - minimums[i])
    
    print('data', data)
    # 训练集和测试集的划分比例
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data

# 获取数据
training_data, test_data = load_data()
# numpy切片操作：
x = training_data[:, :-1]
y = training_data[:, -1:]

# 查看数据
print('x0:',x[0])
print('y0:',y[0])


# 模型设计

# 假定模型为线性模型即：y=wx+b

class Network(object):
    def __init__(self, num_of_weights):
        # 随机产生w的初始值
        # 为了保持程序每次运行结果的一致性，
        # 此处设置固定的随机数种子
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights, 1)
        self.b = 0.
    
    def forward(self, x):
        # 前向计算: 通过模型和训练集数据计算
        z = np.dot(x, self.w) + self.b
        return z

    def loss(self, z, y):
        # 定义损失函数,通过损失函数来衡量模型的好坏
        error = z - y
        cost = error * error
        cost = np.mean(cost)
        return cost

    def gradient(self, x, y):
        # 计算梯度
        z = self.forward(x)
        gradient_w = (z-y)*x
        gradient_w = np.mean(gradient_w, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = (z - y)
        gradient_b = np.mean(gradient_b)
        
        return gradient_w, gradient_b
    
    def update(self, gradient_w, gradient_b, eta = 0.01):
        self.w = self.w - eta * gradient_w
        self.b = self.b - eta * gradient_b
        
    def train(self, x, y, iterations=100, eta=0.01):
        # 训练模型
        losses = []
        for i in range(iterations):
            z = self.forward(x)
            L = self.loss(z, y)
            gradient_w, gradient_b = self.gradient(x, y)
            self.update(gradient_w, gradient_b, eta)
            losses.append(L)
            if (i+1) % 10 == 0:
                print('iter {}, loss {}'.format(i, L))
        return losses

## 前向计算结果和误差
net = Network(13)
x1 = x[0]
y1 = y[0]
z = net.forward(x1)
print('predict:',z)
loss = net.loss(z, y1)
print('loss:',loss)


# 训练过程:
# 训练过程是深度学习模型的关键要素之一，其目标是让定义的损失函数LossLossLoss尽可能的小，也就是说找到一个参数解w和b，使得损失函数取得极小值

net = Network(13)
losses = []
#只画出参数w5和w9在区间[-160, 160]的曲线部分，以及包含损失函数的极值
w5 = np.arange(-160.0, 160.0, 1.0)
w9 = np.arange(-160.0, 160.0, 1.0)
losses = np.zeros([len(w5), len(w9)])

#计算设定区域内每个参数取值所对应的Loss
for i in range(len(w5)):
    for j in range(len(w9)):
        net.w[5] = w5[i]
        net.w[9] = w9[j]
        z = net.forward(x)
        loss = net.loss(z, y)
        losses[i, j] = loss

#使用matplotlib将两个变量和对应的Loss作3D图
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)

# w5, w9 = np.meshgrid(w5, w9)

# ax.plot_surface(w5, w9, losses, rstride=1, cstride=1, cmap='rainbow')
# plt.show()

## 梯度下降法的方案:
# 步骤1：随机的选一组初始值，例如：[w,b]=[−100.0,−100.0][w_5, w_9] = [-100.0, -100.0]
# 步骤2：选取下一个点[w', b'],使得L(w', b') < L(w,b) 
# 步骤3: 重复步骤2，直到损失函数几乎不再下降。

x1 = x[0]
y1 = y[0]
z1 = net.forward(x1)
print('x1 {}, shape {}'.format(x1, x1.shape))
print('y1 {}, shape {}'.format(y1, y1.shape))
print('z1 {}, shape {}'.format(z1, z1.shape))

gradient_w0 = (z1 - y1) * x1[0]
print('gradient_w0 {}'.format(gradient_w0))

gradient_w1 = (z1 - y1) * x1[1]
print('gradient_w1 {}'.format(gradient_w1))

gradient_w2= (z1 - y1) * x1[2]
print('gradient_w1 {}'.format(gradient_w2))

gradient_w = (z1 - y1) * x1
print('gradient_w_by_sample1 {}, gradient.shape {}'.format(gradient_w, gradient_w.shape))

x3 = x[2]
y3 = y[2]
z3 = net.forward(x3)
gradient_w = (z3 - y3) * x3
print('gradient_w_by_sample3 {}, gradient.shape {}'.format(gradient_w, gradient_w.shape))

# 注意这里是一次取出3个样本的数据，不是取出第3个样本
x3samples = x[0:3]
y3samples = y[0:3]
z3samples = net.forward(x3samples)

print('x {}, shape {}'.format(x3samples, x3samples.shape))
print('y {}, shape {}'.format(y3samples, y3samples.shape))
print('z {}, shape {}'.format(z3samples, z3samples.shape))

gradient_w = (z3samples - y3samples) * x3samples
print('gradient_w {}, gradient.shape {}'.format(gradient_w, gradient_w.shape))

z = net.forward(x)
gradient_w = (z - y) * x
print('gradient_w shape {}'.format(gradient_w.shape))
print(gradient_w)

# axis = 0 表示把每一行做相加然后再除以总的行数
gradient_w = np.mean(gradient_w, axis=0)
print('gradient_w ', gradient_w.shape)
print('w ', net.w.shape)
print(gradient_w)
print(net.w)

gradient_w = gradient_w[:, np.newaxis]
print('gradient_w shape', gradient_w.shape)


# 调用上面定义的gradient函数，计算梯度
# 初始化网络
net = Network(13)
# 设置[w5, w9] = [-100., -100.]
net.w[5] = -100.0
net.w[9] = -100.0

z = net.forward(x)
loss = net.loss(z, y)
gradient_w, gradient_b = net.gradient(x, y)
gradient_w5 = gradient_w[5][0]
gradient_w9 = gradient_w[9][0]
print('point {}, loss {}'.format([net.w[5][0], net.w[9][0]], loss))
print('gradient {}'.format([gradient_w5, gradient_w9]))