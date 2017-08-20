# -*- coding: utf-8 -*-
import numpy
import pandas

data = pandas.read_csv('E:\\Python\\Test\\df5.csv')
data
#设置随机种子
numpy.random.seed(seed=2)
#按照个数抽样
data.sample(n=10)
#按照百分比抽样
data.sample(frac=0.2)
#是否可放回抽样
#replace=True,可放回
#replace=False,不可放回
data.sample(n=10,replace=True)
#典型抽样，分层抽样
gbr = data.groupby("class")
gbr.groups

typicalNDict = {
        1:2,#-1班中2个人
        2:4,
        3:6
}
#p1-分组， p2-分组定义
def typicalSampling(group, typicalNDict):
    name = group.name
    n = typicalNDict[name]
    return group.sample(n=n)
result = data.groupby(
        'class', group_keys=False
        ).apply(typicalSampling, typicalNDict)

#分组后按百分比随机抽取
typicalNDict = {
        1:0.5,
        2:0.5,
        3:0.5
}
def typicalSampling(group, typicalFracDict):
    name = group.name
    frac = typicalFracDict[name]
    return group.sample(frac=frac)
result = data.groupby(
        'class', group_keys=False
        ).apply(typicalSampling, typicalNDict)

