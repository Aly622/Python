# -*- coding: utf-8 -*-
import pandas
import matplotlib
import matplotlib.pyplot as plt
# 1表示透明度
mainColor = (42/256,87/256,141/256,1)

#设置字体 默认是英文为了避免乱码要先设置中文
font = {
        'family' : 'SimHei',
        'size'   : 20
        }
matplotlib.rc('font', **font)

data = pandas.read_csv('E:\\Python\\Test\\df15.csv', encoding='utf8')
#对日期格式进行转换
data['购买日期'] = pandas.to_datetime(data['日期'])
#%matplotlib qt
#plt.grid(True)
#设置线条粗细
plt.xlabel('购买日期', color=mainColor)
plt.ylabel('购买用户数', color=mainColor)
plt.tick_params(axis='x', colors=mainColor)
plt.tick_params(axis='y', colors=mainColor)
plt.plot(
        data['购买日期'],
        data['购买用户数'],
        '-',color=mainColor,
        lineWidth=10
        )
plt.title('购买用户数')
plt.show()
#--虚线 -.线加点  :由点组成的曲线  .散点图 