# coding:utf-8
# 不等式

from sympy import symbols, solve, Abs
import run
import math


@run.change_dir
def main():
    x = symbols('x')
    inequality = x - 5 > 0
    solution = solve(inequality, x)
    print(solution)
    inequality = Abs(x-3) < 0.5
    solution = solve(inequality, x)
    print(solution)


if __name__ == "__main__":
    main()