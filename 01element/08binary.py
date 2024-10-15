# coding:utf-8

# 进制转换

import math


def main():
    x = int("1234567")
    print(x)
    y = int("1101011", base = 2)
    print(y)
    z = bin(x)
    print(z)
    z2 = bin(54215)
    print(z2)
    z3 = 0b1100110
    z4 = 0b1101
    sum = bin(z3 + z4)
    print(sum)
    print(bin(z3 - z4))
    print(bin(z3 * z4))
    print(bin(z3 // z4))


if __name__ == "__main__":
    main()