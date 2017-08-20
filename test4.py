# -*- coding: utf-8 -*-
from pandas import read_csv
df = read_csv('E:\\Python\\Test\\df2.csv')
df
#找出行重复的位置
dIndex = df.duplicated()
#根据某些列，找出重复的位置
dIndex = df.duplicated('id')
dIndex = df.duplicated(['id', 'age'])

#根据返回值，把重复数据提取出来
df[dIndex]

#直接删除重复值
#默认根据所有的列，进行删除
newDF = df.drop_duplicates()
newDF
#也可以指定某一列，进行重复值处理
newDF = df.drop_duplicates('id')
newDF

#指定某个值为缺失值
df = read_csv('E:\\Python\\Test\\df2.csv',
              na_values=['ken','jimi'])
df
#找出空值的位置
isNA = df.isnull()
#获取出空值所在的行
df[isNA.any(axis=1)]
df[isNA[['age']].any(axis=1)]
df[isNA[['age', 'name']].any(axis=1)]
#将空值进行填充
df.fillna('21.0')

#直接删除空值
newDF = df.dropna()
#清除空格值
newName = df['id'].str.lstrip()
newName = df['id'].str.rstrip()
newName = df['id'].str.strip()
df['id'] = newName
