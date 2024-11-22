# coding:utf-8
# 解析几何、直线


import run
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt


@run.change_dir
def main():
    # shapely直线操作
    point = Point(0.5, 0.5)
    line = LineString([(0, 0), (1, 1)])
    print(f"点是否在线上:{line.contains(point)}")
    print(f"线的长度:{line.length}")
    # 画图
    # 定义起始点
    x = [0, 10]
    y = [0, 10]
    plt.figure()
    plt.plot(x, y, label = "直线")
    plt.savefig("./output/line.png")
    plt.close()
    
    
    
if __name__ == "__main__":
    main()