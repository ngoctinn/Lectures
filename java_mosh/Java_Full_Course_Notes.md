# ☕ Java Full Course for Beginners — Comprehensive Lecture Notes
> **Giảng viên**: Mosh Hamedani (*Programming with Mosh*)  
> **Thời lượng**: 2 giờ 30 phút 48 giây  
> **Nguồn video**: [YouTube - Java Full Course for Beginners](https://youtu.be/eIrMbAQSU34)  
> **Định dạng tài liệu**: Obsidian Vault / Markdown Study Guide (Biên soạn theo chuẩn `lecture-to-notes`)

---

## 📑 Mục lục tổng quan

- [Phần 1: Giới thiệu & Cài đặt môi trường](#phần-1-giới-thiệu--cài-đặt-môi-trường)
  - [1.1 Tổng quan về Java & Anatomy of a Java Program](#11-tổng-quan-về-java--anatomy-of-a-java-program)
  - [1.2 Cơ chế thực thi của Java Code (JVM & Bytecode)](#12-cơ-chế-thực-thi-của-java-code-jvm--bytecode)
- [Phần 2: Kiểu dữ liệu & Biến (Data Types & Variables)](#phần-2-kiểu-dữ-liệu--biến-data-types--variables)
  - [2.1 Primitive Types vs Reference Types](#21-primitive-types-vs-reference-types)
  - [2.2 Chuỗi ký tự (Strings) & Ký tự thoát (Escape Sequences)](#22-chuỗi-ký-tự-strings--ký-tự-thoát-escape-sequences)
  - [2.3 Mảng (Arrays & Multi-Dimensional Arrays)](#23-mảng-arrays--multi-dimensional-arrays)
  - [2.4 Hằng số (Constants) & Biểu thức toán học](#24-hằng-số-constants--biểu-thức-toán-học)
  - [2.5 Ép kiểu (Casting & Type Conversion)](#25-ép-kiểu-casting--type-conversion)
  - [2.6 Lớp Math & Định dạng số (NumberFormat)](#26-lớp-math--định-dạng-số-numberformat)
  - [2.7 Đọc dữ liệu người dùng (Scanner)](#27-đọc-dữ-liệu-người-dùng-scanner)
- [Phần 3: Dự án thực hành 1 — Mortgage Calculator (Cơ bản)](#phần-3-dự-án-thực-hành-1--mortgage-calculator-cơ-bản)
- [Phần 4: Luồng điều khiển (Control Flow)](#phần-4-luồng-điều-khiển-control-flow)
  - [4.1 Toán tử so sánh & Logic (Comparison & Logical Operators)](#41-toán-tử-so-sánh--logic-comparison--logical-operators)
  - [4.2 Câu lệnh rẽ nhánh: If-Else & Ternary Operator](#42-câu-lệnh-rẽ-nhánh-if-else--ternary-operator)
  - [4.3 Câu lệnh Switch](#43-câu-lệnh-switch)
  - [4.4 Bài tập phỏng vấn kinh điển: FizzBuzz](#44-bài-tập-phỏng-vấn-kinh-điển-fizzbuzz)
  - [4.5 Các cấu trúc vòng lặp (For, While, Do-While, For-Each)](#45-các-cấu-trúc-vòng-lặp-for-while-do-while-for-each)
- [Phần 5: Dự án thực hành 2 — Mortgage Calculator (Nâng cao với Validation)](#phần-5-dự-án-thực-hành-2--mortgage-calculator-nâng-cao-với-validation)
- [Phần 6: Tóm tắt nguyên tắc viết code sạch (Clean Code Practices)](#phần-6-tóm-tắt-nguyên-tắc-viết-code-sạch-clean-code-practices)

---

## Phần 1: Giới thiệu & Cài đặt môi trường

### 1.1 Tổng quan về Java & Anatomy of a Java Program
- `0:00:00 - 0:15:59`
- **Java là gì?** Được phát triển bởi James Gosling tại Sun Microsystems vào năm 1995 (nay thuộc Oracle). Java là ngôn ngữ lập trình hướng đối tượng (OOP), an toàn, mạnh mẽ và phổ biến nhất thế giới trên di động (Android), ứng dụng doanh nghiệp (Enterprise), điện toán đám mây và hệ thống nhúng.
- **Môi trường phát triển**:
  - **JDK (Java Development Kit)**: Chứa trình biên dịch (`javac`), thư viện cốt lõi và JRE.
  - **JRE (Java Runtime Environment)**: Môi trường chạy ứng dụng Java cho người dùng cuối.
  - **IDE khuyên dùng**: IntelliJ IDEA (Community hoặc Ultimate).

#### Cấu trúc một chương trình Java cơ bản:
```java
package com.codewithmosh;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
- **Quy tắc đặt tên (Naming Conventions)**:
  - **Class**: Viết theo chuẩn `PascalCase` (ví dụ: `Main`, `MortgageCalculator`).
  - **Method / Variable**: Viết theo chuẩn `camelCase` (ví dụ: `printMessage`, `calculateInterestRate`).
- **Điểm vào (Entry Point)**: Mọi ứng dụng Java đều bắt đầu thực thi từ phương thức `main`:
  `public static void main(String[] args)`
- **Dấu chấm phẩy (`;`)**: Mọi câu lệnh trong Java đều bắt buộc kết thúc bằng dấu chấm phẩy.

---

### 1.2 Cơ chế thực thi của Java Code (JVM & Bytecode)
- `0:16:29 - 0:22:54`
- Trong các ngôn ngữ như C/C++, code sau khi compile sẽ biến thành **Machine Code** phụ thuộc trực tiếp vào kiến trúc phần cứng (x86, ARM, Windows, Mac, Linux).
- Trong Java, triết lý là **"Write Once, Run Anywhere" (WORA)**:
  1. **Source Code**: File mã nguồn `.java`.
  2. **Java Compiler (`javac`)**: Biên dịch mã `.java` thành mã trung gian gọi là **Bytecode** (File `.class`).
  3. **JVM (Java Virtual Machine)**: Mỗi hệ điều hành (Windows, macOS, Linux) cài đặt một JVM riêng. JVM sẽ đọc file Bytecode và dịch theo thời gian thực thành mã máy tương ứng của thiết bị đó.

---

## Phần 2: Kiểu dữ liệu & Biến (Data Types & Variables)

### 2.1 Primitive Types vs Reference Types
- `0:25:22 - 0:43:38`
- Trong Java, kiểu dữ liệu được chia làm 2 nhóm lớn:

#### Bảng so sánh 8 kiểu nguyên thủy (Primitive Types):
| Kiểu dữ liệu | Kích thước bộ nhớ | Khoảng giá trị | Ví dụ khai báo |
|---|---|---|---|
| `byte` | 1 byte | -128 đến 127 | `byte age = 30;` |
| `short` | 2 bytes | -32K đến 32K | `short year = 2026;` |
| `int` | 4 bytes | -2 tỷ đến 2 tỷ | `int viewsCount = 123_456_789;` (dùng dấu `_` để dễ đọc) |
| `long` | 8 bytes | Rất lớn | `long views = 3_123_456_789L;` *(bắt buộc thêm hậu tố `L`)* |
| `float` | 4 bytes | Số thực dấu phẩy động | `float price = 10.99F;` *(bắt buộc thêm hậu tố `F`)* |
| `double` | 8 bytes | Số thực độ chính xác cao | `double price = 10.99;` (mặc định) |
| `char` | 2 bytes | 1 ký tự Unicode | `char letter = 'A';` *(dấu nháy đơn)* |
| `boolean` | 1 byte | `true` hoặc `false` | `boolean isEligible = true;` |

#### Kiểu tham chiếu (Reference Types):
- Dùng để lưu trữ các đối tượng phức tạp. Cần dùng từ khóa `new` để cấp phát bộ nhớ (trừ `String`).
- Ví dụ:
  ```java
  import java.util.Date;

  Date now = new Date();
  System.out.println(now.getTime());
  ```
- **Sự khác biệt vùng nhớ (Memory Management)**:
  - **Primitive Types**: Giá trị được lưu trực tiếp trên **Stack**. Khi gán `x = y`, giá trị được copy độc lập.
  - **Reference Types**: Đối tượng thực tế được lưu trên **Heap**, biến trên **Stack** chỉ lưu địa chỉ trỏ tới vùng nhớ đó. Khi gán `point2 = point1`, cả 2 biến cùng trỏ về một đối tượng trên Heap.

---

### 2.2 Chuỗi ký tự (Strings) & Ký tự thoát (Escape Sequences)
- `0:43:39 - 0:53:21`
- `String` trong Java là một Reference Type nhưng được tối ưu cách viết rút gọn:
  ```java
  String message = "Hello World" + "!!";
  ```
- **Tính bất biến (Immutability)**: Chuỗi trong Java là không thể thay đổi sau khi tạo. Bất kỳ phương thức nào biến đổi chuỗi đều trả về một chuỗi mới:
  - `message.endsWith("!!")`: kiểm tra hậu tố (trả về `boolean`).
  - `message.length()`: độ dài chuỗi.
  - `message.indexOf("e")`: vị trí ký tự đầu tiên (trả về `-1` nếu không có).
  - `message.replace("!", "*")`: thay thế ký tự/chuỗi.
  - `message.toLowerCase()` / `message.toUpperCase()`.
  - `message.trim()`: xóa khoảng trắng thừa ở 2 đầu.
- **Escape Sequences**:
  - `\"` : Chèn dấu ngoặc kép.
  - `\\` : Chèn dấu gạch chéo ngược.
  - `\n` : Xuống dòng mới (New line).
  - `\t` : Dấu tab căn lề.

---

### 2.3 Mảng (Arrays & Multi-Dimensional Arrays)
- `0:53:22 - 1:01:22`
- **Mảng 1 chiều**: Có kích thước cố định sau khi khởi tạo.
  ```java
  import java.util.Arrays;

  // Cách 1: Khởi tạo với kích thước
  int[] numbers = new int[5];
  numbers[0] = 1;
  numbers[1] = 2;

  // Cách 2: Khởi tạo kèm giá trị
  int[] list = { 2, 3, 5, 1, 4 };
  Arrays.sort(list); // Sắp xếp mảng tăng dần

  // In mảng (Dùng Arrays.toString)
  System.out.println(Arrays.toString(list)); // [1, 2, 3, 4, 5]
  ```
- **Mảng đa chiều (Multi-Dimensional Arrays)**:
  ```java
  int[][] matrix = new int[2][3]; // 2 hàng 3 cột
  matrix[0][0] = 1;

  int[][] matrix2 = { { 1, 2, 3 }, { 4, 5, 6 } };
  System.out.println(Arrays.deepToString(matrix2)); // [[1, 2, 3], [4, 5, 6]]
  ```

---

### 2.4 Hằng số (Constants) & Biểu thức toán học
- `1:01:23 - 1:08:39`
- **Hằng số**: Sử dụng từ khóa `final`. Tên hằng số quy ước viết hoa toàn bộ:
  ```java
  final float PI = 3.14F;
  ```
- **Phép chia số nguyên**:
  `int result = 10 / 3;` sẽ ra `3` (phần dư bị bỏ).
  Muốn ra số thập phân, phải ép kiểu ít nhất 1 toán hạng:
  `double result = (double)10 / (double)3;` -> `3.3333333333333335`
- **Toán tử tăng/giảm (`++`, `--`)**:
  - `x++` (Postfix): Trả về giá trị trước rồi mới tăng.
  - `++x` (Prefix): Tăng giá trị trước rồi mới trả về.
- **Thứ tự ưu tiên toán tử (Order of Operations)**:
  `()` -> `* / %` -> `+ -`.

---

### 2.5 Ép kiểu (Casting & Type Conversion)
- `1:08:40 - 1:15:07`
- **Ép kiểu ngầm định (Implicit / Widening Casting)**: Tự động xảy ra khi kiểu nhỏ được chuyển thành kiểu lớn hơn (không mất mát dữ liệu):
  `byte -> short -> int -> long -> float -> double`
  ```java
  short x = 1;
  int y = x + 2; // x tự động ép thành int
  ```
- **Ép kiểu tường minh (Explicit / Narrowing Casting)**: Phải chỉ định rõ khi chuyển từ kiểu lớn sang kiểu nhỏ:
  ```java
  double x = 1.1;
  int y = (int)x + 2; // y = 3 (mất phần thập phân)
  ```
- **Chuyển chuỗi thành số**:
  - `Integer.parseInt("123")` -> `123`
  - `Double.parseDouble("12.34")` -> `12.34`

---

### 2.6 Lớp Math & Định dạng số (NumberFormat)
- `1:15:08 - 1:25:39`
- **Các phương thức trong `Math`**:
  - `Math.round(1.1F)` -> `1` (Làm tròn)
  - `Math.ceil(1.1F)` -> `2` (Làm tròn lên)
  - `Math.floor(1.1F)` -> `1` (Làm tròn xuống)
  - `Math.max(1, 2)` / `Math.min(1, 2)`
  - `Math.random()`: Tạo số ngẫu nhiên từ `0.0` đến `1.0`. Muốn số nguyên từ 0 đến 100:
    ```java
    int randomInt = (int) Math.round(Math.random() * 100);
    ```
- **Định dạng tiền tệ và phần trăm (`NumberFormat`)**:
  ```java
  import java.text.NumberFormat;

  // Định dạng tiền tệ theo locale
  NumberFormat currency = NumberFormat.getCurrencyInstance();
  String money = currency.format(1234567.891); // "$1,234,567.89"

  // Định dạng phần trăm
  NumberFormat percent = NumberFormat.getPercentInstance();
  String rate = percent.format(0.1); // "10%"
  ```

---

### 2.7 Đọc dữ liệu người dùng (Scanner)
- `1:25:40 - 1:30:44`
```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("Enter your name: ");
String name = scanner.nextLine().trim(); // Đọc cả dòng có khoảng trắng

System.out.print("Enter your age: ");
byte age = scanner.nextByte();

System.out.println("You are " + name + ", " + age + " years old.");
```

---

## Phần 3: Dự án thực hành 1 — Mortgage Calculator (Cơ bản)
- `1:30:45 - 1:37:13`
- **Bài toán**: Tính số tiền phải trả góp thế chấp hàng tháng theo công thức tài chính:
  $$M = P \frac{r(1 + r)^n}{(1 + r)^n - 1}$$
  - $P$ (Principal): Tiền gốc vay (ví dụ $100,000).
  - $r$ (Monthly Interest Rate): Lãi suất tháng = Lãi suất năm / 100 / 12.
  - $n$ (Number of Payments): Tổng số tháng trả góp = Số năm * 12.

#### Mã nguồn Java hoàn chỉnh:
```java
import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal ($1K - $1M): ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate: ");
        float annualInterest = scanner.nextFloat();
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period (Years): ");
        byte years = scanner.nextByte();
        int numberOfPayments = years * MONTHS_IN_YEAR;

        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: " + mortgageFormatted);
    }
}
```

---

## Phần 4: Luồng điều khiển (Control Flow)

### 4.1 Toán tử so sánh & Logic (Comparison & Logical Operators)
- `1:38:43 - 1:45:51`
- **Toán tử so sánh**: `==`, `!=`, `>`, `>=`, `<`, `<=`
- **Toán tử Logic**:
  - `&&` (AND): Tất cả điều kiện phải đúng.
  - `||` (OR): Chỉ cần ít nhất 1 điều kiện đúng.
  - `!` (NOT): Nghịch đảo giá trị boolean.
- **Short-circuit Evaluation**: Nếu vế trái của `&&` là `false`, Java không bao giờ tính toán vế phải. Tương tự, nếu vế trái của `||` là `true`, vế phải được bỏ qua ngay lập tức.

---

### 4.2 Câu lệnh rẽ nhánh: If-Else & Ternary Operator
- `1:45:52 - 1:56:15`
- **Cú pháp If - Else If - Else cơ bản**:
  ```java
  int temp = 32;
  if (temp > 30) {
      System.out.println("It's a hot day");
      System.out.println("Drink plenty of water");
  } else if (temp > 20) {
      System.out.println("It's a nice day");
  } else {
      System.out.println("It's cold");
  }
  ```
- **Toán tử ba ngôi (Ternary Operator)**:
  Rút gọn câu lệnh gán điều kiện:
  ```java
  int income = 120_000;
  String className = (income > 100_000) ? "First" : "Economy";
  ```

---

### 4.3 Câu lệnh Switch
- `1:56:16 - 2:00:06`
- Phù hợp khi cần so sánh một biến với nhiều giá trị rời rạc cụ thể:
  ```java
  String role = "admin";
  switch (role) {
      case "admin":
          System.out.println("You're an admin");
          break; // Bắt buộc có break để tránh lọt xuống case sau (fall-through)
      case "moderator":
          System.out.println("You're a moderator");
          break;
      default:
          System.out.println("You're a guest");
  }
  ```

---

### 4.4 Bài tập phỏng vấn kinh điển: FizzBuzz
- `2:00:07 - 2:06:04`
- **Đề bài**:
  - Nhập vào một số nguyên $n$.
  - Nếu chia hết cho 5: In `"Fizz"`.
  - Nếu chia hết cho 3: In `"Buzz"`.
  - Nếu chia hết cho cả 5 và 3 (tức chia hết cho 15): In `"FizzBuzz"`.
  - Nếu không chia hết cho số nào: In lại chính số đó.

#### Mã nguồn tối ưu:
```java
import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Number: ");
        int number = scanner.nextInt();

        if (number % 15 == 0) // Điều kiện cụ thể nhất đặt lên đầu
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

### 4.5 Các cấu trúc vòng lặp (For, While, Do-While, For-Each)
- `2:06:05 - 2:21:58`

#### 1. Vòng lặp `for`
Dùng khi **biết trước** số lần lặp:
```java
for (int i = 0; i < 5; i++) {
    System.out.println("Hello World " + i);
}
```

#### 2. Vòng lặp `while`
Dùng khi **chưa biết trước** số lần lặp, lặp cho tới khi điều kiện thay đổi (ví dụ chờ người dùng nhập lệnh `"quit"`):
```java
Scanner scanner = new Scanner(System.in);
String input = "";
while (!input.equals("quit")) {
    System.out.print("Input: ");
    input = scanner.nextLine().toLowerCase();
    if (input.equals("pass"))
        continue; // Bỏ qua phần còn lại của vòng lặp, sang lần lặp kế tiếp
    if (input.equals("quit"))
        break; // Thoát hẳn khỏi vòng lặp ngay lập tức
    System.out.println(input);
}
```
> ⚠️ **Lưu ý tối quan trọng**: Không so sánh chuỗi bằng `==` trong Java (ví dụ `input == "quit"` là so sánh địa chỉ bộ nhớ). Luôn dùng phương thức `.equals()` (ví dụ `input.equals("quit")`).

#### 3. Vòng lặp `do-while`
Luôn luôn chạy ít nhất **1 lần**, sau đó mới kiểm tra điều kiện.

#### 4. Vòng lặp `for-each`
Duyệt qua mảng hoặc tập hợp cực kỳ ngắn gọn và trực quan:
```java
String[] fruits = { "Apple", "Mango", "Orange" };

for (String fruit : fruits) {
    System.out.println(fruit);
}
```

---

## Phần 5: Dự án thực hành 2 — Mortgage Calculator (Nâng cao với Validation)
- `2:21:59 - 2:28:27`
- Nâng cấp dự án tính thế chấp: Kiểm tra đầu vào chặt chẽ bằng vòng lặp `while(true)`. Nếu người dùng nhập sai khoảng giá trị cho phép, chương trình sẽ báo lỗi và yêu cầu nhập lại cho đến khi hợp lệ.

#### Mã nguồn dự án hoàn chỉnh:
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

        // 1. Validate Principal (Khoản vay từ $1,000 đến $1,000,000)
        while (true) {
            System.out.print("Principal ($1K - $1M): ");
            principal = scanner.nextInt();
            if (principal >= 1000 && principal <= 1_000_000)
                break;
            System.out.println("Enter a number between 1,000 and 1,000,000.");
        }

        // 2. Validate Annual Interest Rate (Lãi suất từ > 0% đến 30%)
        while (true) {
            System.out.print("Annual Interest Rate: ");
            float annualInterest = scanner.nextFloat();
            if (annualInterest > 0 && annualInterest <= 30) {
                monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Enter a value greater than 0 and less than or equal to 30.");
        }

        // 3. Validate Period (Thời hạn vay từ 1 đến 30 năm)
        while (true) {
            System.out.print("Period (Years): ");
            byte years = scanner.nextByte();
            if (years >= 1 && years <= 30) {
                numberOfPayments = years * MONTHS_IN_YEAR;
                break;
            }
            System.out.println("Enter a value between 1 and 30.");
        }

        // 4. Calculate Mortgage
        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("\n--- RESULT ---");
        System.out.println("Mortgage Monthly Payment: " + mortgageFormatted);
    }
}
```

---

## Phần 6: Tóm tắt nguyên tắc viết code sạch (Clean Code Practices)
- `2:29:25 - 2:30:48`
- **Đặt tên biến có ý nghĩa (Descriptive Names)**: Tránh dùng các ký tự vô nghĩa như `a`, `b`, `p`. Hãy dùng `principal`, `interestRate`, `numberOfPayments`.
- **Tránh Magic Numbers**: Không gõ thẳng các con số như `12`, `100` vào giữa công thức tính toán. Luôn khai báo hằng số có tên mô tả (`MONTHS_IN_YEAR`, `PERCENT`).
- **Thụt lề và format đồng nhất (Consistent Formatting)**: Sử dụng các phím tắt tự động format code trong IDE (IntelliJ: `Ctrl + Alt + L` trên Windows/Linux, `Cmd + Option + L` trên Mac).
- **Tránh lồng ghép điều kiện quá sâu (Flat over Nested)**: Ưu tiên đảo điều kiện và sử dụng `continue` hoặc `return` sớm (Guard Clauses) để giữ cho code thẳng hàng, dễ đọc.
