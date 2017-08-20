
from pandas import read_csv
df = read_csv('E:\\Python\\Test\\df1.csv')
df

from pandas import read_table
df = read_table('E:\\Python\\Test\\df.txt')
df

df = read_table('E:\\Python\\Test\\df1.txt',
     	names=['age','name'],
	sep=',')
df

from pandas import read_table
filePath = 'D://PDA//4.1/中文.txt'
df = read_table(
	filePath,
	sep=',',
	encoding='UTF-8'
)
df
#中文路径的问题 可以通过使用engine处理
df = read_table(
	filePath,
	sep=',',
	encoding='UTF-8',
	engine='python'
)
df


from pandas import read_excel
df = read_excel('D://PDA//4.1//3.xlsx',sheetname = 'data')
df

from pandas import DataFrame
df = DataFrame(
	data={
	       'age':[21,22,23],
               'name':['ken','john','jimi']	
        },
        index=['first','second','third'])
df.to_csv("E:\\Python\\Test\\df.csv")
df.to_csv("E:\\Python\\Test\\df1.csv", index=False)