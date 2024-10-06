# coding:utf-8


# 一元二次方程及其图像


from sympy import *
import run
import matplotlib.pyplot as plt
import numpy as np


# 定义方程
def equation(x):
    return x**2 +2*x - 3
    

def equation2(x):
    return x**2 +2*x + 1
    
    
def equation3(x):
    return x**2 +2*x + 2


@run.change_dir
def main():
    # 解方程
    x = symbols('x')
    y = symbols('y')
    res = solve(-2*x**2 + 5*x + 4)
    print(res)
    res = solve(-16*x**2 + 80*x -120)
    print(res)
    # 画函数图像
    x = np.linspace(-4, 2, 100)
    y = equation(x)
    plt.plot(x, y)
    y2 = equation2(x)
    plt.plot(x, y2)
    y3 = equation3(x)
    plt.plot(x, y3)
    plt.savefig("./output/quadraticfig.png")
    


if __name__ == "__main__":
    main()