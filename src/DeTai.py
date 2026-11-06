# ============================================================
# DT019 - Tìm kiếm tuyến tính và đếm so sánh thực tế
# Sinh viên: Nguyễn Văn Đoàn - MSSV: N24DCDT015 - Lớp: D24CQDT01-N
# ============================================================


def kiem_tra_dau_vao(a, x):
  """Kiểm tra hợp lệ dữ liệu đầu vào theo phiếu DT019:

  - a là list, kích thước 0 <= n <= 10000
  - x là số nguyên
  """
  if not isinstance(a, list):
    raise TypeError("Dữ liệu mảng a phải là kiểu danh sách (list)")
  if len(a) > 10000:
    raise ValueError("Kích thước mảng n không được vượt quá 10000")
  if not isinstance(x, int):
    raise TypeError("Giá trị cần tìm x phải là số nguyên")
  return True


def tim_tuyen_tinh(a, x):
  """Tìm vị trí đầu tiên của x trong mảng a (1-based).

  Trả về 0 nếu không tìm thấy.
  """
  for i in range(len(a)):
    if a[i] == x:
      return i + 1
  return 0


def tim_va_dem(a, x):
  """Tìm vị trí xuất hiện đầu tiên của x, đếm số phép so sánh

  và ghi lại danh sách các vị trí đã kiểm tra (1-based).
  Trả về: tuple (vi_tri, so_sanh, cac_vi_tri_da_kiem)
  """
  so_sanh = 0
  cac_vi_tri_da_kiem = []

  for i in range(len(a)):
    so_sanh += 1
    cac_vi_tri_da_kiem.append(i + 1)  # 1-based index
    if a[i] == x:
      return i + 1, so_sanh, cac_vi_tri_da_kiem

  return 0, so_sanh, cac_vi_tri_da_kiem


def trung_binh_so_sanh(a):
  """Tính trung bình số phép so sánh thực tế trên mảng a phân biệt khi lần lượt

  lấy từng phần tử trong a làm khóa tìm kiếm, đối sánh với công thức lý thuyết
  (n+1)/2.

  Trả về: dict gồm:
  - 'tb_thuc_te': Số phép so sánh trung bình thực nghiệm
  - 'tb_ly_thuyet': Giá trị lý thuyết (n+1)/2
  - 'khop': True nếu thực tế khớp chính xác với lý thuyết
  """
  n = len(a)
  if n == 0:
    return {"tb_thuc_te": 0.0, "tb_ly_thuyet": 0.0, "khop": True}

  tong_so_sanh = 0
  for val in a:
    _, so_sanh, _ = tim_va_dem(a, val)
    tong_so_sanh += so_sanh

  tb_thuc_te = tong_so_sanh / n
  tb_ly_thuyet = (n + 1) / 2.0

  return {
      "tb_thuc_te": tb_thuc_te,
      "tb_ly_thuyet": tb_ly_thuyet,
      "khop": abs(tb_thuc_te - tb_ly_thuyet) < 1e-9,
  }


def tim_tat_ca_vi_tri(a, x):
  """Yêu cầu mở rộng (Điểm cộng): Tìm mọi vị trí xuất hiện của x.

  Hàm này KHÔNG ĐƯỢC DỪNG SỚM vì cần duyệt hết mảng để không bỏ sót các vị trí
  sau.
  """
  vi_tri_list = []
  so_sanh = 0
  for i in range(len(a)):
    so_sanh += 1
    if a[i] == x:
      vi_tri_list.append(i + 1)
  return vi_tri_list, so_sanh


def giai_bai(a, x):
  kiem_tra_dau_vao(a, x)
  vi_tri, so_sanh, da_kiem = tim_va_dem(a, x)
  return {
      "vi_tri": vi_tri,
      "so_sanh": so_sanh,
      "cac_vi_tri_da_kiem": da_kiem,
  }