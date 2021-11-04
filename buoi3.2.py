"""
# bai1
# def rectangle(m, n):
#     dem = 0
#     for i in range(0,m):
#         for j in range(0,n):
#             print("*")
#         print("\r")
# rectangle(3, 4)

# def rectangle(m,n):
#     for i in range(0,m):
#         for j in range(0,n):
#             print("*", end='')
#         print("\r")
# rectangle(2,4)

#
# a = int(input("Nhập a:"))
# b  = int(input("Nhập b:"))
# def RECTANGLE(a,b):
#     if a>0 and b>0:
#         for i in range(0,a):
#             for j in range(0,b):
#                 print("*",end="")
#             print("\r")
#     else:
#         print("nhập số dương")
# print(RECTANGLE(a,b))

#bai3:Bài 1.3. Viết một hàm gọi là sum_digits
# nhận một số nguyên num và trả về tổng các chữ số của num.
# def sum_digits(numb):
#     dem = 0
#     for i in range(0,numb):
#         dem-=-1
#     print("Tổng các chữ số = ", dem)
# sum_digits(5)
#
#
# bai2:
"""
"""
Bài 1.2. (a) Viết một hàm có tên add_excitement nhận một danh sách
 các chuỗi và thêm dấu chấm than (!) vào cuối mỗi chuỗi
  trong danh sách. Chương trình sẽ sửa đổi danh sách ban đầu
  và không trả lại bất kỳ thứ gì.
(b) Viết cùng một hàm giống hàm add_excitement nhưng
 không sửa đổi danh sách ban đầu và thay vào đó sẽ trả về một danh sách mới.

# def add_excitement(S:list):
#     L = []
#     for i in range(0,len(S)):
#         L.append(S[i]+"!")
#     return L
# S = ["abc", "abcd", "xyz"]
# print(add_excitement(S))


# def add_exciment(s):
#     for i in s:
#         print( ''.join([i,"!"]))
# s=["aaa","bbb","ccc"]
# add_exciment(s)

# def add_excitement(L):
#     for i in range(0, len(L)):
#         L[i]+='!'

# S = ["abc", "abcd", "xyz"]
# print("ds truoc khi goi ham: ", S)
# add_excitement(S)
# print("DS sau khi goi ham: ",S)
"""


# def SUM(n):
#     tong = 0
#     while n > 0:
#         du = n%10
#         tong += du
#         n =int (n/ 10)
#     return tong
# n = int(input("Nhập số nguyên dương n = "));
# print("Tổng các chữ số của", n ,"là", SUM(n))
"""
"""
## bai 3
# def sum_digits(num):
#     tong = 0
#     if (num >= 0):
#         while (num != 0) :
#             du = num % 10
#             num = num // 10
#             tong += du
#     else:
#         tong = -1
#     return tong
# print(sum_digits(10))
"""
##########################################
"""
## bai4
"""
def sum_digits(num):
    tong = 0
    if (num >= 0):
        while (num != 0) :
            du = num % 10
            num = num // 10
            tong += du
    else:
        tong = -1
    return tong
# def can(n):
#     if (n < 0):
#         return -1
#     if (n < 10 and n >= 0):
#         return n
#     else:
#         tong = 0
#         if (n >= 0):
#             while (n != 0) :
#                 du = n % 10
#                 n = n // 10
#                 tong += du
#     return can(tong)
# print(can(12345))
## hoac
def can(n):
    if n<0:
        return -1
    tong = sum_digits(n)
    while(tong>=10):
        tong = sum_digits(tong)
    return tong
print(can(12345))


## bai 5 ok 
def first_diff(s1, s2):
    m= len(s1)
    n= len(s2)
    i=0
    while i<m and i<n:
        if (s1[i] != s2[i]):
            return i
        else:
            i+=1
    if i==m and i==n:
        return -1
    else:
        return i
print(first_diff("dddfvdd", "dddgvdd"))
"""
""" hàm lambda
vd:
"""
f = lambda a,b: a+b
print(f(3,4))




