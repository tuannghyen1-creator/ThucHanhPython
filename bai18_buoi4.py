import math

# a) Số thân thiện
friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương
square = lambda n: int(math.sqrt(n))**2 == n

# c) Số đồng nhất
uniform1 = lambda n: all(x == str(n)[0] for x in str(n))
uniform2 = lambda n: not any(x != str(n)[0] for x in str(n))

# d,e) hàm tổng ước số (tối ưu)
divisor_sum = lambda n: sum(i for i in range(1, n//2+1) if n%i==0)

perfect = lambda n: divisor_sum(n)==n
abundant = lambda n: divisor_sum(n)>n

# f) Số tăng dần
increasing = lambda n: all(str(n)[i] <= str(n)[i+1]
                           for i in range(len(str(n))-1))

# g) Armstrong
armstrong = lambda n: sum(int(d)**len(str(n)) for d in str(n))==n

# h) Nguyên tố

# cách 1
prime1 = lambda n: n>1 and sum(1 for i in range(1,n+1) if n%i==0)==2

# cách 2
prime2 = lambda n: n>1 and sum(i for i in range(1,n+1) if n%i==0)==n+1

# cách 3 (nhanh nhất)
prime3 = lambda n: n>1 and not any(
    n%i==0 for i in range(2,int(math.sqrt(n))+1)
)

# cách 4
def F(k):
    return k>1 and len(list(filter(
        lambda x: k%x==0,
        range(1,k+1)
    )))==2

# i) Palindrome
palindrome = lambda n: str(n)==str(n)[::-1]

# j) Prime Palindrome
prime_palindrome = lambda n: palindrome(n) and prime3(n)

# k) Lộc phát
locphat1 = lambda n: all(c in '68' for c in str(n))
locphat2 = lambda n: str(n).count('6')+str(n).count('8')==len(str(n))

# l) Lộc phát Palindrome
locphat_pal = lambda n: locphat1(n) and palindrome(n)

# TEST (đừng chạy 1 triệu trước)
LIMIT = 1000

print("Armstrong:")
for i in range(1, LIMIT+1):
    if armstrong(i):
        print(i,end=' ')

print("\n\nNguyên tố:")
for i in range(1, LIMIT+1):
    if prime3(i):
        print(i,end=' ')