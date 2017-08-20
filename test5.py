# -*- coding: utf-8 -*-
from pandas import read_csv
df = read_csv('E:\\Python\\Test\\df3.csv')
df
df['tel'] = df['tel'].astype(str)

#运营商
bands = df['tel'].str.slice(0,3)
#地区
areas = df['tel'].str.slice(3,7)
#号码段
nums = df['tel'].str.slice(7,11)
#赋值回去
df['bands'] = bands
df['areas'] = areas
df['nums'] = nums
df.to_csv("E:\\Python\\Test\\df4.csv")

#字段拆分
df = read_csv('E:\\Python\\Test\\df4.csv')
df['tel'] = df['tel'].astype(str)
newDF = df['tel'].str.split('0',3, True)
newDF.columns = ['band','name']