import math
class Student:
    ma = 1
    def __init__(self,name,diemTB) :
        self.code= "HS"+'{:02d}'.format(Student.ma)
        Student.ma += 1
        self.name = name
        self.diemTB = diemTB
    def xep_loai(self):
        if self.diemTB >= 9:
            return "XUAT SAC"
        elif self.diemTB >= 8:
            return "GIOI"
        elif self.diemTB >= 7:
            return "KHA"
        elif self.diemTB >= 5:
            return "TB"
        else:
            return "YEU"
        
hs = []
for i in range(int(input())):
    hoten = input() 
    diem = list(map(float, input().split()))
    tong = diem[0]*2 + diem[1]*2
    for j in range(2, 10):
        tong += diem[j]
    ans = round(tong/12 + 0.01,1)
    hs.append(Student(hoten,ans))

hs.sort(key = lambda x: (-x.diemTB,x.ma))
for i in hs:
    print(i.code,i.name,i.diemTB,i.xep_loai())

# def tinh_diem_trung_binh(diem):
#     diem_toan = diem[0]
#     diem_tieng_viet = diem[1]
#     diem_con_lai = diem[2:]
#     diem_trung_binh = (2 * diem_toan + 2 * diem_tieng_viet + sum(diem_con_lai)) / 12
#     return diem_trung_binh

# def xep_loai(diem_trung_binh):
#     if diem_trung_binh >= 9:
#         return "XUAT SAC"
#     elif diem_trung_binh >= 8:
#         return "GIOI"
#     elif diem_trung_binh >= 7:
#         return "KHA"
#     elif diem_trung_binh >= 5:
#         return "TB"
#     else:
#         return "YEU"
# n = int(input())
# danh_sach_hoc_sinh = []
# for i in range(n):
#     ho_ten = input()
#     diem = list(map(float, input().split()))
#     diem_trung_binh = tinh_diem_trung_binh(diem)
#     loai = xep_loai(diem_trung_binh)
#     ma_hoc_sinh = "HS" + "{:02d}".format(i+1)
#     hoc_sinh = (ma_hoc_sinh, ho_ten, diem_trung_binh, loai)
#     danh_sach_hoc_sinh.append(hoc_sinh)

# # Sắp xếp danh sách học sinh theo điểm trung bình giảm dần
# danh_sach_hoc_sinh.sort(key=lambda x: (-x[2], x[0]))

# # In danh sách học sinh đã sắp xếp
# for hoc_sinh in danh_sach_hoc_sinh:
#     ma_hoc_sinh, ho_ten, diem_trung_binh, loai = hoc_sinh
#     print(f"{ma_hoc_sinh} {ho_ten} {round(diem_trung_binh,1)} {loai}")
