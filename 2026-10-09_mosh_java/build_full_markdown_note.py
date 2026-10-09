# -*- coding: utf-8 -*-
"""
Script to synthesize the comprehensive, self-contained Vietnamese Markdown note
for 'Java Full Course for Beginners' adhering strictly to the lecture-to-notes quality specification.
"""
import os
import json

base_dir = "/home/ngoctin/Lectures/2026-10-09_mosh_java"

# Load slides
with open(os.path.join(base_dir, "slides_grounded.json"), "r", encoding="utf-8") as f:
    slides_data = json.load(f)

canonical = [s for s in slides_data if s.get("dedup", {}).get("is_canonical")]

# 43 Chapters with detailed content and timestamps
chapters = [
    {
        "id": 1, "start": 0, "end": 106, "start_str": "00:00", "end_str": "01:46",
        "title": "Giới thiệu khóa học", "title_en": "Introduction",
        "content": """- **Mục tiêu khóa học**: Cung cấp nền tảng lập trình Java vững chắc từ con số 0 cho người mới bắt đầu.
- **Đối tượng hướng tới**: Bất kỳ ai muốn bắt đầu học lập trình hoặc chuyển hướng sang phát triển phần mềm bằng Java.
- **Triết lý giảng dạy của Mosh Hamedani**: Học đi đôi với hành qua các ví dụ thực tế và dự án ứng dụng thực chiến (Mortgage Calculator, FizzBuzz) thay vì chỉ nhồi nhét lý thuyết sách vở.""",
        "frames": ["frame_0002.jpg", "frame_0004.jpg"]
    },
    {
        "id": 2, "start": 106, "end": 239, "start_str": "01:46", "end_str": "03:59",
        "title": "Cài đặt Java & Môi trường phát triển", "title_en": "Installing Java",
        "content": """- **JDK (Java Development Kit)**: Bộ công cụ bắt buộc dành cho lập trình viên, bao gồm:
  - **Trình biên dịch Java (`javac`)**: Dịch mã nguồn `.java` thành Bytecode `.class`.
  - **Java Runtime Environment (JRE)**: Môi trường chạy ứng dụng.
  - Các thư viện tiêu chuẩn (Java Standard Libraries).
- **IDE (Integrated Development Environment)**: Môi trường phát triển tích hợp. Khóa học sử dụng **IntelliJ IDEA** (bản Community miễn phí hoặc Ultimate), một trong những IDE mạnh mẽ và thông minh nhất cho hệ sinh thái Java hiện nay.""",
        "frames": ["frame_0005.jpg", "frame_0006.jpg", "frame_0007.jpg", "frame_0008.jpg"]
    },
    {
        "id": 3, "start": 239, "end": 521, "start_str": "03:59", "end_str": "08:41",
        "title": "Cấu trúc một chương trình Java", "title_en": "Anatomy of a Java Program",
        "content": """- **Class (Lớp)**: Trong Java, mọi dòng code đều bắt buộc phải nằm bên trong một lớp. Tên class phải đặt theo quy ước **PascalCase** (ví dụ: `Main`, `Calculator`).
- **Method / Function (Phương thức / Hàm)**: Khối lệnh thực hiện một hành động cụ thể, đặt theo quy ước **camelCase** (ví dụ: `printReport`, `calculateMonthlyPayment`).
- **Access Modifier (`public`)**: Xác định phạm vi truy cập của class/method từ các phần khác của chương trình.
- **Hàm `main` - Điểm khởi đầu (Entry Point)**:
  ```java
  public class Main {
      public static void main(String[] args) {
          // Mã nguồn chương trình bắt đầu thực thi từ đây
      }
  }
  ```
  - `public`: Cho phép JVM gọi hàm này từ bên ngoài.
  - `static`: Có thể gọi hàm mà không cần tạo đối tượng từ class `Main`.
  - `void`: Hàm không trả về giá trị nào.
  - `String[] args`: Mảng tham số dòng lệnh truyền vào khi chạy.""",
        "frames": ["frame_0009.jpg", "frame_0011.jpg", "frame_0018.jpg"]
    },
    {
        "id": 4, "start": 521, "end": 959, "start_str": "08:41", "end_str": "15:59",
        "title": "Chương trình Java đầu tiên (Hello World)", "title_en": "Your First Java Program",
        "content": """- Viết câu lệnh in chuỗi ký tự ra màn hình console:
  ```java
  package com.codewithmosh;

  public class Main {
      public static void main(String[] args) {
          System.out.println("Hello World");
      }
  }
  ```
- **Giải thích chi tiết lệnh in**:
  - `System`: Lớp hệ thống thuộc gói `java.lang`.
  - `out`: Luồng xuất chuẩn (Standard Output Stream), thuộc kiểu `PrintStream`.
  - `println()`: Phương thức in dữ liệu ra terminal kèm theo ký tự xuống dòng (`\\n`).
- **Quy tắc cú pháp**:
  - Mọi câu lệnh trong Java bắt buộc phải kết thúc bằng dấu chấm phẩy (`;`).
  - Phân biệt chữ hoa và chữ thường (Case-sensitive): `System` khác `system`.""",
        "frames": ["frame_0019.jpg", "frame_0020.jpg", "frame_0023.jpg", "frame_0024.jpg"]
    },
    {
        "id": 5, "start": 959, "end": 989, "start_str": "15:59", "end_str": "16:29",
        "title": "Tài liệu ghi nhớ nhanh cú pháp (Cheat Sheet)", "title_en": "Cheat Sheet",
        "content": """- Tóm tắt nhanh các cú pháp, từ khóa, quy tắc đặt tên và cấu trúc thư mục chuẩn trong dự án Java Maven/Gradle.
- Hỗ trợ học viên tra cứu nhanh trong quá trình học và thực hành dự án.""",
        "frames": ["frame_0033.jpg"]
    },
    {
        "id": 6, "start": 989, "end": 1374, "start_str": "16:29", "end_str": "22:54",
        "title": "Cơ chế thực thi của Java (JVM & Bytecode)", "title_en": "How Java Code Gets Executed",
        "content": """- **Mô hình truyền thống (C/C++)**:
  - Source Code → C++ Compiler → Mã máy (Machine Code nhị phân 0101).
  - Nhược điểm: Phụ thuộc cứng vào hệ điều hành và kiến trúc phần cứng CPU (Windows x86 không chạy được trên Mac ARM hay Linux).
- **Mô hình của Java — "Write Once, Run Anywhere" (WORA)**:
  1. **Source Code (`.java`)**: Mã nguồn do lập trình viên viết.
  2. **Biên dịch (`javac`)**: Trình biên dịch Java dịch mã nguồn thành **Bytecode (`.class`)**. Bytecode là một tập chỉ lệnh trừu tượng, độc lập với nền tảng phần cứng.
  3. **Máy ảo Java (JVM - Java Virtual Machine)**: Mỗi nền tảng hệ điều hành (Windows, macOS, Linux) có một phiên bản JVM riêng. JVM nạp Bytecode và dịch thành Machine Code tương thích của máy chủ tại thời điểm chạy (thông qua JIT Compiler - Just-In-Time).
  > [!note] Nhờ cơ chế này, bạn chỉ cần biên dịch file `.java` thành `.class` một lần duy nhất, sau đó có thể mang file `.class` đó chạy trên bất kỳ hệ điều hành nào có cài đặt JVM!""",
        "frames": ["frame_0034.jpg", "frame_0036.jpg", "frame_0038.jpg", "frame_0040.jpg"]
    },
    {
        "id": 7, "start": 1374, "end": 1522, "start_str": "22:54", "end_str": "25:22",
        "title": "Cấu trúc khóa học", "title_en": "Course Structure",
        "content": """- Lộ trình tổng thể của khóa học gồm 3 trụ cột lớn:
  1. **Các kiểu dữ liệu cốt lõi (Types)**: Biến, kiểu nguyên thủy, kiểu tham chiếu, mảng, toán tử, ép kiểu.
  2. **Luồng điều khiển (Control Flow)**: Rẽ nhánh if-else, switch, các vòng lặp for, while, do-while, for-each.
  3. **Clean Code & Dự án thực tế**: Áp dụng xây dựng Mortgage Calculator và giải bài toán FizzBuzz.""",
        "frames": ["frame_0047.jpg", "frame_0048.jpg", "frame_0049.jpg", "frame_0050.jpg"]
    },
    {
        "id": 8, "start": 1522, "end": 1557, "start_str": "25:22", "end_str": "25:57",
        "title": "Tổng quan về Kiểu dữ liệu (Types)", "title_en": "Types Overview",
        "content": """- Java là một ngôn ngữ **Statically-typed** (định kiểu tĩnh): Mọi biến đều phải được khai báo kiểu dữ liệu rõ ràng trước khi sử dụng và kiểu dữ liệu không thể thay đổi sau khi khai báo.
- Java phân chia dữ liệu làm 2 loại rõ rệt:
  - **Primitive Types (Kiểu nguyên thủy)**: Dùng để lưu các giá trị đơn giản (số nguyên, số thực, ký tự, boolean).
  - **Reference Types (Kiểu tham chiếu)**: Dùng để lưu các đối tượng phức tạp (String, Date, Mảng, Class tùy biến).""",
        "frames": ["frame_0052.jpg"]
    },
    {
        "id": 9, "start": 1557, "end": 1747, "start_str": "25:57", "end_str": "29:07",
        "title": "Biến và Khởi tạo biến (Variables)", "title_en": "Variables",
        "content": """- **Khai báo biến**: `type identifier = initialValue;`
  ```java
  int age = 30;
  age = 35; // Gán lại giá trị mới
  int myAge = 30;
  int herAge = myAge; // Gán giá trị biến này sang biến khác (sao chép độc lập)
  ```
- **Quy ước đặt tên**: Sử dụng `camelCase` (ví dụ: `temperature`, `userCount`, `totalAmount`).""",
        "frames": ["frame_0054.jpg", "frame_0058.jpg", "frame_0059.jpg"]
    },
    {
        "id": 10, "start": 1747, "end": 2067, "start_str": "29:07", "end_str": "34:27",
        "title": "8 Kiểu dữ liệu nguyên thủy (Primitive Types)", "title_en": "Primitive Types",
        "content": """| Kiểu dữ liệu | Kích thước | Khoảng giá trị | Ví dụ khai báo | Ghi chú quan trọng |
|---|---|---|---|---|
| `byte` | 1 byte | -128 đến 127 | `byte age = 30;` | Tiết kiệm bộ nhớ trong mảng lớn |
| `short` | 2 bytes | -32,768 đến 32,767 | `short year = 2026;` | Ít dùng |
| `int` | 4 bytes | -2 tỷ đến +2 tỷ | `int views = 123_456_789;` | Sử dụng dấu `_` phân cách hàng nghìn cho dễ đọc |
| `long` | 8 bytes | Rất lớn (-9 * 10^18) | `long count = 3_123_456_789L;` | **Bắt buộc** có hậu tố `L` hoặc `l` |
| `float` | 4 bytes | 6-7 chữ số thập phân | `float price = 10.99F;` | **Bắt buộc** có hậu tố `F` hoặc `f` |
| `double` | 8 bytes | 15 chữ số thập phân | `double ratio = 10.99;` | Kiểu số thực mặc định trong Java |
| `char` | 2 bytes | 1 ký tự Unicode | `char letter = 'A';` | Dùng dấu nháy đơn `' '`, không dùng nháy kép |
| `boolean` | 1 byte | `true` hoặc `false` | `boolean isEligible = true;` | Dùng cho biểu thức điều kiện logic |""",
        "frames": ["frame_0061.jpg", "frame_0069.jpg"]
    },
    {
        "id": 11, "start": 2067, "end": 2355, "start_str": "34:27", "end_str": "39:15",
        "title": "Kiểu dữ liệu tham chiếu (Reference Types)", "title_en": "Reference Types",
        "content": """- Dùng để lưu trữ các đối tượng phức tạp. Để tạo đối tượng, chúng ta sử dụng từ khóa `new` để cấp phát vùng nhớ:
  ```java
  import java.util.Date;

  Date now = new Date();
  System.out.println(now); // In ra ngày giờ hiện tại
  System.out.println(now.getTime()); // Trả về timestamp mili-giây
  ```
- Khác với primitive types, reference types có chứa các **phương thức (methods)** hỗ trợ tương tác với đối tượng.""",
        "frames": ["frame_0070.jpg", "frame_0072.jpg", "frame_0079.jpg"]
    },
    {
        "id": 12, "start": 2355, "end": 2619, "start_str": "39:15", "end_str": "43:39",
        "title": "So sánh Primitive vs Reference Types", "title_en": "Primitive vs Reference Types",
        "content": """- **Quản lý bộ nhớ (Stack vs Heap)**:
  - **Primitive Types**: Giá trị được lưu trực tiếp tại vị trí biến trên vùng nhớ **Stack**.
    ```java
    byte x = 1;
    byte y = x;
    x = 2;
    System.out.println(y); // In ra 1 (y không bị ảnh hưởng vì x và y nằm ở 2 ô nhớ độc lập)
    ```
  - **Reference Types**: Biến trên **Stack** chỉ lưu một **con trỏ/địa chỉ (address)** trỏ tới đối tượng thực sự được cấp phát trên vùng nhớ **Heap**.
    ```java
    import java.awt.Point;

    Point point1 = new Point(1, 1);
    Point point2 = point1; // point2 sao chép địa chỉ, cùng trỏ về 1 vùng nhớ
    point1.x = 2;
    System.out.println(point2.x); // In ra 2! (thay đổi qua point1 làm thay đổi cả point2)
    ```""",
        "frames": ["frame_0080.jpg", "frame_0081.jpg", "frame_0082.jpg", "frame_0084.jpg"]
    },
    {
        "id": 13, "start": 2619, "end": 3042, "start_str": "43:39", "end_str": "50:42",
        "title": "Chuỗi ký tự (Strings)", "title_en": "Strings",
        "content": """- `String` là một Reference Type nhưng được Java hỗ trợ cú pháp viết tắt đặc biệt:
  ```java
  String message = "Hello World" + "!!";
  ```
- **Tính bất biến (Immutability)**: Chuỗi trong Java một khi đã tạo thì **không bao giờ bị thay đổi** nội dung trong bộ nhớ. Bất kỳ phương thức nào thao tác trên chuỗi đều trả về một đối tượng `String` mới:
  - `message.endsWith("!!")`: Kiểm tra chuỗi kết thúc (trả về `boolean`).
  - `message.startsWith("Hello")`: Kiểm tra chuỗi bắt đầu.
  - `message.length()`: Đếm số lượng ký tự.
  - `message.indexOf("e")`: Tìm vị trí ký tự đầu tiên (trả về `-1` nếu không có).
  - `message.replace("!", "*")`: Thay thế ký tự/chuỗi.
  - `message.toLowerCase()` / `message.toUpperCase()`: Chuyển hoa thường.
  - `message.trim()`: Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi.""",
        "frames": ["frame_0090.jpg", "frame_0093.jpg", "frame_0096.jpg", "frame_0098.jpg"]
    },
    {
        "id": 14, "start": 3042, "end": 3202, "start_str": "50:42", "end_str": "53:22",
        "title": "Ký tự thoát (Escape Sequences)", "title_en": "Escape Sequences",
        "content": """- Dùng dấu gạch chéo ngược (`\\`) để chèn các ký tự đặc biệt vào chuỗi:
  - `\\"` : Chèn dấu ngoặc kép: `String msg = "Hello \\"Mosh\\"";`
  - `\\\\` : Chèn dấu gạch chéo ngược: `String path = "c:\\\\Windows\\\\...";`
  - `\\n` : Xuống dòng mới (New line).
  - `\\t` : Chèn một khoảng cách tab căn lề.""",
        "frames": ["frame_0105.jpg", "frame_0110.jpg"]
    },
    {
        "id": 15, "start": 3202, "end": 3527, "start_str": "53:22", "end_str": "58:47",
        "title": "Mảng một chiều (Arrays)", "title_en": "Arrays",
        "content": """- Mảng trong Java có **kích thước cố định** (fixed size), không thể mở rộng sau khi đã tạo:
  ```java
  import java.util.Arrays;

  // Cách 1: Khởi tạo với kích thước
  int[] numbers = new int[5];
  numbers[0] = 1;
  numbers[1] = 2;

  // Cách 2: Khởi tạo kèm sẵn giá trị
  int[] list = { 2, 3, 5, 1, 4 };
  System.out.println(list.length); // 5

  // Sắp xếp mảng tăng dần
  Arrays.sort(list);

  // In mảng ra console (Dùng Arrays.toString)
  System.out.println(Arrays.toString(list)); // [1, 2, 3, 4, 5]
  ```
  > [!warning] Nếu bạn dùng `System.out.println(list)` trực tiếp, Java sẽ in ra địa chỉ bộ nhớ băm (`[I@15db9742`) thay vì các phần tử!""",
        "frames": ["frame_0111.jpg", "frame_0112.jpg", "frame_0113.jpg", "frame_0114.jpg"]
    },
    {
        "id": 16, "start": 3527, "end": 3683, "start_str": "58:47", "end_str": "1:01:23",
        "title": "Mảng đa chiều (Multi-Dimensional Arrays)", "title_en": "Multi-Dimensional Arrays",
        "content": """- Dùng để lưu trữ ma trận (2 chiều) hoặc dữ liệu không gian (3 chiều):
  ```java
  import java.util.Arrays;

  // Mảng 2 chiều 2 hàng x 3 cột
  int[][] matrix = new int[2][3];
  matrix[0][0] = 1;

  // Khởi tạo trực tiếp
  int[][] matrix2 = { { 1, 2, 3 }, { 4, 5, 6 } };

  // In mảng đa chiều bằng Arrays.deepToString()
  System.out.println(Arrays.deepToString(matrix2)); // [[1, 2, 3], [4, 5, 6]]
  ```""",
        "frames": ["frame_0120.jpg", "frame_0121.jpg"]
    },
    {
        "id": 17, "start": 3683, "end": 3795, "start_str": "1:01:23", "end_str": "1:03:15",
        "title": "Hằng số (Constants)", "title_en": "Constants",
        "content": """- Dùng từ khóa `final` để biến giá trị thành bất biến (không thể gán lại).
- Quy ước đặt tên hằng số là **IN_HOA_TOAN_BO**:
  ```java
  final float PI = 3.14F;
  // PI = 1; // Báo lỗi biên dịch ngay lập tức!
  ```""",
        "frames": ["frame_0125.jpg", "frame_0126.jpg", "frame_0127.jpg"]
    },
    {
        "id": 18, "start": 3795, "end": 4038, "start_str": "1:03:15", "end_str": "1:07:18",
        "title": "Biểu thức số học (Arithmetic Expressions)", "title_en": "Arithmetic Expressions",
        "content": """- Các toán tử: `+`, `-`, `*`, `/`, `%` (chia lấy số dư).
- **Phép chia số nguyên**:
  `int result = 10 / 3;` → kết quả là `3` (phần thập phân bị cắt bỏ).
  Để lấy kết quả số thực, phải ép kiểu ít nhất 1 toán hạng:
  `double result = (double)10 / (double)3;` → `3.3333333333333335`.
- **Toán tử tăng giảm**:
  - `x++` (Postfix): Lấy giá trị của `x` sử dụng trong biểu thức trước, rồi mới tăng `x` lên 1.
  - `++x` (Prefix): Tăng `x` lên 1 trước, rồi mới lấy giá trị mới sử dụng.
  - Toán tử gán kết hợp: `x += 5;`, `x -= 2;`, `x *= 3;`.""",
        "frames": ["frame_0128.jpg", "frame_0133.jpg", "frame_0146.jpg"]
    },
    {
        "id": 19, "start": 4038, "end": 4120, "start_str": "1:07:18", "end_str": "1:08:40",
        "title": "Thứ tự ưu tiên toán tử (Order of Operations)", "title_en": "Order of Operations",
        "content": """- Tuân thủ quy tắc toán học tiêu chuẩn:
  1. Dấu ngoặc đơn `()` có độ ưu tiên cao nhất.
  2. Nhân, chia và lấy dư `*`, `/`, `%`.
  3. Cộng và trừ `+`, `-`.
  ```java
  int x = (10 + 3) * 2; // 26
  ```""",
        "frames": []
    },
    {
        "id": 20, "start": 4120, "end": 4508, "start_str": "1:08:40", "end_str": "1:15:08",
        "title": "Ép kiểu (Casting & Type Conversion)", "title_en": "Casting",
        "content": """- **Implicit Casting (Ép kiểu ngầm định)**: Xảy ra tự động khi chuyển đổi từ kiểu nhỏ sang kiểu lớn hơn, không gây mất mát dữ liệu:
  `byte → short → int → long → float → double`
  ```java
  short x = 1;
  int y = x + 2; // x tự động ép thành int -> y = 3
  ```
- **Explicit Casting (Ép kiểu tường minh)**: Bắt buộc khai báo khi ép kiểu từ kiểu lớn sang kiểu nhỏ (có nguy cơ mất dữ liệu):
  ```java
  double x = 1.1;
  int y = (int)x + 2; // x bị cắt phần thập phân thành 1 -> y = 3
  ```
- **Chuyển đổi từ Chuỗi sang Số (Wrapper Classes)**:
  - `Integer.parseInt("123")` → `123`
  - `Double.parseDouble("12.34")` → `12.34`
  - `Float.parseFloat("10.5F")` → `10.5F`""",
        "frames": ["frame_0152.jpg"]
    },
    {
        "id": 21, "start": 4508, "end": 4790, "start_str": "1:15:08", "end_str": "1:19:50",
        "title": "Lớp toán học (The Math Class)", "title_en": "The Math Class",
        "content": """- Cung cấp các hàm toán học tiện ích hữu dụng:
  - `Math.round(1.1F)` → `1` (Làm tròn số)
  - `Math.ceil(1.1F)` → `2.0` (Làm tròn lên số nguyên trần)
  - `Math.floor(1.1F)` → `1.0` (Làm tròn xuống số nguyên sàn)
  - `Math.max(1, 2)` / `Math.min(1, 2)` (Tìm giá trị lớn nhất / nhỏ nhất)
  - `Math.random()`: Sinh số thực ngẫu nhiên từ `0.0` đến `1.0`.
  - Sinh số nguyên ngẫu nhiên từ 0 đến 100:
    ```java
    int randomInt = (int) (Math.random() * 100);
    ```""",
        "frames": ["frame_0153.jpg", "frame_0154.jpg"]
    },
    {
        "id": 22, "start": 4790, "end": 5140, "start_str": "1:19:50", "end_str": "1:25:40",
        "title": "Định dạng số và tiền tệ (Formatting Numbers)", "title_en": "Formatting Numbers",
        "content": """- Sử dụng lớp trừu tượng `NumberFormat` trong gói `java.text`:
  ```java
  import java.text.NumberFormat;

  // Định dạng tiền tệ theo chuẩn địa phương ($)
  NumberFormat currency = NumberFormat.getCurrencyInstance();
  String money = currency.format(1234567.891);
  System.out.println(money); // "$1,234,567.89"

  // Định dạng phần trăm (%)
  NumberFormat percent = NumberFormat.getPercentInstance();
  String rate = percent.format(0.1);
  System.out.println(rate); // "10%"
  ```
- Kỹ thuật **Method Chaining** (Gọi chuỗi phương thức):
  `String result = NumberFormat.getPercentInstance().format(0.1);`""",
        "frames": ["frame_0161.jpg", "frame_0162.jpg", "frame_0166.jpg", "frame_0167.jpg"]
    },
    {
        "id": 23, "start": 5140, "end": 5445, "start_str": "1:25:40", "end_str": "1:30:45",
        "title": "Nhập dữ liệu từ bàn phím (Reading Input)", "title_en": "Reading Input",
        "content": """- Sử dụng lớp `Scanner` trong gói `java.util`:
  ```java
  import java.util.Scanner;

  Scanner scanner = new Scanner(System.in);

  System.out.print("Tên của bạn: ");
  String name = scanner.nextLine().trim(); // Đọc nguyên cả dòng văn bản

  System.out.print("Tuổi: ");
  byte age = scanner.nextByte(); // Đọc số byte

  System.out.println("Xin chào " + name + ", bạn " + age + " tuổi.");
  ```
  > [!tip] Dùng `scanner.next()` chỉ đọc một từ (dừng khi gặp dấu cách). Muốn đọc toàn bộ chuỗi có khoảng trắng, luôn dùng `scanner.nextLine()`. Dùng `.trim()` để loại bỏ khoảng trắng dư thừa.""",
        "frames": ["frame_0173.jpg", "frame_0174.jpg", "frame_0175.jpg", "frame_0177.jpg"]
    },
    {
        "id": 24, "start": 5445, "end": 5575, "start_str": "1:30:45", "end_str": "1:32:55",
        "title": "Dự án: Máy tính trả góp thế chấp (Mô tả)", "title_en": "Project: Mortgage Calculator",
        "content": """- **Đề bài ứng dụng Mortgage Calculator**:
  - Nhập vào số tiền vay mua nhà (Principal): ví dụ `$100,000`.
  - Nhập vào lãi suất hàng năm (Annual Interest Rate): ví dụ `3.92%`.
  - Nhập vào thời hạn vay (Period tính bằng năm): ví dụ `30` năm.
  - Áp dụng công thức tài chính để tính ra chính xác số tiền phải thanh toán hàng tháng (Mortgage) và định dạng hiển thị tiền tệ đẹp mắt.""",
        "frames": ["frame_0183.jpg", "frame_0184.jpg", "frame_0185.jpg", "frame_0186.jpg"]
    },
    {
        "id": 25, "start": 5575, "end": 5834, "start_str": "1:32:55", "end_str": "1:37:14",
        "title": "Dự án: Giải thuật Mortgage Calculator (v1)", "title_en": "Solution: Mortgage Calculator",
        "content": """- **Công thức tài chính**:
  $$M = P \\frac{r(1 + r)^n}{(1 + r)^n - 1}$$
  - $P$ (Principal): Tiền gốc vay.
  - $r$ (Monthly Interest): Lãi suất tháng = Lãi suất năm / 100 / 12.
  - $n$ (NumberOfPayments): Tổng số tháng thanh toán = Số năm * 12.
- **Mã nguồn giải thuật đầy đủ**:
  ```java
  import java.text.NumberFormat;
  import java.util.Scanner;

  public class Main {
      public static void main(String[] args) {
          final byte MONTHS_IN_YEAR = 12;
          final byte PERCENT = 100;

          Scanner scanner = new Scanner(System.in);

          System.out.print("Principal ($): ");
          int principal = scanner.nextInt();

          System.out.print("Annual Interest Rate (%): ");
          float annualInterest = scanner.nextFloat();
          float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;

          System.out.print("Period (Years): ");
          byte years = scanner.nextByte();
          int numberOfPayments = years * MONTHS_IN_YEAR;

          double mortgage = principal
                  * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                  / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

          String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
          System.out.println("Monthly Mortgage Payment: " + mortgageFormatted);
      }
  }
  ```""",
        "frames": ["frame_0187.jpg", "frame_0188.jpg", "frame_0191.jpg", "frame_0192.jpg"]
    },
    {
        "id": 26, "start": 5834, "end": 5923, "start_str": "1:37:14", "end_str": "1:38:43",
        "title": "Tóm tắt chương Kiểu dữ liệu", "title_en": "Types Summary",
        "content": """- Củng cố toàn bộ kiến thức chương 1:
  - 8 kiểu nguyên thủy lưu giá trị trên Stack.
  - Kiểu tham chiếu lưu con trỏ trỏ tới Heap.
  - Mảng cố định kích thước, String bất biến.
  - Toán tử, ép kiểu và định dạng số.""",
        "frames": ["frame_0196.jpg", "frame_0197.jpg", "frame_0198.jpg"]
    },
    {
        "id": 27, "start": 5923, "end": 5970, "start_str": "1:38:43", "end_str": "1:39:30",
        "title": "Tổng quan về Điều khiển luồng (Control Flow)", "title_en": "Control Flow",
        "content": """- Giới thiệu cách máy tính đưa ra quyết định (Rẽ nhánh) và lặp đi lặp lại một hành động (Vòng lặp) dựa trên điều kiện logic boolean.""",
        "frames": ["frame_0199.jpg", "frame_0201.jpg"]
    },
    {
        "id": 28, "start": 5970, "end": 6076, "start_str": "1:39:30", "end_str": "1:41:16",
        "title": "Toán tử so sánh (Comparison Operators)", "title_en": "Comparison Operators",
        "content": """- Luôn trả về kết quả kiểu `boolean` (`true` hoặc `false`):
  - `==` : Bằng nhau (Lưu ý: Chỉ dùng so sánh số và primitive types, KHÔNG dùng so sánh String).
  - `!=` : Khác nhau.
  - `>`, `>=` : Lớn hơn, lớn hơn hoặc bằng.
  - `<`, `<=` : Nhỏ hơn, nhỏ hơn hoặc bằng.""",
        "frames": ["frame_0201.jpg", "frame_0203.jpg"]
    },
    {
        "id": 29, "start": 6076, "end": 6352, "start_str": "1:41:16", "end_str": "1:45:52",
        "title": "Toán tử logic (Logical Operators)", "title_en": "Logical Operators",
        "content": """- Kết hợp nhiều biểu thức boolean:
  - `&&` (AND): Tất cả điều kiện thành phần phải đúng thì kết quả mới là `true`.
  - `||` (OR): Chỉ cần ít nhất một điều kiện đúng thì kết quả là `true`.
  - `!` (NOT): Đảo ngược giá trị boolean (`!true` thành `false`).
- **Short-circuit Evaluation (Đoản mạch tính toán)**:
  - Trong `A && B`: Nếu `A` là `false`, Java bỏ qua không tính toán `B`.
  - Trong `A || B`: Nếu `A` là `true`, Java bỏ qua không tính toán `B`.""",
        "frames": ["frame_0208.jpg", "frame_0209.jpg", "frame_0210.jpg", "frame_0211.jpg"]
    },
    {
        "id": 30, "start": 6352, "end": 6618, "start_str": "1:45:52", "end_str": "1:50:18",
        "title": "Câu lệnh rẽ nhánh (If Statements)", "title_en": "If Statements",
        "content": """```java
int temp = 32;
if (temp > 30) {
    System.out.println("Trời nóng");
    System.out.println("Hãy uống nhiều nước");
} else if (temp > 20) {
    System.out.println("Thời tiết đẹp");
} else {
    System.out.println("Trời lạnh");
}
```""",
        "frames": ["frame_0213.jpg", "frame_0215.jpg", "frame_0219.jpg"]
    },
    {
        "id": 31, "start": 6618, "end": 6827, "start_str": "1:50:18", "end_str": "1:53:47",
        "title": "Đơn giản hóa câu lệnh If (Simplifying If Statements)", "title_en": "Simplifying If Statements",
        "content": """- **Cách viết rườm rà (Người mới bắt đầu)**:
  ```java
  boolean hasHighIncome;
  if (income > 100_000)
      hasHighIncome = true;
  else
      hasHighIncome = false;
  ```
- **Cách viết chuyên nghiệp và tối ưu (Clean Code)**:
  ```java
  boolean hasHighIncome = (income > 100_000);
  ```
  Biểu thức `income > 100_000` vốn dĩ đã trả về kiểu `boolean`, hãy gán trực tiếp!""",
        "frames": ["frame_0224.jpg", "frame_0225.jpg"]
    },
    {
        "id": 32, "start": 6827, "end": 6976, "start_str": "1:53:47", "end_str": "1:56:16",
        "title": "Toán tử ba ngôi (Ternary Operator)", "title_en": "The Ternary Operator",
        "content": """- Cú pháp: `variable = (condition) ? valueIfTrue : valueIfFalse;`
  ```java
  int income = 120_000;
  String className = (income > 100_000) ? "First Class" : "Economy Class";
  ```""",
        "frames": ["frame_0230.jpg", "frame_0233.jpg"]
    },
    {
        "id": 33, "start": 6976, "end": 7207, "start_str": "1:56:16", "end_str": "2:00:07",
        "title": "Câu lệnh Switch (Switch Statements)", "title_en": "Switch Statements",
        "content": """- Thay thế chuỗi `if-else` dài khi so sánh một biến với các giá trị rời rạc:
  ```java
  String role = "admin";
  switch (role) {
      case "admin":
          System.out.println("Bạn là Quản trị viên");
          break; // Bắt buộc để tránh fall-through
      case "moderator":
          System.out.println("Bạn là Điều hành viên");
          break;
      default:
          System.out.println("Bạn là Khách");
  }
  ```""",
        "frames": ["frame_0236.jpg", "frame_0237.jpg", "frame_0238.jpg", "frame_0239.jpg"]
    },
    {
        "id": 34, "start": 7207, "end": 7565, "start_str": "2:00:07", "end_str": "2:06:05",
        "title": "Bài tập phỏng vấn kinh điển: FizzBuzz", "title_en": "Exercise: FizzBuzz",
        "content": """- **Yêu cầu bài toán**:
  - Nhập số nguyên $n$.
  - Nếu chia hết cho 5 in `"Fizz"`.
  - Nếu chia hết cho 3 in `"Buzz"`.
  - Nếu chia hết cho cả 5 và 3 (chia hết cho 15) in `"FizzBuzz"`.
  - Trường hợp còn lại in chính số đó.
- **Lời giải tối ưu**:
  ```java
  import java.util.Scanner;

  public class FizzBuzz {
      public static void main(String[] args) {
          Scanner scanner = new Scanner(System.in);
          System.out.print("Number: ");
          int number = scanner.nextInt();

          if (number % 15 == 0) // Điều kiện cụ thể nhất đặt lên đầu tiên
              System.out.println("FizzBuzz");
          else if (number % 5 == 0)
              System.out.println("Fizz");
          else if (number % 3 == 0)
              System.out.println("Buzz");
          else
              System.out.println(number);
      }
  }
  ```""",
        "frames": ["frame_0244.jpg", "frame_0245.jpg", "frame_0246.jpg", "frame_0247.jpg"]
    },
    {
        "id": 35, "start": 7565, "end": 7793, "start_str": "2:06:05", "end_str": "2:09:53",
        "title": "Vòng lặp For (For Loops)", "title_en": "For Loops",
        "content": """- Dùng khi biết trước số lần lặp:
  ```java
  for (int i = 0; i < 5; i++) {
      System.out.println("Hello World " + i);
  }
  ```""",
        "frames": ["frame_0260.jpg"]
    },
    {
        "id": 36, "start": 7793, "end": 8059, "start_str": "2:09:53", "end_str": "2:14:19",
        "title": "Vòng lặp While (While Loops)", "title_en": "While Loops",
        "content": """- Dùng khi chưa biết trước số lần lặp, vòng lặp chạy khi điều kiện còn đúng:
  ```java
  Scanner scanner = new Scanner(System.in);
  String input = "";
  while (!input.equals("quit")) {
      System.out.print("Input: ");
      input = scanner.nextLine().toLowerCase();
      System.out.println(input);
  }
  ```
  > [!important] So sánh chuỗi trong Java luôn dùng `input.equals("quit")`, không bao giờ dùng `input == "quit"`!""",
        "frames": ["frame_0261.jpg", "frame_0263.jpg", "frame_0266.jpg", "frame_0267.jpg"]
    },
    {
        "id": 37, "start": 8059, "end": 8136, "start_str": "2:14:19", "end_str": "2:15:36",
        "title": "Vòng lặp Do...While", "title_en": "Do...While Loops",
        "content": """- Luôn luôn thực thi thân vòng lặp ít nhất 1 lần trước khi kiểm tra điều kiện lặp:
  ```java
  do {
      System.out.print("Input: ");
      input = scanner.nextLine().toLowerCase();
  } while (!input.equals("quit"));
  ```""",
        "frames": ["frame_0270.jpg", "frame_0271.jpg", "frame_0277.jpg"]
    },
    {
        "id": 38, "start": 8136, "end": 8332, "start_str": "2:15:36", "end_str": "2:18:52",
        "title": "Lệnh Break và Continue", "title_en": "Break and Continue",
        "content": """- `break`: Dừng và thoát hẳn ra khỏi vòng lặp ngay lập tức.
- `continue`: Bỏ qua các lệnh còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo:
  ```java
  while (true) {
      System.out.print("Input: ");
      input = scanner.nextLine().toLowerCase();
      if (input.equals("pass"))
          continue;
      if (input.equals("quit"))
          break;
      System.out.println(input);
  }
  ```""",
        "frames": []
    },
    {
        "id": 39, "start": 8332, "end": 8519, "start_str": "2:18:52", "end_str": "2:21:59",
        "title": "Vòng lặp For-Each", "title_en": "For-Each Loop",
        "content": """- Cách duyệt nhanh qua các phần tử của mảng hoặc Collection cực kỳ ngắn gọn và trực quan:
  ```java
  String[] fruits = { "Apple", "Mango", "Orange" };

  for (String fruit : fruits) {
      System.out.println(fruit);
  }
  ```""",
        "frames": ["frame_0284.jpg"]
    },
    {
        "id": 40, "start": 8519, "end": 8607, "start_str": "2:21:59", "end_str": "2:23:27",
        "title": "Dự án: Mortgage Calculator (v2 - Yêu cầu)", "title_en": "Project: Mortgage Calculator (v2)",
        "content": """- **Nâng cấp dự án**: Kiểm tra tính hợp lệ của dữ liệu đầu vào (Input Validation):
  - Số tiền vay: từ `$1,000` đến `$1,000,000`.
  - Lãi suất hàng năm: từ `> 0%` đến `30%`.
  - Thời hạn vay: từ `1` đến `30` năm.
  - Nếu người dùng nhập sai, in thông báo lỗi và yêu cầu nhập lại cho đến khi hợp lệ.""",
        "frames": ["frame_0286.jpg", "frame_0287.jpg"]
    },
    {
        "id": 41, "start": 8607, "end": 8908, "start_str": "2:23:27", "end_str": "2:28:28",
        "title": "Dự án: Giải pháp Mortgage Calculator (v2)", "title_en": "Solution: Mortgage Calculator (v2)",
        "content": """- **Mã nguồn giải pháp hoàn chỉnh**:
  ```java
  import java.text.NumberFormat;
  import java.util.Scanner;

  public class MortgageReport {
      public static void main(String[] args) {
          final byte MONTHS_IN_YEAR = 12;
          final byte PERCENT = 100;

          int principal = 0;
          float monthlyInterest = 0;
          int numberOfPayments = 0;

          Scanner scanner = new Scanner(System.in);

          // 1. Kiểm tra Principal ($1,000 - $1,000,000)
          while (true) {
              System.out.print("Principal ($1K - $1M): ");
              principal = scanner.nextInt();
              if (principal >= 1000 && principal <= 1_000_000)
                  break;
              System.out.println("Enter a number between 1,000 and 1,000,000.");
          }

          // 2. Kiểm tra Annual Interest Rate (0% - 30%)
          while (true) {
              System.out.print("Annual Interest Rate: ");
              float annualInterest = scanner.nextFloat();
              if (annualInterest > 0 && annualInterest <= 30) {
                  monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
                  break;
              }
              System.out.println("Enter a value greater than 0 and less than or equal to 30.");
          }

          // 3. Kiểm tra Period (1 - 30 năm)
          while (true) {
              System.out.print("Period (Years): ");
              byte years = scanner.nextByte();
              if (years >= 1 && years <= 30) {
                  numberOfPayments = years * MONTHS_IN_YEAR;
                  break;
              }
              System.out.println("Enter a value between 1 and 30.");
          }

          // 4. Tính toán kết quả
          double mortgage = principal
                  * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                  / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

          String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
          System.out.println("\n--- RESULT ---");
          System.out.println("Mortgage Monthly Payment: " + mortgageFormatted);
      }
  }
  ```""",
        "frames": ["frame_0288.jpg", "frame_0289.jpg", "frame_0290.jpg", "frame_0291.jpg"]
    },
    {
        "id": 42, "start": 8908, "end": 8965, "start_str": "2:28:28", "end_str": "2:29:25",
        "title": "Tóm tắt chương Điều khiển luồng", "title_en": "Control Flow Summary",
        "content": """- Tổng kết lại các kỹ thuật:
  - So sánh điều kiện bằng boolean và toán tử logic.
  - Phân nhánh với if/else và switch.
  - Lặp có điều kiện với for, while, do-while và for-each.
  - Kiểm soát ngắt luồng với break và continue.""",
        "frames": ["frame_0299.jpg"]
    },
    {
        "id": 43, "start": 8965, "end": 9048, "start_str": "2:29:25", "end_str": "2:30:48",
        "title": "Nguyên tắc viết code sạch (Clean Coding)", "title_en": "Clean Coding",
        "content": """- **Đặt tên biến có ý nghĩa (Descriptive Names)**: Tránh viết tắt khó hiểu như `p`, `r`, `n`. Hãy dùng `principal`, `monthlyInterest`, `numberOfPayments`.
- **Tránh Magic Numbers**: Không gõ thẳng số `12`, `100` vào giữa mã lệnh tính toán. Luôn dùng hằng số `MONTHS_IN_YEAR`, `PERCENT`.
- **Thụt lề đồng nhất (Consistent Indentation)**: Giúp mã nguồn có cấu trúc rõ ràng, dễ bảo trì.
- **Tách hàm nhỏ**: Giữ cho mỗi phương thức làm một nhiệm vụ duy nhất.""",
        "frames": ["frame_0300.jpg", "frame_0301.jpg", "frame_0302.jpg"]
    }
]

