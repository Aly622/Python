# -*- coding: utf-8 -27*-
import numpy
import pandas

data = pandas.read_csv('E:\\Python\\Test\\df8.csv', encoding='utf8')
data.value.describe()
data.value.size
data.value.max()
data.value.min()
data.value.sum()
data.value.mean()
data.value.var()
data.value.std()

#累计求和
data.value.cumsum()

#求最大值和最小值所在位置
data.value.argmin()
data.value.argmax()

data.value.quantile(0.3, interpolation="nearest")

# ...28
data = pandas.read_csv('E:\\Python\\Test\\df8.csv', encoding='utf8')
aggResult = data.groupby(
                by = ['date'])['value'].agg(
                        {
                                '总分':numpy.sum,
                                '人数':numpy.size,
                                '平均值':numpy.mean
                                })

#...29
data = pandas.read_csv('E:\\Python\\Test\\df10.csv', encoding='utf8')
aggResult = data.groupby(
                by = ['年龄'])['年龄'].agg(
                        { '人数':numpy.size
                                })

bins = [
        min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1]
labels=[
        '20岁以及以下','21~30岁','31~40岁','41岁以上']
data['年龄分层'] = pandas.cut(data.年龄, bins, labels=labels)

aggResult = data.groupby(
                by = ['年龄分层'])['年龄'].agg(
                        { '人数':numpy.size
                                })
pAggResult = round(
                aggResult/aggResult.sum(), 5)*100
pAggResult['人数'].map('{:,.2f}%'.format)