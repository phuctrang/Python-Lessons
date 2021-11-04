import pandas as pd
# # series
# data = pd.Series([1.2 , 1.3, 1.4, 1.5])
# print(data)
# print(data.index)
# print(data.values)
# print(data[1])
# print(data[2:4])

# mang np chuyen qua pandas
import numpy as np
# x = np.array([11,12,14,17])
# S = pd.Series(x)
# print(S)
# # thay doi chi so trong mang Series
# S = pd.Series([1.2 , 1.3, 1.4, 1.5], index=['a', 'b', 30, 'd'])
# print(S)
# print(S)
# # tuple
# s = pd.Series({'a': 100, 'c': 300, 'd': 400})
# print(s)
"""
# dataframe: nhu mang trong numpy
danso = {'fox': 200, 'tesxa': 300, 'cali': 500}
population = pd.Series(danso)
print("dan so\n", population)

dientich = {'fox': 2000000, 'tesxa': 1500000, 'cali': 50000000}
Area = pd.Series(dientich)
print("dien tich\n",Area)
# ghep mang :)) vi no cung chi so (INDEX)
states = pd.DataFrame({'population': population, 'area': Area})
print(states)
print(states.index)
print(states.columns)
print(states['population'])
# moi cot cua bang la kieu series
temp = states['area']
print(type(temp))

S = pd.Series(['a' , 'b', 'c'], index=[1, 3, 5])
print(S[1], S[3])
# laay chi so 1 toi chi so 3-1
print(S[1:3])
#########################suy ra sinh ra ham   location va index location
# nhap vao cac index da khai bao
print(S.loc[1])
# gia tri index trong khoang 1 den 10 ( lay het cac index 1,3,5 vi 10>5)
print(S.loc[1:10])
# vitri chi so that su: giong java, android
print(S.iloc[0])
print(S.iloc[0:10])

##############################################################
danso = {'fox': 200, 'tesxa': 300, 'cali': 500}
population = pd.Series(danso)
print("dan so\n", population)

dientich = {'fox': 2000000, 'tesxa': 1500000, 'cali': 50000000}
Area = pd.Series(dientich)
print("dien tich\n",Area)
# ghep mang :)) vi no cung chi so (INDEX)
states = pd.DataFrame({'population': population, 'area': Area})
print("states:::::::::::::::")
print(states)
# cham ten index
print(states.area)

# them 1 truong
states['density'] = states['population'] / states['area']
print(states)
states['density'] = 0
print(states)
states['density'] = states['population'] / states['area']
print(states)
###########   lay du lieu cot thu 0 : no giong nu ma tran
print(states.values[0])
# no giong nu ma tran   vidu: dong 0 cot 1  OKOKOKOKOKOKKKKKKKKKKKKK
print(states.values[0,1])
# loc/iloc
# lay dong dau tien  2 cach viet
print(states.iloc[0])
print(states.loc['fox'])
##### cot dau tien A[start:stop:step]
print(states.iloc[:])
#buoc nhay la 2
print(states.iloc[::2])
print("cot dau tien: \n",states.iloc[:,0])
#################################### loc data
print(states.loc[states['density']>0.00015])

## thay doi gia tri ma tran
states.iloc[2,1] = 0
print(states)

"""
"""
phep toán trong pandas - giong nhu trên numpy
#mang 1 chieu
ser = pd.Series(np.random.randint(0,10,4))
print(ser)
#matran
df = pd.DataFrame(np.random.randint(0,10,(3,4)))
print(df)
print(np.sin(ser))
print(np.sin(df))
"""
# giống hàng chỉ số
# neu chi so cua 2 seri ko giông nhau ?


danso = {'fox': 200, 'tesxa': 300, 'cali': 500}
population = pd.Series(danso)
# print("dan so\n", population)

dientich = {'fox': 2000000, 'tesxa': 1500000, 'new york': 50000000}
Area = pd.Series(dientich)
# print("dien tich\n",Area)
# ghep mang :)) vi no cung chi so (INDEX)
states = pd.DataFrame({'population': population, 'area': Area})
# print("states:::::::::::::::")
################# vi khong giong nhau ve index nen sinh ra NaN

density = population/Area
print(density)
print(density.index)
# lap tat ca cac Nan =  0
den = population.div(Area, fill_value=0)
print("den: \n", den)


df1 = pd.DataFrame(np.random.randint(0, 20, (2, 2)),
columns=list('AB'))
df2 = pd.DataFrame(np.random.randint(0, 10, (3, 3)),
columns=list('BAC'))
print("df1", df1)
print("df1", df2)
print(df1+df2)
# cong:  seri nao bằng NaN thì gán = 1
tong = df1.add(df2,fill_value=1)
print(tong)
































