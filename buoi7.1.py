# phep toan giua dataframe va series
import numpy as np
import pandas as pd
"""
# A = np.random.randint(10, size=(3,4))
# print(A)
# df = pd.DataFrame(A, columns=list('QRST'))
# print("data: ", df)
# #tru theo hang
# dfiloc = df - df.iloc[0]
# print(dfiloc)
# # tru theo cot
# tru = df.subtract(df['R'], axis=0)
# print(tru)
#
# ##### NaN lay lan (virrus)
# val2 = np.array([1, np.nan, 3, 4])
# print("val2", val2)
# print("cong: ", val2+1)
# print("tong: ", val2.sum())
# ###### xử lý Nan ########## Bỏ qua NaN :)))
# print(np.nansum(val2))
# #### trong pandas / ko cần xử lý Nan :v
# pd1 = pd.Series([1, np.nan, 2, None])
# print(pd1)
# print(pd.isnull(pd1))
# print(pd.notnull(pd1))
# print(pd1.dropna())

############################################# nối dữ liệu
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
ghep = np.concatenate([x, y, z])
print("theo numpy: \n", ghep)

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
ghep1 = pd.concat([ser1, ser2])
print("theo pandas: \n", ghep1)

data = [['A1', 'B1'],['A2', 'B2']]
df1 = pd.DataFrame(data, columns=('A', 'B'),index=[1, 2])
data = [['A3', 'B3'],['A4', 'B4']]
df2 = pd.DataFrame(data, columns=('A', 'B'),index=[3, 4])
print(df1)
print(df2)
print(pd.concat([df1, df2]))
########### bảo toàn chỉ số
data = [['A1', 'B1'],['A2', 'B2']]
df1 = pd.DataFrame(data, columns=('A', 'B'),index=[1, 2])
data = [['A3', 'B3'],['A4', 'B4']]
df2 = pd.DataFrame(data, columns=('A', 'B'),index=[1, 2])
print(df1)
print(df2)
print("bảo toàn chỉ số\n", pd.concat([df1, df2]))
###########  verify_integrity=True
##############  ignore_index :  Tạo chỉ số mới 0,1,2,3,4,5,6,7...
pd2 = pd.concat([df1, df2], ignore_index=True)
print("Tạo chỉ số mới 0,1,2,3,4,5,6,7...\n", pd2)
## chỉ ra cụ thể
print("chỉ ra cụ thể\n",pd.concat([df1, df2],keys=['ok_1','ok_2']))

################################################
data = [['A1', 'B1'],['A2', 'B2']]
df1 = pd.DataFrame(data, columns=('A', 'B'),index=[1, 2])
data = [['A3', 'B3'],['A4', 'B4']]
print(df1)
df2 = pd.DataFrame(data, columns=('B', 'C'),index=[3, 4])
print(df2)
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2]).fillna(1))
## Lấy trùng
print(pd.concat([df1, df2], join='inner'))
## lay het
print(pd.concat([df1, df2], join='outer'))
###################### Append

"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!__ Trộn data !!!!!!!!!!!!!!!!11
# One-to-one # Many-to-one # Many-to-many
# One-to-one
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],'hire_date': [2004, 2008, 2012, 2014]})
print(df1)
print(df2)
df3 = pd.merge(df1, df2)
print("One-to-one")
print(pd.merge(df1, df2))

# Many-to-one
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],'supervisor': ['Carly', 'Guido', 'Steve']})
print("Many-to-one")
print(pd.merge(df3, df4))

# Many-to-many.
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting','Engineering', 'Engineering', 'HR', 'HR'],'skills': ['math', 'spreadsheets', 'coding', 'linux','spreadsheets', 'organization']})
print("Many-to-many")
print(pd.merge(df1, df5))

# lay cot employee
print(pd.merge(df1, df2, on='employee'))


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'salary': [70000, 80000, 120000, 90000]})
print(pd.merge(df1, df3,left_on='employee', right_on='name'))
print(pd.merge(df1, df3,left_on='employee', right_on='name').drop('name', axis=1))




