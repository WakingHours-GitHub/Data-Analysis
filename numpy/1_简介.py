"""
numpy数据类型:
    numpy数据类型有很多

    numpy的数值类型实际上是dtype对象的实例, 并对应唯一的字符, 包括np.bool_, np.int32, np.float32.等.


数据类型对象: dtype.
    数据类型对象是用来描述与数组对应的内存区域如何使用, 这依赖于这几个方面.
    数据的类型:
    数据的大小:
    数据的字节顺序(大端, 小端)









"""


import numpy as np



# 创建数据类型对象
# dt = np.dtype(dtype, align, copy)

dt = np.dtype(np.int32) # 类型对象.





print(dt)
print(type(dt))