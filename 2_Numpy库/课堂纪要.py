
"""
Numpy -> 高效的运算工具
Numpy的优势
核心的一个数据结构, 就是ndarray对象
我们要研究它的 属性, 方法
从而对数据基本操作:
    ndarray.方法()
    numpy.函数名()
ndarray运算: (核心)
    逻辑运算
    统计运算
    数组间运算
    以及: 合并、分割、IO操作、数据处理

3.1 Numpy优势
    3.1.1 Numpy介绍 - 数值计算库, 用于快速处理任意维度的数组
        两个英文字母的缩写
            num - numerical 数值化的
            py - python
        ndarray: numpy中最重要的一个数据结构
            n - 任意个
            d - dimension 维度
            array - 数组
            该对象是一个快速并且灵活的大数据容器

    3.1.2 ndarray介绍
        NumPy提供了一个N维度数组类型ndarray, 它表述了相同类型的items的集合.
    3.1.3 ndarray与Python原生list运算效率对比
        Numpy专门针对ndarray的操作和运算进行了设计,
        所以数组的存储效率和输入输出性能优于Python中的嵌套列表,
        数组越大, Numpy的优势就越明显

    3.1.4 ndarray的优势
        1）存储风格 -> 内存块风格
            ndarray - 相同类型 - 通用性不强(底层 连续存放, 所以查找的效率就很高)
            list - 不同类型 - 通用性很强(所以底层是以引用的方式, 这样再查找的时候效率就低很多)
        2）并行化运算
            ndarray支持向量化运算
            机制(省略)
        3）底层语言是C
            底层使用C语言编写, 解除了GIL(全局解释器锁)

3.2 认识N维数组-ndarray属性
    3.2.1 ndarray的属性
          属性名字:           属性解释:
        ndarray.shape      数组维度的元组
        ndarray.ndim       数组维度
        ndarray.size       数组中的元素数量
        ndarray.itemsize   一个数组元素的长度(字节)
        ndarray.dtype      数组元素的类型
        常用的:
        shape -> 可以知道维度, 和大小: ndim, size
        dtype -> itemsize

        在创建ndarray的时候，如果没有指定类型, 那么默认类型:
            整数: int64
            浮点数: float64
    3.2.2 ndarray的形状
    看嵌套情况
    [1, 2, 3, 4]

    [[1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]]

    [[[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]],

      [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]],
    [[1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]]]
    3.2.3 ndarray的类型
        一大堆类型.

3.3 基本操作
    adarray.方法()
    np.函数名()
        np.array()
    3.3.1 生成数组的方法
        1）生成0和1
            np.empty(shape) # 创建新数组, 只分配内存空间但不填充任何值
            np.zeros(shape)
            np.ones(shape)
            np.*_like() 以另一个数组作为参数, 并 且根据其形状和dtype创建一个数组
        2）从现有数组中生成
            numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0) 深拷贝
            np.copy() 深拷贝
            np.asarray() 浅拷贝
            深拷贝: 拷贝引用
            浅拷贝: 复制一个新的对象
        3）生成固定范围的数组
            np.linspace(start, stop, num, endpoint, retstep, dtype)
                生成: [start, end] 一共有num个等间距的点

            np.arange(start, stop, step, dtype)
             -> range(start, stop, step)
                    生成: [a, b) c是步长

        4）生成随机数组:
            np.random模块:
            均匀分布:
                np.random.rand(d0, d1, ..., dn)
                    rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
                    dn表格每个维度
                    返回值为指定维度的array
                np.random.uniform(low=0.0, high=1.0, size=None)
                    功能: 从一共均匀分布[low, high)中随机抽样
                    参数:
                        low: 采样下界, float类型, 默认值为0
                        high: 采样上界, float类型, 默认值为1
                        size: 输出样本数目, 为int或元组类型, 例如, size(m, n, k) 则输出mnk个样本吗, 默认值为1
                    返回:
                        ndarray类型, 其形状和参数size中的描述一样
                np.random.randint(low, high=None, size=None, dtype='int')
                    从一个均匀分布中随机采样, 生成一个整数或者N维整数数组, 取值范围: 若high不为None时,
                    取[low, high)之间的随机整数, 否则取值[0, low)之间随机整数.
            正态分布:
                np.random.randn(d0, d1, ..., dn)
                    从标准正太分布中返回一个或多个样本值
                np.random.normal(loc=0.0, scale=1.0, size=None)
                    参数:
                        loc: 均值, 坐标轴
                        scale: 标准差, 离散程度
                        size: 输出的size, 默认为None, 只输出一个值
                    返回一个正太分布的随机数矩阵
                np.random.standard_normal(size=None)
                    返回指定形状的标准正态分布的数组
            分布状况 - 直方图
            1）均匀分布
                每组的可能性相等
            2）正态分布
                u: 均值,也是正态分布的坐标轴
                σ: 幅度、波动程度、集中程度、稳定性、离散程度
                    =sqrt(sum(xi-u)/N)

    3.3.2 数组的索引、切片
        ndarray[,..]
        # 与matlab差不多
    3.3.3 形状修改
        ndarray.reshape(shape) 返回新的ndarray，原始数据没有改变, # 只是将原来的数据进行了分割
            shape=(a, b) , 当a=-1时, 表示自动计算
        ndarray.resize(shape) 没有返回值, 对原始的ndarray进行了修改, 效果与reshape一样
            前两个都没有对行列进行转换, 只是简单的分割
        ndarray.T 转置 行变成列，列变成行, 转至是对行列进行转换. (是ndarray的属性, 修改原数组)
    3.3.4 类型修改
        ndarray.astype(type) -> 通用的
        ndarray序列化到本地 (序列化就是将python的数据, 编成流(bytes), 从而保存在本地)
        ndarray.tostring() # 序列化到本地
    3.3.5 数组的去重
        np.unique(ndarray)
        类似于: set() -> 不过set需要的是一维的.
        set(temp.flatten()) # 可以使用flatten, 这样数组就变成一维的了, 此时使用set就可以去重了


3.4 ndarray运算(高校运算)
    逻辑运算
        布尔索引
            我们不仅仅可以使用数字作为索引, 还可以使用bool值作为索引
            我们可以通过比较运算符, 得到一个逻辑数组
        通用判断函数
            np.all(布尔值(矩阵))
                只要有一个False就返回False，只有全是True才返回True
            np.any(bool matrix(布尔矩阵) )
                只要有一个True就返回True，只有全是False才返回False
            np.where（三元运算符）---
                np.where(布尔矩阵 , True的位置的值, False的位置的值)
        符合逻辑运算:
            np.logical_and(逻辑矩阵, 逻辑矩阵)
            np.logical_or(逻辑矩阵, 逻辑矩阵)
            # 例子: np.logical_and(temp > 0.5, temp < 0.1) 返回的仍然是逻辑矩阵
                实际上就是矩阵做逻辑运算(

    统计运算:
        统计指标函数
            min, max, mean, median, var, std
            np.函数名()
            ndarray.方法名
            例: np.max(A), 或者A.max()
        返回最大值、最小值所在位置: 返回相应的索引
            np.argmax(temp, axis=)
            np.argmin(temp, axis=)
        总结:
            np.min(a [, axis, out, keepdims]) # 找最大化值
            np.max(a [, axis, out, keepdims])
            np.median(a [, axis, dtype, out, keepdims])
            np.mean(a [, axis, dtype, out, keepdims])
            np.std()
            np.var()
            参数:
                a: 要统计计算的矩阵
                axis: 按照第几个维度排列, shape=(a, b, c...)
                    比如axis=0, 就是按照a维度来进行计算,
                    axis=-1, 就是按照最后一个维度进行计算.
                    在二维的时候, axis=0,表示按照列来计算, 得行向量
                      axis=1, 按照行来求最大值, 得列向量

    数组间运算:
        3.5.1 场景
        3.5.2 数组与数的运算
            ndarray数组与数进行运算, 直接是作用到数组里面去的.
            而原生list直接与数运算则会报错, 我们可以使用列表生成式,for, 或者map()
        3.5.3 数组与数组的运算
            执行broadcast的前提在于, 两个ndarray执行的是element-wish的运算,Broadcast机制的功能
            是方便不同形状的ndarray(numpy库的核心数据结构)进行数学运算.

            3.5.4 广播机制
                当操作两个数组的时, numpy会逐个比较他们的shape(构成的元组tuple),
                只有在每个维度满足:
                    - 维数相等
                    - shape(其中相对应的一个维度为1.)
                时, 两个数组才能够进行数组的运算.
                (这个维度, 要么维数相等, 要么shape有一方为1)
                最终取每个维度最大的, 为最后的形状

        3.5.5 矩阵运算 *** 重要的内容
            1 什么是矩阵
                矩阵matrix 二维数组
                矩阵 & 二维数组的区别:
                    矩阵的存储肯定是二维数组, 但是二维数组不一定是矩阵
                两种方法存储矩阵
                    1）ndarray 二维数组形式
                        矩阵乘法：
                            np.matmul() # 矩阵相乘
                             np.dot()
                    2）matrix数据结构
                        np.mat()
                            将数组转换成矩阵类型
                        直接操作

            2 矩阵乘法运算
                形状:
                    (m, n) * (n, l) = (m, l)
                    n必须相同, 这个规则在线性代数也是一样

                运算规则:
                    与线性代数内容一样.
                    A (2, 3) B(3, 2)
                    A * B = (2, 2)
                API:
                    np.matmul()
                    np.dot()

3.6 合并、分割
    合并
        np.hstack(tup) 水平合并数组
        np.vstack(tup) 垂直合并数组
        np.concatenate((a1, a2, ...), axis=0) 指定维度拼接.
    分割:
        np.split(A, indices_or_sections, axis=0)
        按照indices_or_sections(一个列表) 分割A, axis指定维度

3.7 IO操作与数据处理
    3.7.1 Numpy读取 数据文件
        np.genfromtxt(fname[, dtype, comments, ...], delimiter=)
        功能: 加载数据文件
        参数:
            fname: 数据文件路径
            delimiter: 指定分隔符
    3.7.2 如何处理缺失值
    缺失值: 什么时候numpy会出现nan: 当我们读取本地文件为float的时候, 如果有缺失值(或者为None), 就会出现nan
    缺失值处理:
        两种思路：
            直接删除含有缺失值的样本, 整条删除 (数据量较大的情况)
            替换/插补 (插值, 滑动窗格)
                按列求平均，用平均值进行填补
        这里使用numpy直接对数据进行处理是比较困难啊的, 不过问题不大,后面我们会学pandas, 方便多了!
"""




























