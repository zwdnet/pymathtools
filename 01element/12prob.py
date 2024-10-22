# coding:utf-8

# 概率问题


import random


"""
三个盒子，第一个有两个红球，第二个有一红一黑两个球，第三个有两个黑球。随机从三个盒子中的一个里抓一个是红球，问再从该盒子里抓一个，还是红球的概率。
"""
def simulate(n):
    nr = 0
    for i in range(n):
        res = experiment()
        if res == True:
            nr += 1
            
    return float(nr/n)
        
    
    
# 进行一次实验
def experiment():
    # 三个盒子里的球分别为红红、红黑和黑黑
    while True:
        box = random.randint(1,3)
        while box == 3: ## 摸到三盒，没红球，直接重来。
            box = random.randint(1,3)
        if box == 1:
            return True ## 摸到一盒，全是红球，实验成功，退出。
        elif box == 2:
            ball = random.randint(1,2)
            if ball == 2:
                continue
            elif ball == 1:
                return False ## 摸到二盒，一红一黑，先摸到黑球，不符合，重来，不计入。先摸到红球，第二次肯定摸黑球，实验失败。


def main():
    n = 1000000
    res = simulate(n)
    print("所求概率为:", res)
    
    
if __name__ == "__main__":
    main()