# Generate Markdown content
md = []
md.append("""---
title: "Khóa học Java Toàn diện cho Người mới bắt đầu (Mosh Hamedani)"
author: "Mosh Hamedani"
channel: "Programming with Mosh"
duration: "2h 30m 48s"
language: "vi"
original_url: "https://youtu.be/eIrMbAQSU34"
tags:
  - java
  - programming
  - computer-science
  - backend
  - study-notes
---

# ☕ Khóa học Java Toàn diện cho Người mới bắt đầu (Mosh Hamedani)

> **Giảng viên**: Mosh Hamedani (*Programming with Mosh*)  
> **Thời lượng**: 2 giờ 30 phút 48 giây  
> **Link bài giảng gốc**: [YouTube - Java Full Course for Beginners](https://youtu.be/eIrMbAQSU34)  
> **Quy chuẩn tài liệu**: Định dạng chuẩn Markdown Obsidian Vault Note tự chứa đựng (Self-contained)

---

> [!summary] 🎯 CỐT LÕI BÀI HỌC (KEY TAKEAWAYS)
> 1. **Triết lý WORA (Write Once, Run Anywhere)**: Mã Java `.java` được biên dịch thành Bytecode `.class` độc lập nền tảng, sau đó máy ảo Java (JVM) trên từng hệ điều hành sẽ dịch thành Machine Code.
> 2. **Phân biệt kiểu dữ liệu**: 8 kiểu Primitive lưu trực tiếp trên **Stack**; Reference Types lưu trên **Heap** và biến chỉ lưu địa chỉ con trỏ. Chuỗi (`String`) mang tính bất biến (immutable).
> 3. **Cạm bẫy so sánh**: Không so sánh chuỗi hoặc đối tượng bằng toán tử `==` (vì nó so sánh địa chỉ bộ nhớ), luôn sử dụng phương thức `.equals()`.
> 4. **Nguyên tắc Clean Code**: Loại bỏ hoàn toàn Magic Numbers bằng hằng số `final`, đặt tên biến rõ nghĩa (`camelCase`), giữ cấu trúc code phẳng bằng Guard Clauses.

---

## 📚 Bảng thuật ngữ & Từ viết tắt

| Thuật ngữ | Tên tiếng Anh đầy đủ | Ý nghĩa & Bản chất kỹ thuật |
|---|---|---|
| **JDK** | Java Development Kit | Bộ công cụ phát triển Java chứa trình biên dịch `javac`, thư viện và JRE |
| **JRE** | Java Runtime Environment | Môi trường thời gian chạy dành cho người dùng cuối để chạy file Java |
| **JVM** | Java Virtual Machine | Máy ảo Java thực thi Bytecode và dịch sang Machine Code của máy chủ |
| **Bytecode** | Java Bytecode (`.class`) | Mã trung gian độc lập phần cứng được tạo ra bởi trình biên dịch `javac` |
| **Stack** | Stack Memory | Vùng nhớ lưu trữ các biến cục bộ và giá trị nguyên thủy (truy xuất cực nhanh) |
| **Heap** | Heap Memory | Vùng nhớ lưu trữ các đối tượng (Objects) được cấp phát động bằng từ khóa `new` |
| **WORA** | Write Once, Run Anywhere | Triết lý viết một lần, chạy mọi nơi của nền tảng Java |
| **OOP** | Object-Oriented Programming | Lập trình hướng đối tượng |
| **PEMDAS** | Order of Operations | Thứ tự ưu tiên toán tử: Dấu ngoặc () → Nhân chia → Cộng trừ |

---

## 📑 Danh mục 43 Bài học chi tiết
""")

