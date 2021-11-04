import pandas as pd
import numpy as np
# dan so
pop = pd.read_csv('state-population.csv')
# dien tich
areas = pd.read_csv('state-areas.csv')
# tên viêt tắt của các bang
abbrevs = pd.read_csv('state-abbrevs.csv')

# print(pop)
# print(areas)
# print(abbrevs)
# 1. hien thi dan so cac bang vao nam 2010. 2011. 2012
# 2. hien thi dan so nam 2012 theo cac bang
# 3. thong ke theo bang xoay:dong cac bang, cot cac nam, data xuat hien la tong dan so
# 4. những data bị NaN, ta điền giá trị 0
# 5. vẽ do thi bang newyorks các năm
merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation',axis=1)
# print(merged)
data2010 = merged.query("year == 2010")
data2010.set_index('year', inplace=True)
print(data2010)
data2011 = merged.query("year == 2011")
b = data2011.drop('ages', axis=1)
b.set_index('year', inplace=True)
print(b)
data2012 = merged.query("year == 2012")
c = data2012.drop('ages', axis=1)
c.set_index('year', inplace=True)
print(c)


danso2012cacbang = merged.query("year == 2012 & state=='Alaska'")
danso2012cacbang=danso2012cacbang.drop('ages', axis=1)
danso2012cacbang.set_index('year',inplace=True)
print(danso2012cacbang)

# kiem tra truong NaN
print(merged.isnull().any())
# population | state
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
# Pr, usa null in state
print(merged.loc[merged['population'].isnull(), 'state/region'].unique())
# PR null trong population
### gan gia tri =0
# merged.loc[merged['state/region']=='PR','state'] = 0
# merged.loc[merged['state/region']=='USA','state']= 0
# merged.loc[merged['state/region']=='PR','population']= 0
merged.fillna(0, inplace = True)
print(merged.isnull().any())

# da het NaN

"""

AL = final[(final['year'] == 2010) & (final['state'] == 'Alaska')]
AL = final[(final['year'] == 2011) & (final['state'] == 'Alaska')]
AL = final[(final['year'] == 2012) & (final['state'] == 'Alaska')]
AL[['year','state','population']]


import numpy as np
pivot = pd.pivot_table(final,index=["year","state"],values=['population'],aggfunc=np.sum)

pivot.fillna(0, inplace = True)

"""