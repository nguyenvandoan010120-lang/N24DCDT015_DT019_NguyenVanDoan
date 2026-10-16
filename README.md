# DT019 — Tìm kiếm tuyến tính và đếm so sánh thực tế

## Thông tin sinh viên
- **Họ tên:** Nguyễn Văn Đoàn
- **MSSV:** N24DCDT015
- **Lớp:** D24CQDT01-N
- **Mã đề:** DT019

## Mô tả đề tài
Tìm vị trí xuất hiện đầu tiên của x trong mảng bằng quét từ trái sang phải.
Đếm số phép so sánh và phân tích trường hợp tốt nhất, xấu nhất.

## Cấu trúc
- `src/DeTai.py`: Các hàm thuật toán (tim_tuyen_tinh, tim_va_dem, trung_binh_so_sanh)
- `test/test_DeTai.py`: 12 ca kiểm thử (T01-T12) và 4 kiểm tra bổ sung (V01-V04)
- `demo.py`: 8 ca demo minh họa
- `docs/anh_ket_qua/`: 11 ảnh minh chứng

## Cách chạy

```bash
python demo.py --ca=1        # Chạy ca demo 1 (đến --ca=8)
python test/test_DeTai.py    # Chạy bộ kiểm thử