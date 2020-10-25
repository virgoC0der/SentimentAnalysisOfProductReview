# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    sns.set(font='SimHei', style='white', )  # 解决Seaborn中文显示问题

    # 取出作图的数据
    y1 = [4088, 2451, 3896, 2921, 3116, 3189, 2697, 1380] # 发病数
    y2 = [30, 15, 20, 24, 20, 16, 6, 4]   #死亡数
    x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

    # 设置图形大小
    plt.rcParams['figure.figsize'] = (12.0, 8.0)
    fig = plt.figure()


    # 画柱形图
    ax1 = fig.add_subplot(111)
    ax1.set_ylim([0, 4500])
    ax1.bar(x, y1, alpha=0.7, color='k')
    ax1.set_ylabel(u'发病数', fontsize='20')
    # ax1.set_xlabel(u'年份', fontsize='20')
    ax1.tick_params(labelsize=15)
    for i, (_x, _y) in enumerate(zip(x, y1)):
        plt.text(_x, _y, y1[i], color='black', fontsize=20, ha='center', va='bottom')  # 将数值显示在图形上
    # ax1.set_title(u"2011-2018年中国疟疾发病数与死亡数", fontsize='20')


    # 画折线图
    ax2 = ax1.twinx()  # 组合图必须加这个
    ax2.set_ylim([0, 35])
    ax2.plot(x, y2, 'r', ms=10, lw=3, marker='o') # 设置线粗细，节点样式
    ax2.set_ylabel(u'死亡数', fontsize='20')
    sns.despine(left=True, bottom=True)   # 删除坐标轴，默认删除右上
    ax2.tick_params(labelsize=15)
    for x, y in zip(x, y2):   # # 添加数据标签
        plt.text(x, y-2.5, str(y), ha='center', va='bottom', fontsize=20, rotation=0)

    # plt.savefig(r'F:\学习文档\20190723 数据可视化\1.png', dpi=1000, bbox_inches='tight')
    plt.show()