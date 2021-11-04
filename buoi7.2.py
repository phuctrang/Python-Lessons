import pandas as pd
import numpy as np
# dan so
pop = pd.read_csv('state-population.csv')
# dien tich
areas = pd.read_csv('state-areas.csv')
# tên viêt tắt của các bang
abbrevs = pd.read_csv('state-abbrevs.csv')
# print(pop.head(4))
# print(areas.head(4))
# print(abbrevs.head())
##left_on='state/region', right_on='abbreviation': 2 cột này cùng dữ liệu nhưng khác tên cột. nên đùng left-right
merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
# print("merged:\n", merged.head())
merged = merged.drop('abbreviation',axis=1)
# print("merged.drop(abbreviation)\n", merged.head())
# print(merged.isnull().any())
# print("show NaN: ")
# print(merged[merged['population'].isnull()])


# print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
""": dữ liệu population bao gồm các mục của PR (Puerto Rico) và USA 
không xuất hiện trong khóa viết tắt của cột state. Ta có thể khắc phục những lỗi này 
nhanh chóng bằng cách điền vào các giá trị thích hợp:"""
# gan NaN cua state PR = Puerto Rico
# gan NaN cua state USA = United States
merged.loc[merged['state/region']=='PR','state'] = 'Puerto Rico'
merged.loc[merged['state/region']=='USA','state']='United States'
# print(merged.isnull().any())
# print(merged[merged['population'].isnull()])

final = pd.merge(merged, areas, on='state', how='left')
# print("final")
print(final.head())
print("tiep tuc kiem tra final trong NaN hay khong? ")
print(final.isnull().any())
# population, area vẫn rỗng nha :))

print(final['state'][final['area (sq. mi)'].isnull()].unique())
"""Ta thấy rằng cột 'area (sq. mi)' không chứa diện tích của United States. Ta có 
thể chèn giá trị thích hợp (ví dụ: bằng cách sử dụng tổng của tất cả các diện tích tiểu 
bang), nhưng trong trường hợp này, ta sẽ chỉ bỏ các giá trị rỗng"""
final.dropna(inplace=True)
print(final.isnull().any())

"""Bây giờ ta có tất cả dữ liệu cần thiết để trả lời câu hỏi quan tâm. Trước tiên ta chọn 
phần dữ liệu tương ứng với năm 2010 và tổng dân số. Ta sẽ sử dụng hàm query() (sẽ
trình bày sau) để thực hiện việc này một cách nhanh chóng."""
data2011 = final.query("year == 2011 & ages == 'total'")
print(data2011.head())
data2011.set_index('state', inplace=True)
print(data2011.head())

density = data2011['population'] / data2011['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
print('MẬT DỘ DÂN SỐ 2011: ')
print(density.head())

print('MẬT ĐỘ NHỎ CUỐI DANH SÁCH:')
print(density.tail())

# tong dan so nuoc my 2010
data2011 = final.query("year == 2010 & ages == 'total'")
print(data2011)
print("tong dan so 2011: ", data2011['population'].sum())
# temp = data2011['state/region']!='USA'
# print('temp')
# print(temp['population'].sum())








