# 🎵 Delta Force Auto Harmonica

Công cụ tiện ích giúp chuyển đổi file MIDI hoặc bản nhạc dạng Text thành macro tự động chơi nhạc cụ Harmonica trong tựa game **Delta Force**.

Phiên bản ứng dụng Standalone (.exe) cực nhẹ, giao diện mượt mà và khả năng chơi nhạc với độ trễ bằng 0.

## ✨ Tính năng nổi bật

* 🚀 **Chạy Trực Tiếp (1-Click Run):** Tích hợp engine bắn thẳng macro vào hệ thống. Bấm "Chạy luôn" là có thể vào game quẩy ngay, không sinh file rác `.ahk` trong máy.

* ⏱️ **Đếm Nhịp Tuyệt Đối (Absolute Float Timing):** Sử dụng hàm QPC đo thời gian thực tế với sai số cấp mili-giây. Chống trôi nhịp hoàn toàn dù bài nhạc có dài hàng vạn nốt.

* 🎛️ **Auto-Fit Thông Minh:** Thuật toán tự động phân tích và dịch giọng (Transpose) bài MIDI về đúng dải âm của đàn Harmonica trong game, giảm thiểu tối đa các nốt bị lệch.

* 🖱️ **Hỗ trợ Combo Chuột Mở Rộng:** Xử lý chuẩn xác các tổ hợp nốt khó yêu cầu kết hợp chuột như Quãng Thấp (Trái), Quãng Cao (Phải), Thăng (Giữa) và các nốt ghép (VD: `#'`, `,'`).

* 🎧 **Trình Giả Lập Âm Thanh (Live Preview):** Nghe thử bản nhạc ngay trên phần mềm với âm thanh tổng hợp đa luồng (Lookahead Web Audio API) cực kỳ trung thực.

## 📥 Hướng dẫn Cài đặt & Sử dụng

### 1. Yêu cầu hệ thống

* Hệ điều hành: Windows 10 / 11.

* **BẮT BUỘC:** Phải cài đặt sẵn [**AutoHotkey v2**](https://www.autohotkey.com/) trên máy để chạy được Macro.

### 2. Tải phần mềm

Bạn không cần biết code để sử dụng. Chỉ cần:

1. Vào mục [**Releases**](../../releases) bên góc phải của trang GitHub này.

2. Tải xuống file `DeltaForceHarmonica.exe`.

### 3. Cách sử dụng trong game

1. Mở file `.exe` vừa tải.

2. Kéo thả file `.mid` / `.midi` vào phần mềm (hoặc bấm nút "Bản Nhạc Mẫu" để thử).

3. Chuyển sang tab **AHK v2** và bấm nút 🚀 **Chạy luôn**.

4. Vào game **Delta Force**, trang bị và cầm đàn Harmonica lên tay.

5. Sử dụng các phím tắt sau để điều khiển:

   * **`F8`** : Bắt đầu chơi nhạc / Dừng lại (Play/Stop).

   * **`F9`** : Tải lại macro (Reload).

   * **`F10`** : Thoát hoàn toàn macro, trả lại bàn phím bình thường (Exit).

## 💻 Dành cho Nhà Phát Triển (Build from Source)

Nếu bạn muốn chỉnh sửa mã nguồn hoặc tự build lại file `.exe`:

**1. Chuẩn bị môi trường:**

* Cài đặt [Python 3.x](https://www.python.org/downloads/).

* Cài đặt các thư viện cần thiết:

  ```
  pip install pywebview pyinstaller
  
  ```

**2. Đóng gói phần mềm:**
Mở Terminal/Command Prompt tại thư mục chứa source code và chạy lệnh:

```
pyinstaller --noconsole --onefile --add-data "index.html;." app.py

```

*(Nếu dùng Linux/MacOS, thay `index.html;.` thành `index.html:.`)*. File chạy sẽ được tạo ra trong thư mục `dist`.

## ⚠️ Cảnh báo (Disclaimer)

* *Đây là phần mềm của bên thứ 3 tạo thao tác tự động phím/chuột. Việc sử dụng macro trong các tựa game Multiplayer luôn đi kèm với rủi ro bị hệ thống Anti-cheat nhận diện. Người dùng vui lòng tự chịu trách nhiệm đối với tài khoản game của mình.*

* *Dự án này là mã nguồn mở và hoàn toàn miễn phí, không phục vụ mục đích thương mại.*