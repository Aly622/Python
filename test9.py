# -*- coding: utf-8 -*-23
import pandas

data = pandas.read_csv('E:\\Python\\Test\\df7.csv', sep = ',')
bins = [min(data.cost)-1, 20, 40, 60, 80, 100, max(data.cost)+1]
data['cut'] = pandas.cut(data.cost, bins)
data['cut'] = pandas.cut(data.cost, bins, right=False)
labels = ['20以下','20-40','40-60','60-80','80以上']
data['cut'] = pandas.cut(data.cost, bins, right=False, labels=labels)

#-24
import pandas
data = pandas.read_csv('E:\\Python\\Test\\df6.csv', encoding='utf8')
data['时间'] = pandas.to_datetime(data.注册时间, format='%Y/%m/%d')

data['时间-年'] = data['时间'].dt.year
data['时间-月'] = data['时间'].dt.month
data['时间-周'] = data['时间'].dt.weekday
data['时间-日'] = data['时间'].dt.day
data['时间-时'] = data['时间'].dt.hour
data['时间-分'] = data['时间'].dt.minute
data['时间-秒'] = data['时间'].dt.second