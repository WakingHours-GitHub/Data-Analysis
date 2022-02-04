"""
Pandas
    基础处理
        Pandas是什么？为什么用？
        核心数据结构
            DataFrame
            Panel
            Series
        对这些数据结构的基本操作
        运算
        画图(集成了matplotlib)
        文件的读取与存储
    高级处理

4.1Pandas介绍
    4.1.1 Pandas介绍 -> 数据处理工具
        panel + data + analysis
        panel data面板数据 - 来源于: 计量经济学 通常存储三维数据
        
        以Numpy为基础, 借助Numpy模块在计算方面性能高的优势
        基于matplotlib, 能够进行简单的画图
        独特的数据结构 
        
    4.1.2 为什么使用Pandas
        便捷的数据处理能力(比如可用方便处理缺失值, 异常值)
        读取文件方便(支持多种不同文件类型的读取)
        封装了Matplotlib、Numpy的画图和计算
        
    pandas的三大核心数据结构:
        DataFrame, Panel, Series
        
    4.1.3 DataFrame
        结构：既有行索引，又有列索引的二维数组 -> 类似二维表
        DataFrame对象既有行索引, 又有列索引
            - 行索引, 表明不同行, 横向索引, 叫index
            - 列索引, 表明不同列, 纵向索引, 叫columms
        属性：
            shape -> 形状
            index -> 行索引列表
            columns -> 列索引列表
            values -> 直接获取其中array的值 (刨除行索引和列索引的值)
            T -> 转置
        方法：
            head()
            tail()
        3 DataFrame索引的设置
            1）修改行列索引值
                只能是统一的修改所有的行, 列索引值
            2）重设索引
                reset_index(drop=False)
                    功能: 设置新的下表索引
                    drop: 默认为False, 不删除原来索引, 如果为True,删除原来的索引值


            3）设置新索引
                设置某列值为新的索引:
                    set_index(keys, drop=True)
                        keys: 列索引名或列索引名称的列表
                        drop: boolean-, default: True, 当作新的索引, 删除原来的列
                # 当我们设置多个索引的时候,
                # 返回的就是MultiIndex了, 此时数据就是三维数据了
                MultiIndex: 多级或分层索引对象
                    index属性:
                        names: levels的名称
                        levels: 每个level的元组值
    2 Panel
        存储三维结构的面板数据.
        pd.Panel(data=None, items=None, major_axis=None, minor_axis=None, copy=False, dtype=None)
        DataFrame的容器
        但是: Pandas从版本0.20.0开始启用, 推荐的是用于表示3D数据的方法的DataFrame上的MultiIndex方法

    3 Series
        带索引的一维数组
        Series结构只有行索引
        属性
            index -> 行索引
            values -> 只有值的数组(ndarray)
        方法:
            创建Series:
                通过已有数据进行创建:
                    # 指定内容, 默认索引
                    pd.Series(np.arange())
                    # 指定索引
                    pd.Series([], index=[])
                    # 通过字典字典数据创建
                    pd.Series(dict)
    总结：
        Series是只带行索引的一维数组
        DataFrame是即带有行又带列的二维数组
        理解:
        DataFrame是Series的容器
        Panel是DataFrame的容器

4.2 基本数据操作
    4.2.1 索引操作
        1）直接索引
            先列后行
        2）按名字索引
            loc
        3）按数字索引
            iloc
        4）组合索引
            数字、名字
    4.2.3 排序
        对内容排序
            dataframe
            series
        对索引排序
            dataframe
            series
4.3 DataFrame运算
    算术运算
    逻辑运算
        逻辑运算符
            布尔索引
        逻辑运算函数
            query()
            isin()
    统计运算
        min max mean median var std
        np.argmax()
        np.argmin()
    自定义运算
        apply(func, axis=0)True
            func:自定义函数
4.4 Pandas画图
    sr.plot()
4.5 文件读取与存储
    4.5.1 CSV
        pd.read_csv(path)
            usecols=
            names=
        dataframe.to_csv(path)
            columns=[]
            index=False
            header=False
    4.5.2 HDF5
        hdf5 存储 3维数据的文件
            key1 dataframe1二维数据
            key2 dataframe2二维数据
        pd.read_hdf(path, key=)
        df.to_hdf(path, key=)
    4.5.3 JSON
        pd.read_json(path)
            orient="records"
            lines=True
        df.to_json(patn)
            orient="records"
            lines=True
"""