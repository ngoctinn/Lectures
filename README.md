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
* **[Giải đề TOEIC Reading Part 5](file:///home/ngoctin/Lectures/yt-extract_2026-10-09_max-%C4%91i%E1%BB%83m-reading-part-5-video-1/yt-extract_2026-10-09_max-%C4%91i%E1%BB%83m-reading-part-5-video-1.md):**
  * Nguồn: Ms Thanh Toeic | Thời lượng: 01:08:14
  * Trọng tâm: Giải chi tiết 15 câu (101 - 115) với 4 chuyên đề ngữ pháp, phân tích cặn kẽ 4 đáp án A-B-C-D và họ từ mở rộng.

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
