"""
6天 半天
1 Matplotlib 画图
2 Numpy 高效的运算工具
3、4 Pandas 数据处理工具
5、6 金融数据分析与挖掘

数据挖掘基础 - 人工智能阶段的基础
人工智能 - 大量的运算

目标：熟练掌握三大工具
任务：掌握常用的方法
态度：放轻松

一、数据挖掘基础环境安装与使用
1.1 库的安装
    matplotlib==2.2.2
    numpy==1.14.2
    pandas==0.20.3
    TA-Lib==0.4.16 技术指标库
    tables==3.4.2 hdf5
    jupyter==1.0.0 数据分析与展示的平台
1.2 Jupyter Notebook使用
    加强版的ipython
    1.2.1 Jupyter Notebook介绍
        1）web版的ipython
        2）名字
        ju - Julia
        py - Python
        ter - R
        Jupiter 木星 宙斯
        3）编程、写文档、记笔记、展示
        4）.ipynb
    1.2.2 为什么使用Jupyter Notebook?
        1）画图方面的优势(matplotlib)
        2）数据展示方面的优势, (无需重新加载)

    快速上手ipython notebook
    1.2.3 Jupyter Notebook的使用-helloworld
        1 界面启动、创建文件
            在终端输入jupyter notebook / ipython notebook -> 直接在浏览器中打开软件
            快速上手的方法：-> 学习快捷键
                快捷键

                    运行代码                ctrl + enter
                    运行代码并且切换到下一节 shift + enter

        2 cell操作
            cell：一对In Out会话被视作一个代码单元，称为cell
            编辑模式：
                enter
                鼠标直接点
            命令模式：
                esc
                鼠标在本单元格之外点一下
            2）快捷键操作
                执行代码：shift + enter
                命令模式：
                A，在当前cell的上面添加cell
                B，在当前cell的下面添加cell
                双击D：删除当前cell
                编辑模式：
                多光标操作：Ctrl键点击鼠标（Mac:CMD+点击鼠标）
                回退：Ctrl+Z（Mac:CMD+Z）
                补全代码：变量、方法后跟Tab键
                为一行或多行代码添加/取消注释：Ctrl+/（Mac:CMD+/）
            3 markdown演示, 程序员的笔记语法
                # 一级标题, 有几个#就是几级标题
                - 缩进
二、Matplotlib
    2.1 Matplotlib之HelloWorld
        2.1.1 什么是Matplotlib - 画二维图表的python库
            三个英文缩写:
                mat - matrix 矩阵
                    二维数据 - 二维图表
                plot - 画图
                lib - library 库
            学术上: 
                matlab -> 矩阵实验室
                    mat - matrix
                    lab 实验室

            所以， matplotlib就是画2维图表的库
        2.1.2 为什么要学习Matplotlib - 画图
            数据可视化 - 帮助理解数据，方便选择更合适的分析方法
            js库 - 百度:D3 国内:echarts -> 数据展示图 -> 这两个网站就是数据可视化的.
            
            我们学习的: 奥卡姆剃刀原理 - 如无必要勿增实体
                所以我们只需要学习matplotlib然后学习数据的关系就可以了
        2.1.3 实现一个简单的Matplotlib画图
            
        2.1.4 认识Matplotlib图像结构
        2.1.5 拓展知识点：Matplotlib三层结构
            容器层, 辅助显示层, 图像层
            1）容器层
                画板层Canvas: 是位于最底层的系统层, 在绘图的过程中充当画板的角色, 即放置画布(figure)的工具
                画布层Figure -> plt.figure() 是Canvas上方的第一层, 也是需要用户来操作的应用层的第一层, 在绘图的过程中充当画布的角色
                绘图区/坐标系axes -> 其中:一个画布层可以有多个绘图区的
                    plt.subplots()
                    可以看成:绘图区就是由 x、y轴(axis:轴)张成的区域
                            所以也叫axes(axis复数)
                    所以 辅助显示层和图像层都是在绘图区之上的
                    2）辅助显示层
                        帮助我们理解图表的, 例如: 图例, 刻度...
                    3）图像层
                        就是绘制图表的, 例如: 折线图, 散点图

    2.2 折线图(plot)与基础绘图功能
        matplotlib.pyplot模块: 包含一些列类似于matlab的画图函数
            import matplotlib.pyplot as plt
        2.2.1 折线图绘制与保存图片
            创建画布:
                plt.figure(figsize=(), dpi=)
                参数
                    figsize: 指定图的长宽
                    dpi: 图像的清晰度
                return:
                    返回fig对象
            保存图片:
                plt.savefig(path)
                注意, 如果在plt.show()之后保存图片, 得到的是空白图片
                原因: plt.show()会释放figure资源, 如果在显示图像之后保存图片只会保存空图片
            设置坐标轴:
            plt.xticks(x, **kwargs)
                x: 要显示的刻度值
                kwargs: 刻度说明, 要与x一一对应
            plt.yticks(y, **kwargs)
                y: 要显示的刻度值
                kwargs: 刻度说明, 要与y一一对应
            设置网格:
                plt.grid(True, linestyle='--'. alpha=)
                作用: 添加网格线
                参数:
                    是否添加, grid
                    linestyle: 网格线的风格
                    alpha: 透明度
            添加标题:
                图表标题:
                plt.title() #  添加图表说明(标题)
                plt.xlabel() # 添加x轴说明
                plt.ylabel() # 添加y轴说明
                参数都是字符串
            设置图像风格:
                颜色字符:          风格字符
                r -> 红色         - 实线
                g -> 绿色         -- 虚线
                b -> 蓝色         -. 点划线
                w -> 白色         : 点虚线
                c -> 青色         ' ' 留空, 空格
                m -> 杨红
                y -> 黄色
                k -> 黑色
            # 图例需要图像层和辅助显示层
            # 我们需要在图像层设置图例, 然后在辅助显示层开启
            # 在plot的时候, 设置label, 然后调用plt.legend()开启图例
            # 显示图例
            plt.legend()
            我们还可以先择图例展示的位置:
                plt.legend(loc=)
                有: 直接让loc=
                    Location String         Location Code
                        'best'                    0
                        'upper right'             1
                        'upper left'              2
                        'lower left'              3
                        'lower right'             4
                        'right'                   5
                        'center left'             6
                        'center right'            7


            3 设置画布属性与图片保存
                figsize : 画布大小
                dpi : dot per inch 图像的清晰度, 每英寸多少个点
            3 中文显示问题解决(matplotlib是外国人写的, 所以不支持中文)
                我们需要安装支持中文的字体: SumHei字体
                mac的一次配置，一劳永逸
                ubantu每创建一次新的虚拟环境，需要重新配置
                windows
                1）安装字体
                    mac/wins：双击安装
                    ubantu：双击安装
                2）删除matplotlib缓存文件
                3）配置文件
        2.2.4 多个坐标系显示-plt.subplots(面向对象的画图方法)
            figure, axes = plt.subplots(nrows=1, ncols=1, **fig_kw)
            创建一个带有多个axes的回去
                nrows: 几行
                ncols: 几列
                **fig_kw: 可选参数, 例如figsize, dpi
            return:
                fig: 图对象
                ax: 绘图区
            如何在不同的绘图区中画图呢?
            axes[0].方法名() # 操作绘图区1
            axes[1]
            注意: plt.函数名()相当于面向过程的画图方法, axes.set_方法名()相当于面向对象的画图方法

        2.2.5 折线图的应用场景
            某事物、某指标随时间的变化状况
            拓展：画各种数学函数图像


2.3.1 常见图形种类及意义
    折线图: plot
    散点图: scatter
        判读变量之间是否存在数量关联趋势, 展示离群点(分布规律)
        -> 关系/规律
        与plot函数一样, 直接使用即可, 传入x, y
    柱状图: bar
        绘制离散的数据, 能够一眼看出各个数据的大小, 比较数据之间的差别
        -> 统计/对比
        API:
            plt.bar(x, y, width, align='center', **kwargs)
                x: 类别 -> 横坐标
                y: 对应的值 -> 纵坐标
                width: 柱状图的宽度
    直方图: histogram
        绘制连续性的数据展示一组或者多组数据的分布状况(统计)
        -> 分布状况
        
    饼图: pie π
        分类数据的占比情况
        -> 占比

    2.3.2 散点图绘制

    2.4 柱状图(bar)
        2.4.1 柱状图绘制
    2.5 直方图(histogram)
        2.5.1 直方图介绍
            概念:    
            组数：在统计数据时，我们把数据按照不同的范围分成几个组，分成的组的个数称为组数
            组距：每一组两个端点的差
            
            根据总的, 求组数
            已知 最高175.5 最矮150.5 组距5
            求 组数：(175.5 - 150.5) / 5 = 5
            
        2.5.2 直方图与柱状图的对比
            1. 直方图展示数据的分布(强调位置)，柱状图比较数据的大小。
            2. 直方图X轴为定量数据，柱状图X轴为分类数据。
            3. 直方图柱子无间隔(连在一起)，柱状图柱子有间隔(不练在一起)
            4. 直方图柱子宽度(组距)可不一，柱状图柱子宽度须一致
            
            
        2.5.3 直方图绘制
            API:
            plt.hist(x, bins=None, normed=None, **kwargs)
            绘制直方图
            x: x轴,
            bins: 组数
            normed: 是否显示频率(就是概率), 如果是False, 则显示频数
                    不过这个参数已经过时了.
            
            组距自己选择 
            x = time
            bins 组数 = (max(time) - min(time)) // 组距
        3 直方图注意点
            # 组距会影响直方图呈现出来的数据分布, 因此在绘制直方图的时候需要多次尝试改变组距
            # 注意Y轴所代表的变量
    
    2.6 饼图(pie)
        API:
        plt.pie(x, labels=, autopct=, colors)
            参数:
                x: 数据, 自动计算百分比
                labels: x对应的名称
                autopct: 占比显示指定 %1.2f%%,  %1.2表示格式化输出 %% 表示%(转义字符)
                colors: 每部分对应的颜色
        # 添加axis:
        plt.axis('equal') # 使横轴和纵轴比例相同
        使用饼图的时候, 类别不建议超过9个, 可以使用柱状图

        print("%1.2f%%")





总结:




"""
