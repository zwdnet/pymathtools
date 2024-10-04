# coding:utf-8
# 基本算术 分数运算

import run
from fractions import Fraction


def main():
    print(Fraction(16, -10))
    print(Fraction(123))
    print(Fraction('3/7'))
    print(Fraction('333/111'))
    print(Fraction('3.1415926'))
    print(Fraction('-0.125'))
    print(Fraction('1.1'))
    print(Fraction(1.1))
    ## print("{.40g}".format(Fraction(1, 7)))
    print(Fraction('1/4') + Fraction('1/3'))
    print(Fraction('1/4') - Fraction('1/3'))
    print(Fraction('1/4') * Fraction('1/3'))
    print(Fraction('1/4') / Fraction('1/3'))


if __name__ == "__main__":
    main()