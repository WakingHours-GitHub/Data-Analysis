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
        
    4.1.2 为什么使用Pandas
        便捷的数据处理能力
        读取文件方便
        封装了Matplotlib、Numpy的画图和计算
    4.1.3 DataFrame
        结构：既有行索引，又有列索引的二维数组
        属性：
            shape
            index
            columns
            values
            T
        方法：
            head()
            tail()
        3 DataFrame索引的设置
            1）修改行列索引值
            2）重设索引
            3）设置新索引
    2 Panel
        DataFrame的容器
    3 Series
        带索引的一维数组
        属性
            index
            values
    总结：
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