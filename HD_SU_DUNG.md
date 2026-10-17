# HỆ THỐNG TRẮC NGHIỆM CHỦ NGHĨA XÃ HỘI KHOA HỌC (PHONG CÁCH QUIZIZZ)

Ứng dụng web ôn thi trắc nghiệm môn Chủ Nghĩa Xã Hội Khoa Học với **toàn bộ 240 câu hỏi** được trích xuất tự động và chuẩn xác 100% từ 2 file Word gốc:
- `CHỦ NGHĨA XH-KH.docx` (Bài 1 - Bài 5: 197 câu)
- `CNKHXH BAI6.docx` (Bài 6: 43 câu)

---

## ⚡ TÍNH NĂNG NỔI BẬT (PHONG CÁCH QUIZIZZ)

1. **Chọn đáp án là biết ngay kết quả (Instant Feedback)**:
   - Khi bấm vào đáp án A, B, C, D:
     - **Nếu chọn ĐÚNG**: Thẻ lập tức sáng **Xanh lá (Emerald)** rực rỡ, phát âm thanh chúc mừng vui tai (chime), hiệu ứng pháo hoa giấy (confetti), tăng điểm số và tăng chuỗi đúng (**🔥 Streak**).
     - **Nếu chọn SAI**: Thẻ bạn chọn rung nhẹ và chuyển sang **Đỏ**, đồng thời **Đáp án chuẩn đã được bôi đỏ trong tài liệu Word** sẽ lập tức phát sáng **Xanh lá** kèm nhãn `✓ CHÍNH XÁC` để bạn nhận biết và ghi nhớ ngay lập tức!
   - Hiển thị thanh thông báo kết quả tức thì cùng nút **"Câu tiếp theo ➜"** (hoặc bạn chỉ cần bấm phím **Space / Enter**).

2. **Nhận diện chuẩn xác đáp án bôi đỏ trong tài liệu Word**:
   - Tất cả các đáp án có định dạng màu chữ đỏ (`C:EE0000`, `C:FF0000`...) trong file Word gốc đã được script parser nhận diện chuẩn xác 100%.

3. **Hỗ trợ đầy đủ 4 dạng bài tập trong tài liệu**:
   - **Trắc nghiệm 1 đáp án đúng (Single Choice)**: 163 câu.
   - **Trắc nghiệm nhiều đáp án đúng (Multiple Choice - Chọn 2, 3 đáp án)**: 43 câu.
   - **Đúng / Sai theo từng mệnh đề (True / False)**: 16 câu (chọn Đúng/Sai từng ý phát hiện kết quả ngay).
   - **Kéo thả / Ghép vế tương ứng & Phân loại 2 cột (Drag & Drop / Match)**: 18 câu.

4. **Lọc câu hỏi linh hoạt**:
   - Chọn làm theo từng bài: **Bài 1 (39 câu)**, **Bài 2 (43 câu)**, **Bài 3 (38 câu)**, **Bài 4 (41 câu)**, **Bài 5 (36 câu)**, **Bài 6 (43 câu)** hoặc **Tất cả (240 câu)**.
   - Lọc theo dạng câu hỏi: 1 đáp án, nhiều đáp án, đúng/sai, kéo thả.
   - Chế độ **Xáo trộn (Shuffle)**: Ngẫu nhiên hóa thứ tự câu hỏi và thứ tự đáp án A, B, C, D.

5. **Thanh tiến độ & Bảng điều hướng câu hỏi (Drawer Navigator)**:
   - Theo dõi phần trăm hoàn thành.
   - Bảng danh sách câu hỏi 1 -> 240: Màu xanh cho câu làm đúng, màu đỏ cho câu làm sai, bấm vào số bất kỳ để nhảy ngay tới câu đó.

6. **Phím tắt tiện lợi**:
   - Bấm phím `1`, `2`, `3`, `4` hoặc `A`, `B`, `C`, `D` để chọn đáp án tương ứng.
   - Bấm `Enter`, `Space` hoặc `Mũi tên phải (➜)` để chuyển sang câu tiếp theo.
   - Bấm `Mũi tên trái (⬅)` để quay lại câu trước.

---

## 🚀 HƯỚNG DẪN CHẠY TRANG WEB TRÊN MÁY

### Cách 1: Mở trực tiếp (Không cần cài đặt, nhanh nhất)
1. Trong thư mục dự án, bạn chỉ cần nhấp đúp vào file `run_app.bat` hoặc nhấp đúp trực tiếp vào file [index.html](file:///d:/Bài%20Kiểm%20Tra%20LMS/n3k1/chủ%20nghĩa%20xã%20hội%20khoa%20học/TN/index.html).
2. Trang web sẽ mở ra ngay trên trình duyệt mặc định (Chrome, Edge, Firefox, Cốc Cốc...).

### Cách 2: Chạy qua Local Server
Mở terminal / PowerShell tại thư mục này và gõ:
```powershell
python -m http.server 8080
```
Sau đó truy cập: `http://localhost:8080` trên trình duyệt.

---

## 📁 CẤU TRÚC CÁC FILE CHÍNH

- `index.html`: Giao diện ứng dụng phong cách Quizizz.
- `style.css`: Toàn bộ hiệu ứng, thiết kế thẻ Quizizz màu sắc, chế độ sáng/tối (Dark/Light Mode).
- `script.js`: Toàn bộ logic tương tác, chấm điểm tức thì, âm thanh Web Audio, pháo hoa confetti, phím tắt.
- `questions.json`: File dữ liệu 240 câu hỏi định dạng JSON.
- `questions-data.js`: File dữ liệu câu hỏi nhúng trực tiếp dạng JS (giúp web chạy mượt mà ngay cả khi mở file offline mà không bị lỗi CORS).
- `parse_all_questions.py`: Script trích xuất và phân tích toàn bộ câu hỏi từ 2 file Word `CHỦ NGHĨA XH-KH.docx` và `CNKHXH BAI6.docx`.
- `run_app.bat`: Phím tắt mở nhanh trang web trên Windows.
