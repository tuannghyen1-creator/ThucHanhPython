# Bai1_101.py

dai = float(input("Nhap chieu dai day hinh khoi chu nhat (cm): "))
rong = float(input("Nhap chieu rong day hinh khoi chu nhat (cm): "))
cao = float(input("Nhap chieu cao hinh khoi chu nhat (cm): "))

chuoi = str(dai) + str(rong) + str(cao)

dem = 0

for i in chuoi:
    if i.isdigit():
        if int(i) % 2 != 0:
            dem += 1

dienTich = 2 * (dai * rong + dai * cao + rong * cao)
theTich = dai * rong * cao

print("So luong so le can hien thi:", dem)
print("Dien tich day hinh chu nhat =", round(dienTich,2), "cm\u00b2")
print("The tich hinh khoi =", round(theTich,2), "cm\u00b3")