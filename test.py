from pandas import Series
x=Series(['a',True,1], 
         index=['first','second','third'])
x
x[1]
x['second']
n=Series(['2'])
#需要使用一个变量来承载变化，因为系列修改返回的是新的系列
x
x=x.append(n)
x

'2' in x.values
#切片 大于等于-小于
x[1:3]
#定位获取
x[[0,2,1]]
#删除
x.drop(0)
x.drop('first')
#根据位置删除
x.drop(x.index[3])
#根据值删除
x=Series(['2',True,2], 
         index=['first','second','third'])
x.drop('2'!=x.values) 
