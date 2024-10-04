# coding:utf-8

# 数论

import sympy as sp
from fractions import Fraction


def main():
    print(sp.isprime(1984))
    print(sp.isprime(29))
    # 因式分解
    print(sp.factorint(9992))
    print(sp.factorint(28))
    # 最大公约数
    print(sp.gcd(2279, 4687))
    # 分数小数互转
    print(Fraction(0.3542))
    print(sp.Rational(0.3542))
    # 循环小数
    print(Fraction(0.3333).limit_denominator())
    print(sp.Rational(0.3333).limit_denominator())
    # 分数
    print(float(Fraction(112, 354)))
    
    
    
if __name__ == "__main__":
    main()