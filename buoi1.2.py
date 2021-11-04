import math
import cmath
# a = float(input("nhap he so a: "))
# b = float(input("nhap he so b: "))
# c = float(input("nhap he so c: "))
# denta = (b**2)-4*a*c
# x1 = 0
# x2 = 0
# #ax2 +bx +c = 0:
# if(a==0):
#     print(">>>return pt bac 1<<<")
#     if(b==0):
#         print("PT vo so nghiem")
#     else:
#         print("PT co nghiem la: x = %.2f" %(-c/b))
# else:
#     if(denta < 0):
#         print("PT vo nghiem")
#     if(denta==0):
#         print("PT co 1 nghiem kep: %f" %(-b/2*a))
#     if(denta>0):
#         x1 = (-(b)**2 + (math.sqrt(denta)))/2*a
#         x1 = (-(b)**2 - (math.sqrt(denta)))/2*a
#         print("pt có 2 nghiem: x1 = %.2f, x2 = %.2f" %(x1, x2))


#bai 1:
# t = float(input("nhap thoi diem nem bong: "))
# h0 = float(input("Nhap do cao ban dau: "))
# v0 = float(input("Nhap van toc ban dau: "))
# g = 9.8
# v = v0 - g*t
# tg = g*t*t
# h = h0 + v0*t - 0.5*tg
# print("Tai thoi diem %d giay:\nchieu cao qua bong = %.1f met\nVan toc = %.1f m/s"%(t,h,v))

#bai2
# import math
# a = (2+math.exp(2.8))/(math.sqrt(13)-2)
# print(a)
# b= (1-math.pow((1+math.log(a,math.e)),-3.5))   /   (1+math.sqrt(5))
# print(b)
# c = math.sin((2-math.sqrt(2))/(2+math.sqrt(2)))
# print(c)

#bai3:
# import math
# a = float(input("cạnh a: "))
# b = float(input("cạnh b: "))
# c = float(input("cạnh c: "))
#
# p = a+b+c
# nuachuvi = p/2
# s = math.sqrt(nuachuvi*(nuachuvi-a)*(nuachuvi-b)*(nuachuvi-c))
# cosA = (b*b + c*c - a*a)/(2*b*c)   #đơn vị radian
# cosB = (c*c + a*a - b*b)/(2*c*a)
# cosC = (a*a + b*b - c*c)/(2*a*b)
# doi = 180/math.pi
# gocA = math.acos(cosA)*doi  #đổi từ radian sang độ
# gocB = math.acos(cosB)*doi
# gocC = math.acos(cosC)*doi
#
# print("Chu vi:",p)
# print("Diện tích:",s)
# print("góc a:",gocA)

s ="abc"
print(s[0])
print(s[1])
print(s[2])
# cuoi chuoi
print(s[-1])
#ke cuoi
print(s[-2])
print(s[-3])
s = s + 'd'
print(s)











