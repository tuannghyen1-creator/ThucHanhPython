# Bai3_101.py

kiemTraSNT = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

n = int(input("Nhap n: "))

if kiemTraSNT(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")


loaiTamGiac = lambda a,b,c: (
    "Khong phai tam giac"
    if a+b<=c or a+c<=b or b+c<=a
    else
    "Tam giac deu"
    if a==b==c
    else
    "Tam giac vuong"
    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a
    else
    "Tam giac can"
    if a==b or b==c or a==c
    else
    "Tam giac thuong"
    
)

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

print(loaiTamGiac(a,b,c))