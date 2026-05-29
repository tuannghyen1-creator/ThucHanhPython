# Bai2_101.py

def bangCuuChuong(a, b):

    for i in range(a, b + 1):

        print("\nBang cuu chuong", i)

        for j in range(1, 11):
            print(i, "x", j, "=", i * j)


def lietKeSNT(n):

    print("Cac so nguyen to <= ", n)

    for i in range(2, n + 1):

        kt = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                kt = False
                break

        if kt:
            print(i, end=" ")

    print()


def lietKeUoc(n):

    print("Cac uoc cua", n, "la:")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

    print()


a, b = map(int, input("Nhap a,b: ").split(","))

bangCuuChuong(a, b)

n = int(input("\nNhap n de liet ke so nguyen to: "))
lietKeSNT(n)

n = int(input("\nNhap n de liet ke uoc: "))
lietKeUoc(n)