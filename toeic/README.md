# Kho Tài Liệu Luyện Thi TOEIC

Kho lưu trữ và hệ thống bài giảng luyện thi TOEIC được chuẩn hóa theo quy chuẩn ghi chú học tập 2 tầng, phân loại theo phong cách giảng dạy và từng giai đoạn mục tiêu điểm số.

---

## 1. Phân loại theo giảng viên & Lộ trình học tập

```
toeic/
├── ms-tham/      # Giai đoạn 1: Xây nền tảng ngữ pháp & từ vựng cốt lõi (Mục tiêu: 0 - 500)
├── anh-le/       # Giai đoạn 2: Luyện đề ETS & mẹo thực chiến tốc độ (Mục tiêu: 500 - 750+)
└── ms-thanh/     # Giai đoạn 3: Bóc bẫy đề thi, Collocations & Reading chuyên sâu (Mục tiêu: 700 - 850+)
```

### [Ms Thắm TOEIC](file:///home/ngoctin/Lectures/toeic/ms-tham) - Nền tảng cốt lõi
* **Trọng tâm:** Bản chất ngữ pháp (12 thì, Mệnh đề quan hệ, Cụm danh từ, Thể bị động, Phân tích thành phần câu S-V-O).
* **Mục đích:** Xây gốc vững chắc, hiểu cặn kẽ cấu trúc câu, tránh học vẹt.
* **Đối tượng:** Người mất gốc, bắt đầu học lại từ đầu hoặc hay bị nhầm lẫn các câu ngữ pháp căn bản.

### [Anh Lê TOEIC](file:///home/ngoctin/Lectures/toeic/anh-le) - Thực chiến & Tối ưu tốc độ
* **Trọng tâm:** Giải đề Full Test bộ ETS, kỹ thuật nhận diện đáp án nhanh 5-10 giây, mẹo loại trừ, quản lý thời gian thi.
* **Mục đích:** Nâng phản xạ phòng thi và kéo điểm cấp tốc.
* **Đối tượng:** Đã có nền tảng cơ bản, cần luyện giải đề liên tục để chuẩn bị thi.

### [Ms Thanh TOEIC](file:///home/ngoctin/Lectures/toeic/ms-thanh) - Bóc bẫy & Bứt phá điểm
* **Trọng tâm:** Bóc tách bẫy tinh vi trong format đề thi mới, học từ vựng theo cụm (Collocation), kỹ thuật dịch hiểu và xử lý đoạn dài Part 7.
* **Mục đích:** Khắc phục tình trạng chững điểm ở mốc 500-600, tối ưu hóa điểm số Part 5 và Part 7.
* **Đối tượng:** Trình độ trung cấp muốn bứt phá lên mốc 750 - 850+.

---

## 2. Danh mục bài học hiện có

### Thư mục `anh-le/`
* [Giải chi tiết đề thi TOEIC 2025](file:///home/ngoctin/Lectures/toeic/anh-le/giai-chi-tiet-de-thi-toeic-2025-anhle-toeic/giai-chi-tiet-de-thi-toeic-2025-anhle-toeic.md) (Thời lượng: 02:15:31)
* [Giải chi tiết đề thi TOEIC mới nhất](file:///home/ngoctin/Lectures/toeic/anh-le/giải-chi-tiết-đề-thi-toeic-mới-nhất-anhle-toeic/giải-chi-tiết-đề-thi-toeic-mới-nhất-anhle-toeic.md) (Thời lượng: 02:14:40)

### Thư mục `ms-thanh/`
* [Chỉ mục bài giảng & Danh sách TODO](file:///home/ngoctin/Lectures/toeic/ms-thanh/TODO.md) (10 bài giảng đã hoàn tất, 9 video kênh phụ `@anhngumsthanh_2` chờ xử lý)
* [Tổng quan thư mục Ms Thanh](file:///home/ngoctin/Lectures/toeic/ms-thanh/README.md) (Tổng hợp 10 bài giảng chuyên sâu đã ghi chú)

### Thư mục `ms-tham/`
* *(Sẵn sàng trích xuất bài giảng ngữ pháp nền tảng bằng `/ytbknot`)*

---

## 3. Quy chuẩn tạo Note bài học mới

Khi tạo bài note mới bằng `ytbknot`, hãy lưu vào thư mục tương ứng theo cú pháp:

```bash
# Ví dụ trích xuất video bài giảng Ms Thắm vào thư mục ms-tham
ytbknot "<URL_YOUTUBE>" --output-base "toeic/ms-tham" --clean-ads

# Ví dụ trích xuất video giải đề của Anh Lê vào thư mục anh-le
ytbknot "<URL_YOUTUBE>" --output-base "toeic/anh-le" --clean-ads

# Ví dụ trích xuất video của Ms Thanh vào thư mục ms-thanh
ytbknot "<URL_YOUTUBE>" --output-base "toeic/ms-thanh" --clean-ads
```
