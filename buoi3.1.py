


"""
# cau truc dieu khien và hàm
# if ...else
# x= int(input("X= "))
# y= int(input("y= "))
# if(x>y):
#     print("so lon nhat la: ", x)
# else:
#     print("so nho nhat: ", x)

# x = float(input("nhap diem so: "))
# if x>8:
#     print("hsg")
# elif x>=6.5:
#     print("kha")
# elif x>=5:
#     print("tb")
# else:
#     print("yeu")


############## for - while :   while (e): s1   \n else: s2
# nhap vaof 1 so, in ra man hinh tong nho nhat , (cua cac chu so nho hon n) lon hon hoac =n
# vi du n=10. in ra 1+2+3+4
# x= int(input("X= "))
# sum = 0
# i=1
# while sum<x:
#     sum = sum + i
#     print("%d " % (i))
#     i = i+1
# else:
#     print("tong can tim la: ", sum)

## for_ in   else:   for e in <mien gia trij> > s1 else s2
# L = [2,5,4,9]
# s = "abcd"
# for i in s:
#     print(i)
#

 ham
Hàm
-Hàm toàn cục : hàm được viết trong file .py: tat cả các lệnh trong file
này đều sử dụng được 
-hàm cục bộ: hàm định nghĩa trong hàm khác
-phương thức trong lớp
-hàm lamda: hàm định nghĩa tại thời điểm sử dụng, thường có 1 dòng lệnh
và là biểu thức
     def tenham(các tham sô):
        các câu lệnh
Hàm trả về giá trị hoặc không

vd: nhap 2 so, tra ve so lon nhat

def lonnhat(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("nhap a: "))
b = int(input("nhap b: "))
max = lonnhat(a,b)
print("so lon nhat la: ", max)

- tham số ngầm định của hàm: lúc gọi hàm có thể truyền đối số hoặc không

vd:

def f(a, b=0):
    print("tham số a của hàm: %d"%(a))
    print("tham số b của hàm: %d" % (b))
# f(3,4) 34
# f(3) 3,0: ngam dinh la b=0

-tham so ngầm định phải ở cuối danh sách các tham sô
-Truyền tham số rõ ràng, ta có thể chỉ rõ tham sô nào và nhận giá trị
gì bằng cú pháp "tenthamso = giá trị"


vd:

def f(a,b,c):
    print(a)
    print(b)
    print(c)
f(a=1,b=2,c=3)
#same: khong can thu tu tham so
f(b=2, a=1, c=3)

Quy ước: tên hằng: tất cả là chữ hoa; vd: PI, DENTA
        Tên hàm, tên biến: ghi thường, nếu nhiều hơn 1 từ dùng dấu gạch dưới
        Tên lớp: viết hoá chữ đầu tiên của từ
Thuộc tính: __doc__ cho mỗi đối tượng: ý nghĩa của Hàm và lớp

import math
print(math.sqrt.__doc__)

# viet ham đưa ra gợi ý của hàm __doc__



def f(a,b,c):
    "Hàm f chỉ nhận 3 tham so a,b,c_ Đây là mô tả hàm !!!"
    print(a)
    print(b)
    print(c)
print(f.__doc__)

Ta tổ chức hàm thành module ( để sẳn và xài bằng import ):
tất cả hàm viết trong file .py tạo thành 1 module,
Tên module là tên file

Thường lưu các file module này  trong thư viện lib của python trong ổ C
Sau đó sử dụng bằng lệnh Import <tên module>
vd

def f(a,b):
    return a+b
def f1(x,y,z=0):
    return x*y+z
# su dung:
import buoi3.1
a = int(input("nhap so 1 =  "))
b = int(input("nhap so 2 =  "))
c = int(input("nhap so 3 =  "))
tong = buoi3.1.f(a,b)
tong = buoi3.1.f(tong, c)
print("tong 3 so: %d"%(tong)).

- Nhom nhieu module (file .py) lại thành một gói(package)
tao 2 module trong p1


goi moi P1: chia 2 module M1,M2
M1 chứa hàm f
M2 chứa hàm f1

su dung:

import goi1.M1
import goi1.M2

su dung f của M1
print(goi1.M1.f(10,20))

OK !!!
"""

# from P1 import M1
# # hoặc import P1.M1
# tong = M1.f(2,4)
# print(tong)











