# -*- coding: utf-8 -*-
import pandas
from pandas import read_csv
from pandas import DataFrame 

data1 = DataFrame(
	data={
	       'age':[21,22,23],
           'id':[21,22,23],
           'name':['ken','john','jimi']	
        })

data2 = DataFrame(
	data={
	       'age':[1,2,4],
           'id':[21,22,23],
           'name':['ken','john','jimi']	
        })

data3 = DataFrame(
	data={
	       'age':[2,4,5],
           'id':[21,22,23],
           'name':['ken','john','jimi']	
        })

data = pandas.concat([data1,data2,data3])

dt = pandas.concat([data1[['age','id']],data2[['age','name']],data3[['name','id']]])

data1 = data1.astype(str)
total = data1['age'] + data1['id'] + data1['name']

data1['name'] = total