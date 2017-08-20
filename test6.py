# -*- coding: utf-8 -*-
from pandas import read_csv
df = read_csv('E:\\Python\\Test\\df4.csv')
df
#单条件
df[df.comments>10000]
#多条件
df[df.comments.between(1000,10000)]
#过滤空值所在行
df[pandas.isnull(df.title)]
#根据关键字过滤
df[df.title.str.contains('台电', na=False)]
#~取反
df[~df.title.str.contains('台电', na=False)]
#组合逻辑条件
df[(df.comments>1000)&(df.comments<=100000)]
