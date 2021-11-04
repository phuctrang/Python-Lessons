# bai 1. tạo ngẫu nhiên 1 dãy số nguyên, in ra max, min, ave
# import random
# L = [random.randint(1, 100) for i in range(2,20)]
# print(L)
# x = int(input("Nhap mot so nguyen: "))
# print("so nguyen %d xuat hien %d lan"%(x, L.count(x)))
# print("so lon nhat: ", max(L))
# print("so nho nhat: ",min(L))
# print("trung binh cong: ",sum(L) / len(L))
# ## nhap day so nguyen cach nhau 1 khoang trong
# # arr = list(map(int, input().split()))
# # xem ham nay lam gì?
# print(map.__doc__)

# bai 2.
import math
D = {'X_a':float(input("nhap X_a: ")), 'Y_a':float(input("nhap Y_a: ")),
     'X_b':float(input("nhap X_b: ")),'Y_b':float(input("nhap Y_b: ")),
     'X_c':float(input("nhap X_c: ")),'Y_c':float(input("nhap Y_c: "))}
print("3 diem vua nhap co toạ độ lần lượt là: ")
print("A=",[D['X_a'],D['Y_a']],"\nB=", [D['X_b'],D['Y_b']], "\nC=",[D['X_c'],D['Y_c']] )
AB = math.sqrt(pow(D['X_b'] - D['X_a'], 2) + pow(D['Y_b'] - D['Y_a'], 2))
AC = math.sqrt(pow(D['X_c'] - D['X_a'], 2) + pow(D['Y_c'] - D['Y_a'], 2))
BC = math.sqrt(pow(D['X_c'] - D['X_b'], 2) + pow(D['Y_c'] - D['Y_b'], 2))
print("Độ dài AB=%.2f, AC=%.2f, BC=%.2f"%(AB, AC, BC))
p = (AB+AC+BC)
print("Chu vi:",p)
p = p/2
print("Diện tích tam giác ABC: ", math.sqrt(p * (p - AB) * (p - AC) * (p - BC)))

# import math
# import collections
#
# Point2D = collections.namedtuple("Point2D", "x y")
# x_a = int(input("Nhap toa do x cua A: "))
# y_a = int(input("Nhap toa do y CUA A: "))
# x_b = int(input("Nhap toa do x cua B: "))
# y_b = int(input("Nhap toa do y CUA B: "))
# x_c = int(input("Nhap toa do x cua C: "))
# y_c = int(input("Nhap toa do y CUA C: "))
# A = Point2D(x_a, y_a)
# B = Point2D(x_b, y_b)
# C = Point2D(x_c, y_c)
# AB = math.dist(A, B)
# BC = math.dist(B, C)
# AC = math.dist(A, C)
# P = (AB + AC + BC) / 2
#
#
# def getAngle(A, B, C)
#      def getAngle(A, B, C):
#           ang = math.degrees(math.atan2(C[1] - B[1], C[0] - B[0]) - math.atan2(A[1] - B[1], A[0] - B[0]))
#           return ang + 360 if ang < 0 else ang
#
#
# print("Độ dài AB: ", AB)
# print("Độ dài BC: ", BC)
# print("Độ dài AC: ", AC)
# print("Chu vi của tam giác ABC: ", AB + BC + AC)
# print("Diện tích tam giác ABC: ", math.sqrt(P * (P - AB) * (P - AC) * (P - BC)))
# print("Góc B: ", getAngle(A, B, C))
# print("Góc C: ", getAngle(A, C, B))
# print("Góc A: ", getAngle(C, A, B))

#bai3
import random

#
#
# L = [i for i in range(1900,2099)]
# print(L)
# L1 = [i for i in range(1900,2099) if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]
# x = int(input("Nhap vao 1 năm để kiểm tra: "))
# if L1.count(x) !=0:
#      print(x, "la nam nhuan")
# else:
#      print(x, "Khong phai nam nhuan")












