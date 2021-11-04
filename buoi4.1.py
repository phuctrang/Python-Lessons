"""KHOA HOC MAY TINH"""
import numpy as np
"""
1. Thay vi dung list trong python, ta dùng đối tượng darray của numpy./ 
2. ta có thể tạo mảng data 


A = np.array([1,2,3,4])
print(type(A))
print(A)
#mang 2 chieu:
B = np.array([[1,2,3], [4,5,6]])
print(B)
# mang so:
C = np.zeros(10, dtype=int)
print(C)
print(np.ones(10, dtype=int))
D = np.array((2,3))
# 2 chieu
E = np.ones((2,3), dtype=int)
print(E)


x = np.random.randint(10, size=(3,4,5))
# chi so 0: hang 0, cot 0 !!!!

print(x)

print("x ndim:", x.ndim)
print("x shape:", x.shape)
print("x size:", x.size)
print("x dtype:", x.dtype)
print("x itemsize:", x.itemsize)
print("x nbyte:", x.nbytes)

y = np.random.randint(10, size=(3,4))
print(y)
print(y[1,2])

# x(start, stop, step)
a = np.arange(10)
print(a)
print("1. 5 ptu dau: ", a[:5])
print("2. 5 ptu sau: ", a[5:])
print("3. mang a cach nhau 2 donvi: ", a[::2])
print("4. 5-8: ", a[5:8])
print("5. mang nguoc: ", a[::-1])
print("nguoc ", a[5::-2])
# neu step là số âm, thì vị trí bắt đầu là phẩn tử cuối: 9


y = np.random.randint(10, size=(3,4))
print(y)
# print(y[1:2])
# print(y[:, 0])
# ban sao nhung thay doi luon ban goc
xcopy = y[:2, :2]
print(xcopy)
xcopy[0,0] = 100
print(y)
# ban sao nhung khong thay doi luon ban goc !!!
xcopy = y[:2, :2].copy()
print(xcopy)
xcopy[0,0] = 5
print(y)

print("########## doi mang 1 chieu thanh mang 2 chieu ########3")
x = np.arange(1,10)
print(x)
x1 = x.reshape(3,3)
print(x1)


"""
####################################################################
"""
grid = np.array([[1, 2, 3],[4, 5, 6]])
print(grid)
a = np.concatenate((grid, grid))
print(a)
b = np.concatenate((grid, grid), axis=1)
print(b)

x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y))
print("z = ",z)
z1 = z.reshape(2,3)
print(z1)

print("x, y", x,y)
z = np.hstack([x,y])
print("dong: ",z)
z = np.vstack([x,y])
print("cot: ")
print(z)

# các hàm này viết bằng c++
# tach mang
x = np.array([1,2,3,4,5,6,7])
print(x)
x1 ,x2,x3 = np.split(x, [3,5])
print(x1, x2, x3)
# x1 la: ptu 0 > ptu 3
# x2 la: ptu 3 > ptu 5
# x3 la: ptu 5 > ptu cuoi cung

"""

## ham ufunc

x = np.arange(1,10)
y = np.arange(11,20)
print(x)
print(y)
tong = x+y
print(tong)
hieu = x-y
print(hieu)
cong = x+5
print(cong)
print("tinh sin cua tung phan tu trong mang x: ",np.sin(x))

# thuoc tinh out:
print(np.multiply(x,3))









