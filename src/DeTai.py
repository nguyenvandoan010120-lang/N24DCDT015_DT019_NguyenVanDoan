# ============================================================
# DT019 - Tìm kiếm tuyến tính và đếm so sánh thực tế
# Sinh viên: Nguyễn Văn Đoàn
# MSSV: N24DCDT015
# Lớp: D24CQDT01-N
# ============================================================


def tim_tuyen_tinh(a, x):
    """
    Tìm vị trí đầu tiên của x trong mảng a (1-based).
    Trả về 0 nếu không tìm thấy.

    Tham số:
    - a: list[int] - mảng số nguyên
    - x: int - giá trị cần tìm

    Trả về:
    - int: vị trí (1-based) hoặc 0
    """
    for i in range(len(a)):
        if a[i] == x:
            return i + 1   # Python 0-based -> chuyển sang 1-based
    return 0


def tim_va_dem(a, x):
    """
    Tìm vị trí đầu tiên của x và đếm số phép so sánh.
    Dừng ngay khi tìm thấy.

    Tham số:
    - a: list[int] - mảng số nguyên
    - x: int - giá trị cần tìm

    Trả về:
    - tuple (vi_tri, so_sanh)
    """
    dem = 0
    for i in range(len(a)):
        dem += 1                # Tăng đếm TRƯỚC khi so sánh
        if a[i] == x:
            return (i + 1, dem) # 1-based
    return (0, dem)


def trung_binh_so_sanh(a):
    """
    Tính trung bình số so sánh khi tìm mỗi phần tử trong mảng.
    Áp dụng cho mảng phân biệt, mỗi phần tử đều có mặt.

    Tham số:
    - a: list[int] - mảng phân biệt

    Trả về:
    - float: trung bình số so sánh
    """
    n = len(a)
    if n == 0:
        return 0.0
    tong = 0
    for x in a:
        _, dem = tim_va_dem(a, x)
        tong += dem
    return tong / n


def kiem_tra_mang(a):
    """
    Kiểm tra mảng không rỗng.

    Trả về:
    - bool: True nếu hợp lệ, False nếu rỗng
    """
    return len(a) > 0