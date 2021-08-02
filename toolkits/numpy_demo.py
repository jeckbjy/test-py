# -*- coding: utf-8 -*

# 注意：文件名不能为numpy.py，否则会报错:AttributeError: 'module' object has no attribute 'array'

import numpy as np

# 一维
a = np.array([1,2,3])  
print (a)

# 二维
b = np.array([[1,  2],  [3,  4]])  
print(b)

# 使用最小维度,即输出的是二维数组
c = np.array([1, 2, 3, 4, 5], ndmin=2)
print(c)

# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)

# 类型字段名可以用于存取实际的 age 列
print(a['age'])

# 定义结构化数据
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
print(a.dtype)

# 数组属性

# ndarray.ndim 用于返回数组的维数，等于秩。
a = np.arange(24)  
print (a.ndim) # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)

# ndarray.shape: 表示数组的维度
a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
a.shape =  (3,2)  
print (a)

# ndarray.itemsize: 以字节的形式返回数组中每一个元素的大小。
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)

# ndarray.flags: 返回 ndarray 对象的内存信息

# 创建方式:
x = np.empty([3,2], dtype = int) 
print(x)
y = np.zeros((5,), dtype = np.int) 
print(y)
x = np.ones([2,2], dtype = int)
print(x)

# 从数值范围创建数组
# numpy.arange(start, stop, step, dtype)
x = np.arange(5)  
print (x)

# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
a = np.linspace(1,10,10)
print(a)
# numpy.logspace 函数用于创建一个于等比数列。格式如下：
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
a = np.logspace(1.0,  2.0, num =  10)  
print (a)
