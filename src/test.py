import pandas as pd

columns = ['Код', 'Название', 'url']

a = ['a','b','c']
b = ['1','2','3']
c = []

e = [a,b,b,b,b,c]

df = pd.DataFrame(e,columns=columns)

#print(df)
kk = df.ix[1:,:].drop(df.tail(1).index)

print(kk)

kkk = pd.concat([kk,kk,kk])

plot_data = [['k']] * 3

plot_data.append(['2'])
print(plot_data)
ff = plot_data
print(kkk)
print(kkk[1:-1])

aaa = ['f','f','f']
vvv = [a]+[b]
#vvv = vvv.append(vvv)

print(vvv)

ddd = vvv+[b]
ddd += [a]
print(ddd)

ddd += vvv
ddd += [b]
print(ddd)
print([x[1] for x in ddd])
