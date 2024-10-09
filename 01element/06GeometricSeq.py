# coding:utf-8


# 几何数列(等比数列)

import run
import matplotlib.pyplot as plt
import numpy as np


@run.change_dir
def main():
    # 生成几何数列
    # 方法1
    x = np.geomspace(1, 1024, 11)
    print(x, np.sum(x), geosum(1, 2, 10))
    # 方法2
    y = np.logspace(0.0, 10.0, num = 11, base = 2.0)
    print(y, np.sum(y), geosum(1, 2, 10))
    
    # 测试r = 1的情况
    z = np.geomspace(1, 1, 11)
    print(z, np.sum(z), geosum(1, 1, 10))
    
    # 画图
    n = np.linspace(1, 11, 11)
    print(n)
    plt.plot(n, x)
    plt.savefig("./output/geoseq.png")
    
    
# 用通用公式求几何数列的和
def geosum(a, r, n):
    if r == 1:
        return a*(n+1)
    else:
        return a/(r-1)*(r**(n+1) - 1)
    
    
    
if __name__ == "__main__":
    main()