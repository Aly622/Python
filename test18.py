# -*- coding: utf-8 -*-
import numpy
import pandas
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
#设置不在交互式命令行绘图，在弹出新的窗口进行绘图
data = pandas.read_csv('E:\\Python\\Test\\df15.csv', encoding='utf8')

result = data.groupby(
            by=['渠道数'],
            as_index=False
        )['渠道数'].agg({'购买用户数':numpy.sum})
#设置长宽分辨率
plt.figure(figsize=(30,30), dpi=80)

#使用绝对路径获取字体的名称的方法
fontProp = font_manager.FontProperties(
            fname="C:\\Windows\\Fonts\\FZSTK.TTF"
        )
#设置字体 
# 1表示透明度
mainColor = (42/256,87/256,141/256,1)
#设置字体 默认是英文为了避免乱码要先设置中文
font = {
        'family' : 'SimHei',
        'size'   : 5
        }
matplotlib.rc('font', **font)

#设置为横轴和纵轴等长的饼图
#也就是图形的饼图，而非椭圆形的饼图
plt.axis('equal')
plt.pie(
        result['购买用户数'],
        labels=result['渠道数'],
        autopct='%.2f%%'
        )
#设置突出部分
explode = (0.1,0.2,0.3)
plt.axis('equal')
plt.pie(
        result['购买用户数'],
        labels=result['渠道数'],
        autopct='%.2f%%'
        )
 