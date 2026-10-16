# demo.py - Chạy thử các ca demo DT019
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from DeTai import tim_va_dem


def in_ket_qua(a, x, tieu_de=""):
    vi_tri, so_sanh = tim_va_dem(a, x)
    print(f"--- {tieu_de} ---")
    print(f"Mang: {a}")
    print(f"Tim x = {x}")
    print(f"Ket qua: vi_tri = {vi_tri}, so_sanh = {so_sanh}")
    print()


if len(sys.argv) > 1 and sys.argv[1].startswith("--ca="):
    ca = sys.argv[1]
    if ca == "--ca=1":
        print("DT019 - TIM KIEM TUYEN TINH - CA 1")
        in_ket_qua([4, 7, 4], 4, "VI DU 1: Tim thay o dau")
    elif ca == "--ca=2":
        print("DT019 - TIM KIEM TUYEN TINH - CA 2")
        in_ket_qua([4, 7, 4], 9, "VI DU 2: Khong tim thay")
    elif ca == "--ca=3":
        print("DT019 - TIM KIEM TUYEN TINH - CA 3")
        in_ket_qua([10, 20, 30, 40, 50], 30, "TU THIET KE 1: Tim thay o giua")
    elif ca == "--ca=4":
        print("DT019 - TIM KIEM TUYEN TINH - CA 4")
        in_ket_qua([5, 3, 8, 1], 8, "TU THIET KE 2: Tim thay o vi tri 3")
    elif ca == "--ca=5":
        print("DT019 - TIM KIEM TUYEN TINH - CA 5")
        in_ket_qua([8], 8, "BIEN 1: Mang mot phan tu")
    elif ca == "--ca=6":
        print("DT019 - TIM KIEM TUYEN TINH - CA 6")
        in_ket_qua([], 5, "BIEN 2: Mang rong")
    elif ca == "--ca=7":
        print("DT019 - TIM KIEM TUYEN TINH - CA 7")
        in_ket_qua([1, 2, 3, 4, 5], 5, "BIEN 3: Phan tu cuoi mang")
    elif ca == "--ca=8":
        print("DT019 - TIM KIEM TUYEN TINH - CA 8")
        in_ket_qua([], -1, "INPUT KHONG HOP LE: Mang rong, x am")
    else:
        print("Chon --ca=1 den --ca=8")
else:
    print("Chay: python demo.py --ca=1 den --ca=8")