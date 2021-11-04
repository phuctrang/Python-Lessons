import pandas as pd

data = pd.read_csv('filecsvbuoi4.2.csv')
# rain = data['PRCP'].values
# date = data['DATE'].values
# datafr = pd.DataFrame({'luong_mua': rain}, index=date)
# data_qui2 = data.loc[20140401:20140630]
# date = data['DATE']
# rain = data['PRCP']
# print(data_qui2)
############ ok mà??
data_qui2 = data[(data['DATE']>=20140401) & (data['DATE']<=20140630)]
# print(data_qui2)
date = data_qui2['DATE']
rain = data_qui2['PRCP']
datafr = pd.DataFrame({'ngay': date, 'luong_mua': rain})
print(datafr)
print("so ngay mua trong qui 2: \n", pd.value_counts(rain>0))
print("luong mua trung binh qui 2: \n", rain.mean())

# print('lượng mua nho nhat la:',np.min(rain[np.where(qui1>0)]))
print("luong mua lon nhat quy 2: ", rain.max())
# print(data_qui2[rain>0].min())
dt = data_qui2[rain > 0]
muanhonhat = dt['PRCP'].min()
print("mua nho nhat: ", muanhonhat)

# print("luong mua lon nhat quy 2: ", data_qui2.max())
# print("so ngay mua trong qui 2: ", pd.value_counts(data_qui2>0))


#
# dau_qui = date[
# index_dau = int(dau_qui[0])
# cuoi_qui = date.equals(20140631)
# index_cuoi = int(cuoi_qui[0])
#
# qui_2 = datafr.iloc[index_dau:index_cuoi]
# print(qui_2)
#
# #
# # index_qui2 = index_cuoi - index_dau
# ngaymua = np.count_nonzero(rain[index_dau:index_cuoi])
# print("ngaymua_qui2: ", ngaymua)



