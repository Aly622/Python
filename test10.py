# -*- coding: utf-8 -*-25
import pandas

data = pandas.read_csv('E:\\Python\\Test\\df8.csv', encoding='utf8')

dateparse = lambda dates: pandas.datetime.strptime(dates, '%Y%m%d')

data = pandas.read_csv('E:\\Python\\Test\\df8.csv', 
                       encoding='utf8',
                       parse_dates=['date'],
                       date_parser=dateparse,
                       index_col='date')

#根据索引进行抽取
import datetime

dt1 = datetime.date(year=2015, month=1, day=2);
dt2 = datetime.date(year=2016, month=1, day=2);

data.ix[dt1:dt2]
data.ix[[dt1, dt2]]

#根据时间列进行抽取
data = pandas.read_csv('E:\\Python\\Test\\df8.csv', 
                       encoding='utf8', 
                       parse_dates=['date'],
                       date_parser=dateparse)
data[(data.date>=dt1) & (data.date<=dt2)]

#--26 虚拟变量
import pandas

data = pandas.read_csv('E:\\Python\\Test\\df9.csv', encoding='utf8')
data['Education level'].drop_duplicates()
educationLevelDict = {
        'Post-Doc':9,
        'Doctorate':8,
        'Master`s Degree':7,
        'Bachelor`s Degree':6,
        'Associate`s Degree':5,
        'Some College':4,
        'Trade School':3,
        'High School':2,
        'Grade School':1
        }
data['Education level Map'] = data[
        'Education level'
        ].map(educationLevelDict)
data['Gender'].drop_duplicates()
dummies = pandas.get_dummies(
        data,
        columns=['Gender'],
        prefix=['Gender'],
        prefix_sep="_",
        dummy_na=False,
        drop_first=False)
dummies['Gender'] = data['Gender']