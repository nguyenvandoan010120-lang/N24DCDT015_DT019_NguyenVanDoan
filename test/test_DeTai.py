# ============================================================
# test_DeTai.py - Bộ kiểm thử cho DT019
# Sinh viên: Nguyễn Văn Đoàn
# MSSV: N24DCDT015
# ============================================================

import unittest
import sys
import os

# Thêm đường dẫn src/ vào sys.path để import được DeTai
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from DeTai import tim_tuyen_tinh, tim_va_dem, trung_binh_so_sanh, kiem_tra_dau_vao


class TestDT019(unittest.TestCase):

    # ========================================================
    # 5 CA BẮT BUỘC TRONG PHIẾU
    # ========================================================

    def test_T01_vi_du_1(self):
        """T01: Ví dụ 1 - tìm thấy ở đầu"""
        self.assertEqual(tim_va_dem([4, 7, 4], 4), (1, 1))

    def test_T02_vi_du_2(self):
        """T02: Ví dụ 2 - không tìm thấy"""
        self.assertEqual(tim_va_dem([4, 7, 4], 9), (0, 3))

    def test_T03_tim_thay_o_cuoi(self):
        """T03: Tìm thấy ở cuối mảng"""
        self.assertEqual(tim_va_dem([1, 2, 3], 3), (3, 3))

    def test_T04_mang_mot_phan_tu(self):
        """T04: Mảng một phần tử, tìm thấy"""
        self.assertEqual(tim_va_dem([8], 8), (1, 1))

    def test_T05_mang_rong(self):
        """T05: Mảng rỗng"""
        self.assertEqual(tim_va_dem([], 5), (0, 0))

    # ========================================================
    # 7 CA BỔ SUNG
    # ========================================================

    def test_T06_tim_thay_o_giua(self):
        """T06: Tìm thấy ở giữa mảng"""
        self.assertEqual(tim_va_dem([10, 20, 30], 20), (2, 2))

    def test_T07_phan_tu_trung_lap(self):
        """T07: Phần tử trùng, trả vị trí đầu tiên"""
        self.assertEqual(tim_va_dem([2, 2, 2], 2), (1, 1))

    def test_T08_so_am(self):
        """T08: Mảng có số âm"""
        self.assertEqual(tim_va_dem([-3, -1, -2], -1), (2, 2))

    def test_T09_tim_tuyen_tinh_tra_vi_tri(self):
        """T09: Hàm tim_tuyen_tinh trả đúng vị trí"""
        self.assertEqual(tim_tuyen_tinh([1, 2, 3, 4], 3), 3)

    def test_T10_tim_tuyen_tinh_khong_thay(self):
        """T10: Hàm tim_tuyen_tinh trả 0 khi không có"""
        self.assertEqual(tim_tuyen_tinh([1, 2, 3], 5), 0)

    def test_T11_trung_binh_so_sanh(self):
        """T11: Trung bình số so sánh với n=5 phải bằng 3.0"""
        # Sửa lại: Hàm trung_binh_so_sanh giờ nhận vào số nguyên n, không phải mảng
        self.assertAlmostEqual(trung_binh_so_sanh(5), 3.0, places=5)

    def test_T12_kiem_tra_dau_vao(self):
        """T12: Hàm validator phải chặn mảng quá lớn và x không phải số nguyên"""
        # Mảng > 10000 phần tử phải báo lỗi ValueError
        with self.assertRaises(ValueError):
            kiem_tra_dau_vao([1] * 10001, 5)
        # x không phải số nguyên phải báo lỗi TypeError
        with self.assertRaises(TypeError):
            kiem_tra_dau_vao([1, 2, 3], "abc")
        # Mảng hợp lệ phải trả về True
        self.assertTrue(kiem_tra_dau_vao([1, 2, 3], 5))

    # ========================================================
    # 4 KIỂM TRA BỔ SUNG (VALIDATOR / BẤT BIẾN)
    # ========================================================

    def test_V01_dem_tang_truoc_khi_so_sanh(self):
        """V01: Đếm phải tăng trước khi so sánh - tìm ở cuối cần n so sánh"""
        _, dem = tim_va_dem([1, 2, 3, 4, 5], 5)
        self.assertEqual(dem, 5)

    def test_V02_khong_tim_thay_can_n_so_sanh(self):
        """V02: Không tìm thấy cần đúng n so sánh"""
        _, dem = tim_va_dem([1, 2, 3], 99)
        self.assertEqual(dem, 3)

    def test_V03_vi_tri_1_based(self):
        """V03: Vị trí phải là 1-based, không phải 0-based"""
        vi_tri, _ = tim_va_dem([10, 20, 30], 10)
        self.assertEqual(vi_tri, 1)   # Phải là 1, không phải 0

    def test_V04_trung_binh_khop_cong_thuc(self):
        """V04: Trung bình phải khớp (n+1)/2 với mảng phân biệt"""
        n = 7
        tb = trung_binh_so_sanh(n) # Sửa lại: Truyền n vào
        self.assertAlmostEqual(tb, (n + 1) / 2, places=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)