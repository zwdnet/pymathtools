# coding:utf-8

# 画参数方程的图像


import run
import matplotlib.pyplot as plt
import numpy as np


@run.change_dir
def main():
    # 定义摆线的参数方程
    t = np.linspace(0, 4.0*np.pi, 1000)
    x = t - np.sin(t)
    y = 1 - np.cos(t)
    # 画图
    fig, ax = plt.subplots()
    ax.plot(x, y, label = "x")
    plt.savefig("./output/bailine.png")
    
    
if __name__ == "__main__":
    main()