for c in chapters:
    cid = f"{c['id']:02d}"
    youtube_link = f"https://youtu.be/eIrMbAQSU34?t={c['start']}"
    md.append(f"### {cid}. {c['title']} (`{c['title_en']}`)")
    md.append(f"- **Mốc thời gian**: [▶️ {c['start_str']} - {c['end_str']}]({youtube_link}) *(Bấm vào để xem video)*\n")
    md.append(c['content'])
    md.append("")
    
    # Embed canonical slides if present
    if c['frames']:
        md.append("**Slide bài giảng minh họa:**")
        for f in c['frames']:
            slide_path = f"slides/{f}"
            md.append(f"> [!figure] Slide minh họa: {c['title']}\n> ![{c['title']}]({slide_path})")
        md.append("")
    md.append("---\n")

md.append("""## 🛠️ Dự án thực hành cốt lõi

### 1. Ứng dụng Mortgage Calculator v2 (Bản nâng cao với Validation)
```java
package com.codewithmosh;

import java.text.NumberFormat;
import java.util.Scanner;

public class MortgageCalculator {
    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        int principal = 0;
        float monthlyInterest = 0;
        int numberOfPayments = 0;

        Scanner scanner = new Scanner(System.in);

        // 1. Kiểm tra tiền gốc ($1K - $1M)
        while (true) {
            System.out.print("Principal ($1K - $1M): ");
            principal = scanner.nextInt();
            if (principal >= 1000 && principal <= 1_000_000)
                break;
            System.out.println("Vui lòng nhập số tiền trong khoảng từ 1,000 đến 1,000,000.");
        }

        // 2. Kiểm tra lãi suất năm (> 0% đến 30%)
        while (true) {
            System.out.print("Annual Interest Rate (%): ");
            float annualInterest = scanner.nextFloat();
            if (annualInterest > 0 && annualInterest <= 30) {
                monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Vui lòng nhập lãi suất lớn hơn 0 và nhỏ hơn hoặc bằng 30.");
        }

        // 3. Kiểm tra số năm vay (1 - 30 năm)
        while (true) {
            System.out.print("Period (Years): ");
            byte years = scanner.nextByte();
            if (years >= 1 && years <= 30) {
                numberOfPayments = years * MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Vui lòng nhập số năm trong khoảng từ 1 đến 30.");
        }

        // 4. Áp dụng công thức tính tiền trả góp hàng tháng
        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("\\n==================================");
        System.out.println("Số tiền phải trả hàng tháng: " + mortgageFormatted);
        System.out.println("==================================");
    }
}
```

### 2. Thuật toán phỏng vấn FizzBuzz
```java
package com.codewithmosh;

import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập một số nguyên: ");
        int number = scanner.nextInt();

        if (number % 15 == 0)
            System.out.println("FizzBuzz");
        else if (number % 5 == 0)
            System.out.println("Fizz");
        else if (number % 3 == 0)
            System.out.println("Buzz");
        else
            System.out.println(number);
    }
}
```

---

## 📌 Hướng dẫn mở và đọc tài liệu này
- **Xem trong Obsidian**: Mở thư mục bài giảng làm một Vault, mọi hình ảnh `slides/` và callout sẽ hiển thị tuyệt đẹp.
- **Xem trong VS Code**: Mở file `.md` và nhấn tổ hợp phím `Ctrl + Shift + V` (hoặc `Cmd + Shift + V` trên Mac) để bật Markdown Preview.
- **Xem video đồng bộ**: Bấm vào bất kỳ mốc thời gian `[▶️ MM:SS]` ở từng chương để mở đúng đoạn video giảng giải tương ứng trên YouTube!
""")

full_content = "\n".join(md)

# Write to Java_Full_Course_Notes.md and README.md
note_path = os.path.join(base_dir, "Java_Full_Course_Notes.md")
readme_path = os.path.join(base_dir, "README.md")

with open(note_path, "w", encoding="utf-8") as f:
    f.write(full_content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated {note_path} and {readme_path}!")
