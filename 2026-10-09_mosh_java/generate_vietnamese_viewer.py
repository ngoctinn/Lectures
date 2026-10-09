import json, os, re

out_dir = "/home/ngoctin/Lectures/2026-10-09_mosh_java"

# 1. Load grounded slides
with open(os.path.join(out_dir, "slides_grounded.json"), "r", encoding="utf-8") as f:
    slides = json.load(f)

canonical_slides = [s for s in slides if s.get("dedup", {}).get("is_canonical")]

# 2. Chapters data with Vietnamese titles & summaries
chapters_data = [
    (0, 106, "00:00", "01:46", "Giới thiệu khóa học", "Giới thiệu tổng quan về ngôn ngữ lập trình Java, lộ trình học tập từ cơ bản đến nâng cao cho người mới bắt đầu.", "Introduction"),
    (106, 239, "01:46", "03:59", "Cài đặt Java & Môi trường", "Hướng dẫn tải và cài đặt JDK (Java Development Kit) và IDE IntelliJ IDEA để bắt đầu lập trình.", "Installing Java"),
    (239, 521, "03:59", "08:41", "Cấu trúc một chương trình Java", "Tìm hiểu về Class, Function/Method, hàm main, quy tắc đặt tên PascalCase và camelCase.", "Anatomy of a Java Program"),
    (521, 959, "08:41", "15:59", "Chương trình Java đầu tiên", "Viết và chạy chương trình Hello World, sử dụng lệnh System.out.println() và biên dịch bằng javac.", "Your First Java Program"),
    (959, 989, "15:59", "16:29", "Tài liệu tóm tắt (Cheat Sheet)", "Các tài liệu ghi nhớ nhanh cú pháp cốt lõi của Java dành cho lập trình viên.", "Cheat Sheet"),
    (989, 1374, "16:29", "22:54", "Cơ chế thực thi của Java (JVM & Bytecode)", "Mã nguồn .java được biên dịch thành Bytecode .class, sau đó máy ảo Java (JVM) dịch thành Machine Code (WORA).", "How Java Code Gets Executed"),
    (1374, 1522, "22:54", "25:22", "Cấu trúc khóa học", "Lộ trình các chủ đề tiếp theo: Kiểu dữ liệu, luồng điều khiển, dự án thực tế và viết Clean Code.", "Course Structure"),
    (1522, 1557, "25:22", "25:57", "Tổng quan về Kiểu dữ liệu (Types)", "Giới thiệu sự phân chia giữa kiểu nguyên thủy (Primitive Types) và kiểu tham chiếu (Reference Types).", "Types"),
    (1557, 1747, "25:57", "29:07", "Biến và Khởi tạo biến (Variables)", "Cách khai báo biến, gán giá trị và quy tắc đặt tên biến có ý nghĩa trong Java.", "Variables"),
    (1747, 2067, "29:07", "34:27", "8 Kiểu dữ liệu nguyên thủy (Primitive Types)", "Chi tiết về byte, short, int, long (hậu tố L), float (hậu tố F), double, char và boolean.", "Primitive Types"),
    (2067, 2355, "34:27", "39:15", "Kiểu dữ liệu tham chiếu (Reference Types)", "Làm việc với Object, từ khóa new, lớp Date và cơ chế cấp phát bộ nhớ trên Heap.", "Reference Types"),
    (2355, 2619, "39:15", "43:39", "So sánh Primitive vs Reference Types", "Sự khác biệt vùng nhớ: Primitive lưu trực tiếp trên Stack (copy giá trị), Reference lưu địa chỉ trỏ tới Heap.", "Primitive Types vs Reference Types"),
    (2619, 3042, "43:39", "50:42", "Chuỗi ký tự (Strings)", "Tính bất biến (immutability) của String, các hàm hữu ích: length(), replace(), toLowerCase(), indexOf().", "Strings"),
    (3042, 3202, "50:42", "53:22", "Ký tự thoát (Escape Sequences)", "Sử dụng dấu gạch chéo ngược: \\n (xuống dòng), \\t (tab), \\\" (ngoặc kép), \\\\ (dấu gạch chéo).", "Escape Sequences"),
    (3202, 3527, "53:22", "58:47", "Mảng (Arrays)", "Khai báo mảng 1 chiều, kích thước cố định, sử dụng Arrays.toString() và Arrays.sort().", "Arrays"),
    (3527, 3683, "58:47", "1:01:23", "Mảng đa chiều (Multi-Dimensional Arrays)", "Khởi tạo ma trận 2D, 3D và hiển thị bằng Arrays.deepToString().", "Multi-Dimensional Arrays"),
    (3683, 3795, "1:01:23", "1:03:15", "Hằng số (Constants)", "Sử dụng từ khóa final để cố định giá trị biến, quy ước đặt tên VIẾT_HOA.", "Constants"),
    (3795, 4038, "1:03:15", "1:07:18", "Biểu thức số học (Arithmetic Expressions)", "Phép cộng, trừ, nhân, chia, chia lấy dư (%), toán tử tăng giảm ++x và x++.", "Arithmetic Expressions"),
    (4038, 4120, "1:07:18", "1:08:40", "Thứ tự ưu tiên toán tử (Order of Operations)", "Quy tắc PEMDAS: Dấu ngoặc () ưu tiên cao nhất, đến nhân/chia (*, /, %), sau cùng là cộng/trừ (+, -).", "Order of Operations"),
    (4120, 4508, "1:08:40", "1:15:08", "Ép kiểu (Casting & Type Conversion)", "Ép kiểu ngầm định (Implicit) và ép kiểu tường minh (Explicit), chuyển chuỗi sang số Integer.parseInt().", "Casting"),
    (4508, 4790, "1:15:08", "1:19:50", "Lớp toán học (The Math Class)", "Các hàm tiện ích: Math.round(), Math.ceil(), Math.floor(), Math.max(), Math.random().", "The Math Class"),
    (4790, 5140, "1:19:50", "1:25:40", "Định dạng số và tiền tệ (Formatting Numbers)", "Sử dụng NumberFormat để định dạng tiền tệ ($) và phần trăm (%) theo Locale chuẩn.", "Formatting Numbers"),
    (5140, 5445, "1:25:40", "1:30:45", "Nhập dữ liệu từ bàn phím (Reading Input)", "Sử dụng lớp Scanner đọc dữ liệu từ System.in: scanner.next(), scanner.nextLine(), scanner.nextInt().", "Reading Input"),
    (5445, 5575, "1:30:45", "1:32:55", "Dự án: Máy tính trả góp thế chấp (Mô tả)", "Đề bài ứng dụng Mortgage Calculator: Nhập số tiền vay, lãi suất hàng năm, thời hạn vay.", "Project: Mortgage Calculator"),
    (5575, 5834, "1:32:55", "1:37:14", "Dự án: Giải thuật Mortgage Calculator (v1)", "Áp dụng công thức tài chính tính toán tiền trả góp hàng tháng và hiển thị định dạng tiền tệ.", "Solution: Mortgage Calculator"),
    (5834, 5923, "1:37:14", "1:38:43", "Tóm tắt chương Kiểu dữ liệu", "Ôn tập toàn bộ kiến thức về biến, kiểu dữ liệu, mảng, toán tử và ép kiểu trong Java.", "Types Summary"),
    (5923, 5970, "1:38:43", "1:39:30", "Tổng quan về Điều khiển luồng (Control Flow)", "Giới thiệu các cấu trúc ra quyết định và lặp lại trong lập trình.", "Control Flow"),
    (5970, 6076, "1:39:30", "1:41:16", "Toán tử so sánh (Comparison Operators)", "Các toán tử điều kiện: ==, !=, >, >=, <, <= trả về giá trị boolean.", "Comparison Operators"),
    (6076, 6352, "1:41:16", "1:45:52", "Toán tử logic (Logical Operators)", "Toán tử AND (&&), OR (||), NOT (!) và cơ chế ngắt mạch tính toán (Short-circuit Evaluation).", "Logical Operators"),
    (6352, 6618, "1:45:52", "1:50:18", "Câu lệnh rẽ nhánh (If Statements)", "Cấu trúc if, else if, else để điều khiển các luồng thực thi điều kiện khác nhau.", "If Statements"),
    (6618, 6827, "1:50:18", "1:53:47", "Đơn giản hóa câu lệnh If", "Kỹ thuật viết code ngắn gọn, loại bỏ các biến boolean trung gian thừa thãi.", "Simplifying If Statements"),
    (6827, 6976, "1:53:47", "1:56:16", "Toán tử ba ngôi (Ternary Operator)", "Cú pháp rút gọn biểu thức điều kiện: condition ? valueIfTrue : valueIfFalse.", "The Ternary Operator"),
    (6976, 7207, "1:56:16", "2:00:07", "Câu lệnh Switch (Switch Statements)", "Rẽ nhánh nhiều trường hợp rời rạc với case, break và default.", "Switch Statements"),
    (7207, 7565, "2:00:07", "2:06:05", "Bài tập phỏng vấn: FizzBuzz", "Giải bài toán FizzBuzz kinh điển: chia hết cho 5 ra Fizz, cho 3 ra Buzz, cho cả hai ra FizzBuzz.", "Exercise: FizzBuzz"),
    (7565, 7793, "2:06:05", "2:09:53", "Vòng lặp For (For Loops)", "Cú pháp vòng lặp for khi biết trước số lần lặp, biến đếm i.", "For Loops"),
    (7793, 8059, "2:09:53", "2:14:19", "Vòng lặp While (While Loops)", "Vòng lặp while thực thi khi điều kiện còn đúng, xử lý nhập lệnh 'quit' từ người dùng.", "While Loops"),
    (8059, 8136, "2:14:19", "2:15:36", "Vòng lặp Do...While", "Cấu trúc vòng lặp luôn thực hiện ít nhất 1 lần trước khi kiểm tra điều kiện.", "Do...While Loops"),
    (8136, 8332, "2:15:36", "2:18:52", "Lệnh Break và Continue", "break để thoát vòng lặp ngay lập tức, continue để bỏ qua lần lặp hiện tại sang lần tiếp theo.", "Break and Continue"),
    (8332, 8519, "2:18:52", "2:21:59", "Vòng lặp For-Each", "Cách duyệt nhanh các phần tử trong mảng hoặc danh sách cực kỳ trực quan và sạch sẽ.", "For-Each Loop"),
    (8519, 8607, "2:21:59", "2:23:27", "Dự án: Mortgage Calculator (v2 - Yêu cầu)", "Nâng cấp dự án: Bổ sung vòng lặp kiểm tra tính hợp lệ của dữ liệu nhập (Input Validation).", "Project: Mortgage Calculator (v2)"),
    (8607, 8908, "2:23:27", "2:28:28", "Dự án: Giải pháp Mortgage Calculator (v2)", "Hoàn thiện mã nguồn với vòng lặp while(true) và thông báo lỗi nếu nhập ngoài khoảng cho phép.", "Solution: Mortgage Calculator (v2)"),
    (8908, 8965, "2:28:28", "2:29:25", "Tóm tắt chương Điều khiển luồng", "Tổng kết kiến thức về điều kiện logic, rẽ nhánh và các loại vòng lặp trong Java.", "Control Flow Summary"),
    (8965, 9048, "2:29:25", "2:30:48", "Nguyên tắc viết code sạch (Clean Coding)", "Quy tắc đặt tên biến rõ nghĩa, tránh magic numbers, giữ hàm ngắn gọn và định dạng code chuẩn.", "Clean Coding")
]

