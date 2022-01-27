import matplotlib.pyplot as plt
import pandas as pd

def matplotlib_demo():
    """
    简单演示matplotlib
    :return: None
    """
    plt.figure(figsize=(20, 8), dpi=100)
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()

    return None

def read_csv_demo():
    """
    简单演示读取数据
    :return: None
    """
    stock_day = pd.read_csv("./stock_day/stock_day.csv")

    print(stock_day)
    return None


if __name__ == "__main__":
    # 代码1：简单演示matplotlib
    matplotlib_demo()
    # 代码2：简单演示读取数据
    read_csv_demo()