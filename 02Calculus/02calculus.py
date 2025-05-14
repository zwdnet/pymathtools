# coding:utf-8

# 微积分运算


import run
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import scipy


# 数列的极限
def fun1():
    n = np.arange(1, 41)
    recp = 1/n
    xn = 1 - recp
    err_xn = recp
    
    yn = np.sin(n)/n
    err_yn = abs(yn)
    
    zn = np.log(n)/n
    err_zn = abs(zn)
    
    En = (1+recp)**n
    err_En = abs(En - np.e)
    
    plt.plot(n, err_xn, 'o-', ms = 3)
    plt.plot(n, err_yn, 'o--', ms = 3)
    plt.plot(n, err_zn, 'o-.', ms = 3)
    plt.plot(n, err_En, 'o:', ms = 3)
    
    plt.xlim(0, 40)
    plt.ylim(0, 0.4)
    plt.xlabel(r'$n$')
    plt.ylabel('|Error|')
    plt.legend([r'$|x_n-1|$', r'$|y_n|$', r'$|z_n|$', r'$|E_n-e|$'])
    plt.grid('on')
    plt.savefig("./output/limit.png")
    
    
# 符号运算
def fun2():
    x = Symbol('x')
    y = Symbol('y')
    y = x**5
    print(y)
    print(y.diff(x)) # 求微分
    print("二阶导数:", diff(x**3, x, 2))
    print(y.integrate(x)) # 求积分
    print("定积分:", integrate(y, (x, 0, 1)))
    print(y.limit(x, 5)) # 求极限
    y = x*cos(x)
    print(y)
    print(y.diff(x))
    print(y.integrate(x))
    
    
# 半圆方程
def half_circle(x):
    return (1-x**2)**0.5
    

# 半球方程
def half_sphere(x, y):
    return (1-x**2-y**2)**0.5


# 数值微积分
def fun3():
    # 数值微分
    x = symbols('x', real=True)
    h = symbols('h', positive=True)
    f = symbols('f', cls=Function)
    f_diff = f(x).diff(x, 1)
    print(f_diff)
    expr_diff = Derivative.as_finite_difference(f_diff, [x, x-h, x-2*h, x-3*h])
    print(expr_diff)
    sym_dexpr = f_diff.subs(f(x), x*exp(-x**2)).doit()
    print(sym_dexpr)
    sym_dfunc = lambdify([x], sym_dexpr, modules="numpy")
    print(sym_dfunc(np.array([-1, 0, 1])))
    
    # 数值积分
    # 矩形方法
    N = 10000
    x = np.linspace(-1, 1, N)
    dx = x[1] - x[0]
    y = half_circle(x)
    S = dx*np.sum(y)
    print("矩形法:", S)
    # 梯形法
    S2 = np.trapz(y, x)
    print("梯形法:", S2)
    # quad
    pi_half, err = scipy.integrate.quad(half_circle, -1, 1)
    print("quad法:", pi_half)
    #simpson法
    pi_half = scipy.integrate.simpson(y, x=x)
    print("simpson法:", pi_half)
    
    # 二重积分
    volume, error = scipy.integrate.dblquad(half_sphere, -1, 1, lambda x:-half_circle(x), lambda x:half_circle(x))
    print("二重积分:", volume)
    

@run.change_dir
def main():
    fun1()
    fun2()
    fun3()
    
    
if __name__ == "__main__":
    main()