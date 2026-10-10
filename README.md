# Lectures

Kho tài liệu học tập và bài giảng kỹ thuật được trích xuất tự động từ YouTube bằng plugin **`ytbknot`** trên Google Antigravity (AGY).

---

## 1. Giới thiệu

Thư mục này lưu trữ các bài giảng kỹ thuật, khóa học lập trình và luyện thi chuyên sâu. Toàn bộ tài liệu được chuẩn hóa theo quy chuẩn **`ytbknot`**:
* **Không Emoji:** Giữ trọn tính nghiêm túc, gãy gọn của tài liệu kỹ thuật.
* **Tiêu đề ngắn gọn thuần Việt:** Không dùng ngoặc đơn chêm tiếng Anh ở tiêu đề.
* **Cấu trúc 2 tầng:**
  * *Tầng 1 (Tổng luận chuyên đề):* Đọc nhanh 5 phút nắm 100% tinh hoa, công thức và quy tắc vàng.
  * *Tầng 2 (Bóc tách chi tiết):* Đi sâu từng câu hỏi / từng mốc demo kèm đầy đủ 4 đáp án A-B-C-D và họ từ mở rộng.
* **Bộ ảnh độc lập:** Kho ảnh phân cảnh và slide nằm riêng trong thư mục `screenshots/`.

---

## 2. Danh mục bài học hiện có

* **[Quy trình kỹ sư Agentic năm 2026](file:///home/ngoctin/Lectures/yt-extract_2026-10-09_the-agentic-engineer-workflow-you-need-in-2026/yt-extract_2026-10-09_the-agentic-engineer-workflow-you-need-in-2026.md):**
  * Nguồn: IndyDevDan | Thời lượng: 18:24
  * Trọng tâm: Git Worktree, Context Window Drift, Claude Code Terminal setup và mô hình kỹ sư điều phối AI Agent.
* **[Kho tài liệu luyện thi TOEIC](file:///home/ngoctin/Lectures/toeic/README.md):**
  * Phân loại theo 3 nguồn: **Ms Thắm** (Xây nền), **Anh Lê** (Luyện đề & Mẹo), **Ms Thanh** (Bóc bẫy & Từ vựng chuyên sâu).
  * Gồm các bài giải đề ETS chi tiết tại [Anh Lê TOEIC](file:///home/ngoctin/Lectures/toeic/anh-le) và [Ms Thanh TOEIC](file:///home/ngoctin/Lectures/toeic/ms-thanh).
* **[Reading English with Eric - Peter Pan](file:///home/ngoctin/Lectures/Reading%20English%20with%20Eric/00_overview.md):**
  * Nguồn: Reading English with Eric | Thời lượng: 02:48:05 (3 tập chuyên sâu)
  * Trọng tâm: Bóc tách từng chữ tác phẩm Peter Pan của J.M. Barrie, phân tích ngữ pháp cổ điển, từ vựng theo ngữ cảnh, kỹ thuật Shadowing và 41 khung hình trích xuất ghi chú viết tay trên trang sách.

---

## 3. Cách trích xuất bài học mới bằng `ytbknot`

Trong môi trường Antigravity IDE hoặc CLI, chỉ cần gõ:

```text
/ytbknot https://www.youtube.com/watch?v=...
```

### Các tùy chọn nâng cao:
* **Chụp ảnh dày đặc theo chu kỳ (bài giảng slide):**
  ```text
  /ytbknot <URL> --interval 60
  ```
* **Lọc bỏ quảng cáo & phân đoạn tài trợ (SponsorBlock):**
  ```text
  /ytbknot <URL> --clean-ads
  ```
* **Chạy trực tiếp từ dòng lệnh:**
  ```bash
  ytbknot "<URL>" --output-base "." --interval 120 --clean-ads
  ```
