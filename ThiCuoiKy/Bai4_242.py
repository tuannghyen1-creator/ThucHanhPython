# Bai4_101.py

soDongNhat = lambda n: len(set(str(n))) == 1

soHoanThien = lambda n: sum(i for i in range(1,n) if n%i==0) == n

print("Cac so dong nhat tu 1 den 10000:")

for i in range(1,10001):
    if soDongNhat(i):
        print(i, end=" ")

print("\n")

print("Cac so hoan thien tu 1 den 10000:")

for i in range(1,10001):
    if soHoanThien(i):
        print(i, end=" ")