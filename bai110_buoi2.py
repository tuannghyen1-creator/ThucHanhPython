def solve_110():
    cipher_text = input("Nhập chuỗi nén (cipher text): ")
    plain_text = ""
    i = 0
    
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            # Lấy số lượng (nằm ngay sau dấu #)
            count = int(cipher_text[i+1])
            # Lấy ký tự cần lặp (nằm sau chữ số)
            char = cipher_text[i+2]
            # Thêm vào chuỗi kết quả
            plain_text += char * count
            # Nhảy qua 3 ký tự vừa xử lý (#, số, ký tự)
            i += 3
        else:
            # Nếu không phải dấu #, giữ nguyên ký tự
            plain_text += cipher_text[i]
            i += 1
            
    print("Plain text:", plain_text)

# Chạy thử
# Input: XY#6Z1#4023 -> Output: XYZZZZZZ1000023
# Input: #39+1=1#30  -> Output: 999+1=1000
solve_110()