chapters_json = []
for idx, (s_start, s_end, t_start, t_end, title_vi, desc_vi, title_en) in enumerate(chapters_data):
    matched = [s for s in canonical_slides if s_start <= s.get("timestamp_start", 0) <= s_end]
    frames = [s.get("filename") for s in matched if s.get("filename")]
    chapters_json.append({
        "id": idx + 1,
        "start": s_start,
        "end": s_end,
        "start_str": t_start,
        "end_str": t_end,
        "title": title_vi,
        "title_en": title_en,
        "desc": desc_vi,
        "frames": frames[:4]
    })

chapters_json_str = json.dumps(chapters_json, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Khóa học Java Toàn diện cho Người mới bắt đầu — Ghi chú & Video Đồng bộ</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0f172a;
      --panel: #1e293b;
      --panel-border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #f59e0b;
      --badge-bg: #0369a1;
      --code-bg: #090d16;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    header {{
      background: #090d16;
      border-bottom: 1px solid var(--panel-border);
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
    }}
    .logo-area {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .badge {{
      background: var(--badge-bg);
      color: #fff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    h1.course-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text);
    }}
    .meta-tags {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .search-box {{
      position: relative;
      width: 320px;
    }}
    .search-box input {{
      width: 100%;
      background: var(--panel);
      border: 1px solid var(--panel-border);
      color: var(--text);
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      font-size: 0.88rem;
      outline: none;
      transition: all 0.2s;
    }}
    .search-box input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }}

    /* Main layout */
    .main-container {{
      flex: 1;
      display: grid;
      grid-template-columns: minmax(480px, 1.25fr) minmax(400px, 1fr);
      min-height: 0;
      overflow: hidden;
    }}

    /* Left pane: Video & Current playing */
    .video-section {{
      background: #000;
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--panel-border);
      min-height: 0;
    }}
    .video-wrapper {{
      flex: 1;
      position: relative;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 0;
    }}
    video {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #000;
    }}
    .video-bar {{
      background: var(--panel);
      border-top: 1px solid var(--panel-border);
      padding: 0.75rem 1.2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-shrink: 0;
    }}
    .playing-info {{
      font-size: 0.88rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }}
    .time-indicator {{
      color: var(--accent);
      font-family: 'Fira Code', monospace;
      font-weight: 600;
    }}

    /* Right pane: Course Curriculum & Slides */
    .notes-section {{
      background: var(--bg);
      display: flex;
      flex-direction: column;
      min-height: 0;
    }}
    .section-header {{
      background: var(--panel);
      border-bottom: 1px solid var(--panel-border);
      padding: 0.75rem 1.2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
    }}
    .section-header h2 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .curriculum-list {{
      flex: 1;
      overflow-y: auto;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
    }}

    /* Chapter card */
    .chapter-card {{
      background: var(--panel);
      border: 1px solid var(--panel-border);
      border-radius: 10px;
      padding: 1rem;
      transition: all 0.25s ease;
      cursor: pointer;
    }}
    .chapter-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    }}
    .chapter-card.active {{
      border-color: var(--primary);
      background: #1e3a5f;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.4);
    }}
    .card-top {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 0.35rem;
    }}
    .chapter-title {{
      font-weight: 700;
      font-size: 0.98rem;
      color: #fff;
    }}
    .chapter-timestamp {{
      font-family: 'Fira Code', monospace;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--primary);
      background: rgba(56, 189, 248, 0.12);
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      flex-shrink: 0;
    }}
    .chapter-en {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 0.45rem;
      font-style: italic;
    }}
    .chapter-desc {{
      font-size: 0.86rem;
      color: #cbd5e1;
      line-height: 1.5;
      margin-bottom: 0.75rem;
    }}

    /* Slide gallery inside card */
    .slide-gallery {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 0.5rem;
      margin-top: 0.5rem;
      padding-top: 0.5rem;
      border-top: 1px dashed rgba(255, 255, 255, 0.1);
    }}
    .slide-thumb {{
      position: relative;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      aspect-ratio: 16/9;
      background: #000;
    }}
    .slide-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.2s;
    }}
    .slide-thumb:hover img {{
      transform: scale(1.08);
    }}

    /* Lightbox Modal for slides */
    .modal {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      z-index: 999;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .modal.open {{ display: flex; }}
    .modal img {{
      max-width: 90vw;
      max-height: 85vh;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8);
      border: 1px solid var(--panel-border);
    }}

    /* Scrollbar */
    ::-webkit-scrollbar {{ width: 6px; }}
    ::-webkit-scrollbar-track {{ background: var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background: var(--panel-border); border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--text-muted); }}

    /* Switch mode buttons */
    .player-mode-switch {{
      display: flex;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 3px;
      gap: 4px;
    }}
    .mode-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}
    .mode-btn:hover {{
      color: var(--text);
    }}
    .mode-btn.active {{
      background: var(--primary);
      color: #0f172a;
    }}
    .yt-container {{
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }}
    .yt-container iframe {{
      width: 100%;
      height: 100%;
      border: none;
    }}

    @media (max-width: 900px) {{
      .main-container {{ grid-template-columns: 1fr; grid-template-rows: 40vh 1fr; }}
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo-area">
      <span class="badge">Lecture to Notes</span>
      <h1 class="course-title">Java Full Course for Beginners</h1>
      <span class="meta-tags">• Giảng viên: Mosh Hamedani • Thời lượng: 2h 30m</span>
    </div>
    <div style="display: flex; align-items: center; gap: 1rem;">
      <div class="player-mode-switch">
        <button class="mode-btn active" id="btnModeYt" onclick="setPlayerMode('yt')">
          ▶️ YouTube Trực tuyến
        </button>
        <button class="mode-btn" id="btnModeLocal" onclick="setPlayerMode('local')">
          💾 Video Cục bộ (Offline)
        </button>
      </div>
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="Tìm kiếm chương bài học hoặc từ khóa...">
      </div>
    </div>
  </header>

  <div class="main-container">
    <!-- Left column: Video player -->
    <div class="video-section">
      <div class="video-wrapper">
        <!-- YouTube Player -->
        <div id="ytContainer" class="yt-container">
          <div id="ytPlayer"></div>
        </div>
        <!-- Local Video Player -->
        <video id="mainPlayer" controls preload="metadata" style="display: none;">
          <source src="video.mp4" type="video/mp4">
          Trình duyệt của bạn không hỗ trợ thẻ video cục bộ.
        </video>
      </div>
      <div class="video-bar">
        <div class="playing-info">
          <span>Đang phát:</span>
          <span class="time-indicator" id="timeDisplay">00:00</span>
          <strong id="currentChapterName">01. Giới thiệu khóa học</strong>
        </div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">
          <span id="playerStatusHint">⚡ Bấm vào bất kỳ thẻ bài học nào bên phải để tua video tự động</span>
        </div>
      </div>
    </div>

    <!-- Right column: Vietnamese curriculum -->
    <div class="notes-section">
      <div class="section-header">
        <h2>📑 Danh mục 43 Bài học (Kèm Slide bóc tách)</h2>
        <span style="font-size: 0.82rem; color: var(--text-muted);" id="chapCount">43 chương</span>
      </div>
      <div class="curriculum-list" id="curriculumList">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <!-- Modal zoom slide -->
  <div class="modal" id="imageModal" onclick="this.classList.remove('open')">
    <img id="modalImg" src="">
  </div>

  <!-- YouTube IFrame API -->
  <script src="https://www.youtube.com/iframe_api"></script>

  <script>
    const chapters = {chapters_json_str};
    let currentMode = 'yt'; // 'yt' or 'local'
    let ytPlayer = null;
    let ytReady = false;

    const localPlayer = document.getElementById('mainPlayer');
    const ytContainer = document.getElementById('ytContainer');
    const timeDisplay = document.getElementById('timeDisplay');
    const currentChapterName = document.getElementById('currentChapterName');
    const listContainer = document.getElementById('curriculumList');
    const searchInput = document.getElementById('searchInput');
    const imageModal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const btnModeYt = document.getElementById('btnModeYt');
    const btnModeLocal = document.getElementById('btnModeLocal');
    const playerStatusHint = document.getElementById('playerStatusHint');

    // YouTube API Ready Callback
    window.onYouTubeIframeAPIReady = function() {{
      ytPlayer = new YT.Player('ytPlayer', {{
        height: '100%',
        width: '100%',
        videoId: 'eIrMbAQSU34',
        playerVars: {{
          'playsinline': 1,
          'rel': 0,
          'modestbranding': 1
        }},
        events: {{
          'onReady': () => {{
            ytReady = true;
          }}
        }}
      }});
    }};

    function setPlayerMode(mode) {{
      currentMode = mode;
      if (mode === 'yt') {{
        btnModeYt.classList.add('active');
        btnModeLocal.classList.remove('active');
        ytContainer.style.display = 'block';
        localPlayer.style.display = 'none';
        localPlayer.pause();
        playerStatusHint.textContent = '⚡ Đang phát trực tuyến từ YouTube (Full HD 1080p)';
      }} else {{
        btnModeLocal.classList.add('active');
        btnModeYt.classList.remove('active');
        ytContainer.style.display = 'none';
        localPlayer.style.display = 'block';
        if (ytReady && ytPlayer && ytPlayer.pauseVideo) {{
          ytPlayer.pauseVideo();
        }}
        playerStatusHint.textContent = '💾 Đang phát từ file video.mp4 cục bộ';
      }}
    }}

    function seekToTime(seconds) {{
      if (currentMode === 'yt') {{
        if (ytReady && ytPlayer && ytPlayer.seekTo) {{
          ytPlayer.seekTo(seconds, true);
          ytPlayer.playVideo();
        }}
      }} else {{
        localPlayer.currentTime = seconds;
        localPlayer.play().catch(e => {{
          console.warn('Local play failed, switching to YouTube', e);
          alert('Không tìm thấy file video.mp4 cục bộ hoặc trình duyệt không hỗ trợ. Tự động chuyển sang YouTube!');
          setPlayerMode('yt');
          seekToTime(seconds);
        }});
      }}
    }}

    function formatTime(sec) {{
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
    }}

    function renderChapters(items) {{
      listContainer.innerHTML = '';
      items.forEach(c => {{
        const card = document.createElement('div');
        card.className = 'chapter-card';
        card.id = 'chapter-' + c.id;
        card.dataset.start = c.start;
        card.dataset.end = c.end;

        let slidesHtml = '';
        if (c.frames && c.frames.length > 0) {{
          slidesHtml = '<div class="slide-gallery">' +
            c.frames.map(f => `
              <div class="slide-thumb" onclick="event.stopPropagation(); openImage('slides/${{f}}')">
                <img src="slides/${{f}}" alt="Slide" loading="lazy" onerror="this.onerror=null; this.src='https://img.youtube.com/vi/eIrMbAQSU34/mqdefault.jpg'">
              </div>
            `).join('') +
            '</div>';
        }}

        card.innerHTML = `
          <div class="card-top">
            <span class="chapter-title">${{c.id < 10 ? '0' + c.id : c.id}}. ${{c.title}}</span>
            <span class="chapter-timestamp">${{c.start_str}}</span>
          </div>
          <div class="chapter-en">${{c.title_en}}</div>
          <div class="chapter-desc">${{c.desc}}</div>
          ${{slidesHtml}}
        `;

        card.addEventListener('click', () => {{
          seekToTime(c.start);
        }});

        listContainer.appendChild(card);
      }});
    }}

    function openImage(src) {{
      modalImg.src = src;
      imageModal.classList.add('open');
    }}

    // Initial render
    renderChapters(chapters);

    function updateActiveChapter(curr) {{
      timeDisplay.textContent = formatTime(curr);
      const active = chapters.find(c => curr >= c.start && curr <= c.end);
      if (active) {{
        currentChapterName.textContent = (active.id < 10 ? '0' + active.id : active.id) + '. ' + active.title;
        document.querySelectorAll('.chapter-card').forEach(card => card.classList.remove('active'));
        const activeCard = document.getElementById('chapter-' + active.id);
        if (activeCard) {{
          activeCard.classList.add('active');
        }}
      }}
    }}

    // Periodic sync for YouTube Player
    setInterval(() => {{
      if (currentMode === 'yt' && ytReady && ytPlayer && ytPlayer.getCurrentTime) {{
        try {{
          const curr = ytPlayer.getCurrentTime();
          if (curr !== undefined) {{
            updateActiveChapter(curr);
          }}
        }} catch (err) {{}}
      }}
    }}, 600);

    // Sync for Local Player
    localPlayer.addEventListener('timeupdate', () => {{
      if (currentMode === 'local') {{
        updateActiveChapter(localPlayer.currentTime);
      }}
    }});

    localPlayer.addEventListener('error', () => {{
      if (currentMode === 'local') {{
        playerStatusHint.textContent = '⚠️ File video.mp4 cục bộ không khả dụng. Khuyên dùng chế độ YouTube.';
      }}
    }});

    // Search filter
    searchInput.addEventListener('input', (e) => {{
      const term = e.target.value.toLowerCase().trim();
      const filtered = chapters.filter(c => 
        c.title.toLowerCase().includes(term) ||
        c.title_en.toLowerCase().includes(term) ||
        c.desc.toLowerCase().includes(term)
      );
      renderChapters(filtered);
    }});
  </script>
</body>
</html>
"""

# Write to viewer_tieng_viet.html and index.html
with open(os.path.join(out_dir, "viewer_tieng_viet.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated viewer_tieng_viet.html and index.html successfully!")
