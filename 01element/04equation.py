# coding:utf-8


# 方程及其图像

from sympy import *
import run
import matplotlib.pyplot as plt
import numpy as np


# 定义方程
def equation(x):
    return 2*x + 1
    

def equation2(x):
    return x - 1


@run.change_dir
def main():
    # 解方程
    x = symbols('x')
    y = symbols('y')
    res = solve(0.6*x-1.5, x)
    print(res)
    res = solve([4*x-3*y+6, 4*x-2*y+4], [x, y])
    print(res)
    res = solve([x+y-10, x-y-5], [x, y])
    print(res)
    # 画函数图像
    x = np.linspace(-10, 10, 100)
    y = equation(x)
    plt.plot(x, y)
    y2 = equation2(x)
    plt.plot(x, y2)
    plt.savefig("./output/equfig.png")
    


if __name__ == "__main__":
    main()