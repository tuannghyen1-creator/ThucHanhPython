import math

# 1. Hàm kiểm tra số nguyên tố siêu tốc
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# 2. Thuật toán sinh số Strobogrammatic (Đệ quy)
def generate_strobogrammatic(length, total_length, mapping):
    if length == 0:
        return [""]
    if length == 1:
        return [digit for digit in mapping if mapping[digit] == digit]
    
    sub_res = generate_strobogrammatic(length - 2, total_length, mapping)
    res = []
    
    for s in sub_res:
        for left, right in mapping.items():
            # Không để số 0 đứng đầu số lớn hơn 1 chữ số
            if left == '0' and length == total_length:
                continue
            res.append(left + s + right)
    return res

def get_all_strobogrammatic(max_val, mapping):
    all_nums = []
    max_len = len(str(max_val - 1))
    for l in range(1, max_len + 1):
        all_nums.extend(generate_strobogrammatic(l, l, mapping))
    
    # Chuyển thành số nguyên và lọc các số nhỏ hơn max_val
    return sorted(list(set([int(x) for x in all_nums if int(x) < max_val])))

# 3. Bản đồ xoay 180 độ cho 2 trường hợp
standard_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
extended_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6', '2': '5', '5': '2'}

# Giới hạn đề bài: nhỏ hơn 1 triệu
LIMIT = 1000000

print("--- ĐANG XỬ LÝ DỮ LIỆU ---")

# --- CÂU A & B ---
strobo_standard = get_all_strobogrammatic(LIMIT, standard_map)
strobo_prime_standard = [x for x in strobo_standard if is_prime(x)]

# --- CÂU C & D ---
strobo_extended = get_all_strobogrammatic(LIMIT, extended_map)
strobo_prime_extended = [x for x in strobo_extended if is_prime(x)]

# --- CÂU E ---
# Hàm xoay 180 độ một số bất kỳ (trả về chuỗi số sau khi xoay, hoặc None nếu chứa số không xoay được)
full_rotatable_map = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
def rotate_180(n):
    s = str(n)
    rotated = []
    for char in reversed(s):
        if char not in full_rotatable_map:
            return None
        rotated.append(full_rotatable_map[char])
    return int("".join(rotated))

ans_e = []
# Tập hợp các số mở rộng để check điều kiện "không phải là số strobo mở rộng" cho nhanh
extended_set = set(strobo_extended) 

for i in range(LIMIT):
    if i not in extended_set and not is_prime(i):
        rev_val = rotate_180(i)
        if rev_val is not None and is_prime(rev_val):
            ans_e.append(i)

# --- IN KẾT QUẢ ---

print("\na.- Các số strobogrammatic chuẩn nhỏ hơn 1 triệu (In số lượng và một vài số đầu):")
print(f"Tổng cộng có: {len(strobo_standard)} số. Vài số đầu: {strobo_standard[:15]}...")

print("\nb.- Các số nguyên tố strobogrammatic chuẩn nhỏ hơn 1 triệu:")
print(strobo_prime_standard)

print("\nc.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu (In số lượng và một vài số đầu):")
print(f"Tổng cộng có: {len(strobo_extended)} số. Vài số đầu: {strobo_extended[:15]}...")

print("\nd.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
print(strobo_prime_extended)

print("\ne.- Các số không phải strobo, không phải nguyên tố nhưng xoay 180 độ ra số nguyên tố:")
print(f"Tìm thấy {len(ans_e)} số. Ví dụ 20 số đầu tiên:")
print(ans_e[:20])