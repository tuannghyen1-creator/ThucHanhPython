import math

def get_reverse(n):
    # Hàm đảo ngược số
    return int(str(n)[::-1])

def solve_114():
    try:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        
        friendly_numbers = []
        
        for i in range(a, b + 1):
            rev_i = get_reverse(i)
            # Kiểm tra GCD của số và số đảo ngược
            if math.gcd(i, rev_i) == 1:
                friendly_numbers.append(i)
        
        print("Các số thân thiện trong khoảng:")
        print(*friendly_numbers)
        print(f"Số lượng số thân thiện: {len(friendly_numbers)}")
        
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

solve_114()