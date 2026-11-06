# ============================================================
# test_DeTai.py - Bộ kiểm thử tự động cho DT019
# Sinh viên: Nguyễn Văn Đoàn - MSSV: N24DCDT015
# ============================================================

import os
import sys
import unittest

# Thêm đường dẫn src vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from DeTai import (
    giai_bai,
    kiem_tra_dau_vao,
    tim_tat_ca_vi_tri,
    tim_tuyen_tinh,
    tim_va_dem,
    trung_binh_so_sanh,
)


class TestDT019(unittest.TestCase):

  # ========================================================
  # 5 CA BẮT BUỘC THEO PHIẾU GIAO ĐỀ TÀI
  # ========================================================

  def test_T01_vi_du_1(self):
    """T01: Ví dụ 1 - tìm thấy ở đầu mảng (1-based)"""
    # Trả về: (vị trí 1, 1 phép so sánh, danh sách đã kiểm [1])
    self.assertEqual(tim_va_dem([4, 7, 4], 4), (1, 1, [1]))

  def test_T02_vi_du_2(self):
    """T02: Ví dụ 2 - không tìm thấy, duyệt hết 3 phần tử"""
    self.assertEqual(tim_va_dem([4, 7, 4], 9), (0, 3, [1, 2, 3]))

  def test_T03_tim_thay_o_cuoi(self):
    """T03: Tìm thấy ở cuối mảng (khóa ở cuối)"""
    self.assertEqual(tim_va_dem([1, 2, 3], 3), (3, 3, [1, 2, 3]))

  def test_T04_mang_mot_phan_tu(self):
    """T04: Mảng một phần tử (Biên n=1)"""
    self.assertEqual(tim_va_dem([8], 8), (1, 1, [1]))

  def test_T05_mang_rong(self):
    """T05: Mảng rỗng (Biên n=0)"""
    self.assertEqual(tim_va_dem([], 5), (0, 0, []))

  # ========================================================
  # CÁC CA BỔ SUNG & CA TỰ THIẾT KẾ
  # ========================================================

  def test_T06_tim_thay_o_giua(self):
    """T06: Tìm thấy ở giữa mảng"""
    self.assertEqual(tim_va_dem([10, 20, 30], 20), (2, 2, [1, 2]))

  def test_T07_phan_tu_trung_lap(self):
    """T07: Trùng lặp, dừng ngay lần đầu tiên"""
    self.assertEqual(tim_va_dem([2, 2, 2], 2), (1, 1, [1]))

  def test_T08_so_am(self):
    """T08: Mảng chứa số nguyên âm"""
    self.assertEqual(tim_va_dem([-3, -1, -2], -1), (2, 2, [1, 2]))

  def test_T09_tim_tuyen_tinh_tra_vi_tri(self):
    """T09: Hàm tim_tuyen_tinh trả đúng vị trí 1-based"""
    self.assertEqual(tim_tuyen_tinh([1, 2, 3, 4], 3), 3)

  def test_T10_tim_tuyen_tinh_khong_thay(self):
    """T10: Hàm tim_tuyen_tinh trả về 0 khi không có"""
    self.assertEqual(tim_tuyen_tinh([1, 2, 3], 5), 0)

  def test_T11_trung_binh_so_sanh_thuc_nghiem(self):
    """T11: Tính trung bình số so sánh trên mảng phân biệt và khớp (n+1)/2"""
    # Mảng 5 phần tử: [10, 20, 30, 40, 50] -> TB lý thuyết = (5+1)/2 = 3.0
    res = trung_binh_so_sanh([10, 20, 30, 40, 50])
    self.assertTrue(res["khop"])
    self.assertEqual(res["tb_thuc_te"], 3.0)
    self.assertEqual(res["tb_ly_thuyet"], 3.0)

  def test_T12_tim_tat_ca_vi_tri(self):
    """T12: Hàm mở rộng tìm mọi vị trí xuất hiện của x"""
    # [4, 7, 4] có số 4 ở vị trí 1 và 3, duyệt hết 3 phần tử
    vi_tri_list, so_sanh = tim_tat_ca_vi_tri([4, 7, 4], 4)
    self.assertEqual(vi_tri_list, [1, 3])
    self.assertEqual(so_sanh, 3)

  def test_T13_kiem_tra_dau_vao(self):
    """T13: Hàm validator chặn mảng > 10000 phần tử và x sai kiểu"""
    with self.assertRaises(ValueError):
      kiem_tra_dau_vao([1] * 10001, 5)
    with self.assertRaises(TypeError):
      kiem_tra_dau_vao([1, 2, 3], "abc")

  # ========================================================
  # CÁC PHÉP KIỂM BẤT BIẾN
  # ========================================================

  def test_V01_dem_dung_so_phan_tu_da_kiem(self):
    """V01: Số phép so sánh phải đúng bằng độ dài danh sách các vị trí đã kiểm"""
    _, so_sanh, da_kiem = tim_va_dem([5, 3, 8, 1], 8)
    self.assertEqual(so_sanh, len(da_kiem))

  def test_V02_mang_rong_trung_binh(self):
    """V02: Mảng rỗng tính trung bình trả về 0.0 an toàn"""
    res = trung_binh_so_sanh([])
    self.assertEqual(res["tb_thuc_te"], 0.0)

  def test_V03_giai_bai_tra_du_field(self):
    """V03: Hàm giai_bai trả về đầy đủ các trường theo đặc tả"""
    kq = giai_bai([4, 7, 4], 4)
    self.assertIn("vi_tri", kq)
    self.assertIn("so_sanh", kq)
    self.assertIn("cac_vi_tri_da_kiem", kq)


if __name__ == "__main__":
  unittest.main(verbosity=2)