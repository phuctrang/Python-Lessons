import numpy as np
import pandas as pd
data = pd.read_csv('filecsvbuoi4.2.csv')
print("hang, cot: ")
print(data.shape)
rain = data['PRCP'].values
print("luong mua: ", rain)
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
ngaymua = np.count_nonzero(rain[0:chisongay])
print("songaymua: ", ngaymua)
ngaykhongmua = np.count_nonzero(rain[0:chisongay]==0)
print("songaykhongmua: ", ngaykhongmua)






