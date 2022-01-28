from matplotlib.pyplot import *
import numpy as np
import random
import time

# 生成数据的方式:
# 直接从数组生成:

score = np.array( # 直接使用array生成ndarray类型
    [
        [80, 89, 86, 67, 79],
        [78, 97, 89, 67, 81],
        [90, 94, 78, 67, 74],
        [91, 91, 90, 67, 69],
        [76, 87, 75, 67, 86],
        [70, 79, 84, 67, 84],
        [94, 92, 93, 67, 64],
        [86, 85, 83, 67, 80]
    ]
)

print("score: \n", score)
print("type(score): ", type(score))  # <class 'numpy.ndarray'>

# 这种嵌套列表的形式, 我们使用python原生list也可以实现, 为什么转而使用ndarray
# 效率对比
# 生成一个大一点的数组:
python_List = list()

for i in range(10000000):
    python_List.append(i)
ndarray_list = np.array(python_List) # 将列表数据转换成ndarray类型
