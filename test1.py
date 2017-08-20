from pandas import DataFrame 

df = DataFrame(
	data={
	       'age':[21,22,23],
           'name':['ken','john','jimi']	
        },
    index=['first','second','third'])
df
#按列访问
df['age']
df[['age','name']]
#按行访问
df[1:2]
#按行索引访问
df.loc[['first','second']]
#按行列号访问
df.iloc[0:2,0:1]
#按行索引，列名访问
df.at['first','name']
#修改列名
df.columns
df.columns=['age2','name2']
#修改行索引
df.index
df.index=range(1,4)
df.index
#根据行索引删除 默认参数axis为0,0表示行
#根据列名删除
df.drop('first',axis=0)
df
df.drop('age2',axis=1)
df
#增加行，这种方法效率非常低，不应该用于遍历中
df.loc[len(df)]=[24,'kenken']
#增加列
df['newCol'] = [2,4,6]
df