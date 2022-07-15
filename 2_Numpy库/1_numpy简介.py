"""
numpy是什么: 一个开源的python科学计算库
    使用Numpy可以方便的使用数组, 矩阵等运算
    包含线性代数, 傅里叶变换, 随机数生成等大量函数.
为什么使用Numpy:
    代码更简洁, 性能更高效. 同时numpy是很多库的基础库.
    numpy的数据存储和python原生list是不一样的
    numpy底层是C语言实现的. 没有线程限制.

numpy ndarray对象:
    numpy定义了一个n维数组对象, 简称ndarray对象, 是一个有相同数据类型元素组成的数组集合.
    数组中的每个元素都占有相同大小的内存块.
    ndarray对象 采用用了数组的索引机制, 将数组中的每个元素映射到内存块上, 并且按照一定的布局对内存块进行排列(行或列)



"""

import numpy as np

print(np.__version__) # 1.22.4




