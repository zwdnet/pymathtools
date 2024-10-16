# coding:utf-8

# 集合与计数

import itertools
import math


def main():
    # 定义集合
    S = {1,2,3,3,4,5,6,7,8,9}
    A = {1,2,3,4}
    B = {3,4,5,6}
    # 定义空集 
    N = set()
    print(S, A, B, N)
    # 判断元素是否在集合内
    print(20 in S)
    print(8 in S)
    # 集合运算
    print(B - A)
    print(A | B) # 并集
    print(A & B) # 交集
    print(A ^ B) # 不同时包含于AB
    # 集合个数
    print(len(S))
    # 判断是否为子集
    print(A.issubset(S))
    
    # 排列组合
    # 集合的笛卡尔集
    print("笛卡尔集")
    for each in itertools.product(A, repeat = 2):
        print(each)
    
    # 排列
    print("排列")
    for each in itertools.permutations(A, 2):
        print(each)
    
    # 组合
    print("组合")
    for each in itertools.combinations(A, 2):
        print(each)
        
    # 计算排列组合数
    # 排列数
    print(math.perm(4, 2))
    # 组合数
    print(math.comb(4, 2))


if __name__ == "__main__":
    main()