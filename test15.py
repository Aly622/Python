# -*- coding: utf-8 -*-
import pandas
import matplotlib
import matplotlib.pyplot as plt

mainColor = (42/256,87/256,141/256,1)
#设置字体 默认是英文为了避免乱码要先设置中文
font = {
        'family' : 'SimHei',
        'size'   : 20
        }
matplotlib.rc('font', **font)

data = pandas.read_csv('E:\\Python\\Test\\df14.csv', encoding='utf8')
# 设置图形格式及尺寸
fig = plt.figure(
        figsize = (30,20),
        dpi = 80
        )
#111把图形分为一行一列 并且当前使用一个字图的意思
sp = fig.add_subplot(111)
#设置坐标范围
sp.set_xlim([
        0,
        data.GDP.max()*1.1
        ])
sp.set_ylim([
        0,
        data.population.max()*1.1
        ])
#关闭坐标轴，坐标轴的刻度
sp.get_xaxis().set_ticks([])
sp.get_yaxis().set_ticks([])
#画点
sp.scatter(
        data.GDP, data.population,
        alpha=0.5, s = 200, marker = "o",
        edgecolors=mainColor, linewidths = 5
        )

#画均值线
sp.axvline(
        x=data.GDP.mean(),
        linewidth = 1, color = mainColor
        )
sp.axhline(
        y=data.population.mean(),
        linewidth = 1, color = mainColor
        )
sp.axvline(
        x=0,
        linewidth = 3, color = mainColor
        )
sp.axhline(
        y=0,
        linewidth=3, color = mainColor
        )
sp.set_xlabel('GDP')
sp.set_ylabel('人口')
#画标签
data.apply(
        lambda row: plt.text(
                    row.GDP,
                    row.population,
                    row.province,
                    fontsize = 10
                ),
        axis = 1
        )

plt.show()