# ============================================================
# DT019 - Tìm kiếm tuyến tính và đếm so sánh thực tế
# Sinh viên: Nguyễn Văn Đoàn
# MSSV: N24DCDT015
# Lớp: D24CQDT01-N
# ============================================================

def kiem_tra_dau_vao(a, x):
    """
    Kiểm tra dữ liệu đầu vào theo phiếu DT019:
    - Kích thước mảng n từ 0 đến 10000
    - x phải là số nguyên
    """
    if len(a) > 10000:
        raise ValueError("Kích thước mảng n không được vượt quá 10000")
    if not isinstance(x, int):
        raise TypeError("x phải là số nguyên")
    return True

def tim_tuyen_tinh(a, x):
    """
    Tìm vị trí đầu tiên của x trong mảng a (1-based).
    Trả về 0 nếu không tìm thấy.
    """
    for i in range(len(a)):
        if a[i] == x:
            return i + 1
    return 0

def tim_va_dem(a, x):
    """
    Tìm vị trí đầu tiên của x và đếm số phép so sánh thực tế.
    """
    so_sanh = 0
    for i in range(len(a)):
        so_sanh += 1
        if a[i] == x:
            return i + 1, so_sanh
    return 0, so_sanh

def trung_binh_so_sanh(n):
    """
    Tính số phép so sánh trung bình lý thuyết (n+1)/2.
    Điều kiện: các phần tử trong mảng phân biệt và x chắc chắn có trong mảng.
    """
    if n == 0:
        return 0.0
    return (n + 1) / 2.0

def giai_bai(a, x):
    """
    Hàm gọi chính thực hiện toàn bộ quy trình bài toán.
    """
    kiem_tra_dau_vao(a, x)
    vi_tri, so_sanh = tim_va_dem(a, x)
    return {"vi_tri": vi_tri, "so_sanh": so_sanh}