# ============================================================
# demo.py - Chạy thử nghiệm các ca kiểm thử cho DT019
# Sinh viên: Nguyễn Văn Đoàn
# MSSV: N24DCDT015
# Lớp: D24CQDT01-N
# ============================================================

import sys
import os

# Thêm đường dẫn thư mục src vào sys.path để import được DeTai
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from DeTai import giai_bai

def in_ket_qua(a, x, ten_ca=""):
    """Hàm phụ trợ để in kết quả ra màn hình cho đẹp"""
    print(f"\n--- {ten_ca} ---")
    print(f"Mang: {a}")
    print(f"Tim x = {x}")
    try:
        ket_qua = giai_bai(a, x)
        print(f"Ket qua: vi_tri = {ket_qua['vi_tri']}, so_sanh = {ket_qua['so_sanh']}")
    except Exception as e:
        print(f"Loi: {e}")

def main():
    # Nếu không truyền tham số, in hướng dẫn
    if len(sys.argv) < 2:
        print("Vui long chay kem tham so --ca=1 den --ca=8")
        print("Vi du: python demo.py --ca=1")
        return

    ca = sys.argv[1]

    if ca == "--ca=1":
        in_ket_qua([4, 7, 4], 4, "CA 1: Vi du 1 (Tim thay o dau)")
    elif ca == "--ca=2":
        in_ket_qua([4, 7, 4], 9, "CA 2: Vi du 2 (Khong tim thay)")
    elif ca == "--ca=3":
        in_ket_qua([1, 2, 3], 3, "CA 3: Tim thay o cuoi mang")
    elif ca == "--ca=4":
        in_ket_qua([8], 8, "CA 4: Mang mot phan tu")
    elif ca == "--ca=5":
        in_ket_qua([], 5, "CA 5: Mang rong")
    elif ca == "--ca=6":
        in_ket_qua([10, 20, 30], 20, "CA 6: Tim thay o giua mang")
    elif ca == "--ca=7":
        in_ket_qua([-3, -1, -2], -1, "CA 7: Mang co so am")
    elif ca == "--ca=8":
        print("\n--- CA 8: MINH HOA TU CHOI DU LIEU KHONG HOP LE ---")
        print("Thu 1: Mang vuot qua 10000 phan tu")
        try:
            # Tạo mảng 10001 phần tử để kích hoạt lỗi
            giai_bai([1] * 10001, 5)
        except ValueError as e:
            print(f"-> DA TU CHOI DU LIEU: {e}")
        
        print("\nThu 2: x khong phai la so nguyen (truyen vao chuoi)")
        try:
            # Truyền x là chuỗi "abc" để kích hoạt lỗi
            giai_bai([1, 2, 3], "abc")
        except TypeError as e:
            print(f"-> DA TU CHOI DU LIEU: {e}")
    else:
        print("Tham so khong hop le. Vui long chon --ca=1 den --ca=8")

if __name__ == "__main__":
    main()