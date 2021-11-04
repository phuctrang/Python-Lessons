# nhom du lieu (groupby)
"""
import pandas as pd
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],'data':
range(6)}, columns=['key', 'data'])
print(df)
df.groupby('key').sum
print(df.groupby('key').sum())

import numpy as np
hanghoa = pd.DataFrame({'mh': ['A', 'B', 'C', 'A', 'B', 'C'],
'xuat': np.random.randint(5, size=6), 'nhap': np.random.randint(10,
size=6)}, columns=['mh', 'nhap', 'xuat'])
print(hanghoa)
print(hanghoa.groupby('mh').sum())
print(hanghoa.groupby('mh')['nhap'].sum())

for (ma, dulieu) in hanghoa.groupby('mh'):
    print('Mặt hàng {0} có số lượng xuất:{1}'.format(ma,dulieu['xuat'].sum()))
# hanghoa.groupby('mh').aggregate(['min', 'mean','max'])
print(hanghoa.groupby('mh').aggregate(['min', 'mean','max']))
# print(hanghoa.index)
#######################
########################
#########################

# goi pandas chua cac doi tuong va cac phuong thuc thao tac tren du lieu:
Các đối tượng
1. Series: giong mang 1 chieu
2.  DataFrame: giong mang 2 chieu 
3. Index: chi so cua du lieu
Các thao tác: 
+ Trích chọn data từ mỗi đối tượng
+ Các phép toán trên các đối tượng: 
+ Quản lý dữ liệu bị thiếu (NaN) NOT A NUMBER NONE
+ Ghép nối data 
+ Trộn data
+ Nhóm data
#######################
########################
#########################
"""
# vẽ đồ thị:
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# tu 1 den 10: chia thanh 1000 so: 1.001 , 1.002 ....9.999
# x = np.linspace(0, 10, 1000)
# # plt.plot(x, np.sin(x))
# plt.xlim(-10, 10)
# plt.ylim(-5, 5)
# plt.plot(x, np.cos(x),'--c')
# # plt.savefig('E:\hinh1.png')
# # dieu tiet truc toa do chinh xac
# # plt.axis('equal')
# # dam bao do thi ham so đi phủ hết figure
# plt.xlabel('truc x')
# plt.ylabel('truc y')
# plt.axis('tight')

data = pd.read_csv('filecsvbuoi4.2.csv')
x = data.index
y = data['PRCP']
# bat dau tu ngay 1
# dinh o, mau green
# plt.plot(x,y, '-og', label= 'do thi 2014')
# plt.plot(x+10,y+10, label= 'do thi 2014+10')
# plt.xlabel('Ngày mưa 2014')
# plt.ylabel('Lượng mưa')
plt.title('bieu do luong mua theo tung ngay trong nam 2014')
plt.xlabel('luong mua')
plt.ylabel('so ngay co luong mua tuong ung')
plt.hist(y)

## cac diem data ko có nối với nhau !!!
# plt.scatter(x,y, '-og', label= 'do thi 2014')
plt.show()


