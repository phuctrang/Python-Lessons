import numpy as np
import pandas as pd
data = pd.read_csv('filecsvbuoi4.2.csv')
print("hang, cot: ")
print(data.shape)
rain = data['PRCP'].values
# print("luong mua: ", rain)
print(len(rain))
print("ngay ko mua: ", np.sum(rain==0))
print("ngay mua: ", np.sum(rain>0))

# cau1
# count = 0
# for i in range(0,365):
#     if (ngaythang <=20140331):
#         count += np.count_nonzero(rain[i]>0)
# print(count)

import datetime as dt
time1 = dt.datetime(2014, 1, 1)
time2 = dt.datetime(2014, 3, 31)
time = time2 - time1
ngaymua = 0
n = (time.days)
for i in range(0, n):
    ngaymua += np.sum(rain[i] > 0)
print("so ngay mua tu 1.1.14 den 31.3.14 là: ", ngaymua)
## cach khac:
ngaythang = data['DATE'].values
# ngaythang = 20140331
chisongay = np.where(ngaythang==20140331)
# chisongay = np.sum(chisongay)
# print(chisongay)
chisongay = int(chisongay[0])
# tu ngay 0 den ngay 89
# ngay mưa mặc định rain ==1
ngaymua = np.count_nonzero(rain[0:chisongay])
print("songaymua: ", ngaymua)
ngaykhongmua = np.count_nonzero(rain[0:chisongay]==0)
print("songaykhongmua: ", ngaykhongmua)
# ngaykhongmua = np.zeros(rain[0:chisongay])
# print("songaykhongmua: ", ngaykhongmua)
qui1 = rain[0:chisongay]
print(qui1) # cac gia tri cua qui 1. 1/1 > 31/3
print("ngaykhongmua: ", np.count_nonzero(qui1==0))

print("luong mua trung binh: ", np.average(qui1))

print("luong mua lon nhat: ", np.max(qui1))
#ngay mua lon nhat:
x = np.where((qui1==np.max(qui1)))

print("ngay co luong mua lon nhat: ", ngaythang[x])
# mua nho chu ko phai ko mua (>0)
ngaymua = np.count_nonzero(qui1>0)
print("so ngay mua qui 1: ", ngaymua)
rain = data['PRCP'].values
solieu = np.where(qui1!=0)
manggiatri = rain[solieu]
print("manggiatri: ",manggiatri )
print(np.min(manggiatri))
# hoặc :))))))))) :)))))))
print('lượng mua nho nhat la:',np.min(rain[np.where(qui1>0)]))
# OK OK OK # OK OK OK # OK OK OK # OK OK OK # OK OK OK # OK OK OK # OK OK OK # OK OK OK
print("tong luong mua qui 1: ", np.sum(qui1))
songaymua = np.count_nonzero(qui1)
tb = np.average(qui1)
print("so ngày có mưa > luong mua TB: ", np.count_nonzero(qui1>tb))

import matplotlib.pyplot as plt
plt.plot(rain)
plt.show()














