def solve_117():
    n_str = input("Nhập số nguyên dương n: ")
    total_sum = 0
    length = len(n_str)
    
    # Duyệt qua tất cả các vị trí bắt đầu và kết thúc để lấy chuỗi con
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub_str = n_str[i:j]
            sub_num = int(sub_str)
            total_sum += sub_num ** 2
            
    print(f"Tổng bình phương (S): {total_sum}")

# Chạy thử
# Input: 2207  -> Output: 4963088
# Input: 54321 -> Output: 2999539505
solve_117()