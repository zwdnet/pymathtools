# coding:utf-8

# 三角学
# 参考https://docs.pingcode.com/baike/932425


import math
import run
import numpy as np
import matplotlib.pyplot as plt


@run.change_dir
def main():
    # 基本三角函数
    angle = math.radians(22.5)
    print("角度为22.5°")
    print("sin:", math.sin(angle))
    print("cos:", math.cos(angle))
    print("tan:", math.tan(angle))
    print("cot:", 1.0/math.tan(angle))
    print("sec:", 1.0/math.cos(angle))
    print("csc:", 1.0/math.sin(angle))
    
    # 反三角函数
    value = 0.3826834323650898
    print("三角函数值为:", value)
    print("asin:", math.degrees(math.asin(value)))
    print("acos:", math.degrees(math.acos(math.sqrt(1 - value**2))))
    print("atan:", math.degrees(math.atan(value/math.sqrt(1 - value**2))))
    print("acot:", 90-math.degrees(math.atan(math.sqrt(1 - value**2)/value)))
    
    # 三角恒等式
    print(math.sin(angle)**2 + math.cos(angle)**2)
    print(math.sin(2*angle), 2*math.sin(angle)*math.cos(angle))
    
    # 双曲三角函数
    print("角度为22.5°")
    print("sinh:", math.sinh(angle))
    print("cosh:", math.cosh(angle))
    print("tanh:", math.tanh(angle))
    
    # 画正弦函数
    t = np.linspace(0, 1, 500)
    freq = 5
    signal = np.sin(2 * np.pi * freq * t)
    plt.plot(t, signal)
    plt.savefig("./output/sin.png")
    plt.close()
    
    
    
if __name__ == "__main__":
    main()