# [Thực hành] Tạo bảng đơn giản với tiêu đề và dữ liệu

[![HTML5](https://img.shields.io/badge/HTML5-Table-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
[![Status](https://img.shields.io/badge/Status-Completed-22C55E?style=for-the-badge)](https://github.com/proyctk03-eng/thuc-hanh-tao-bang-html)
[![Report](https://img.shields.io/badge/File_Format-.DOCX_(195KB)-2563EB?style=for-the-badge&logo=microsoftword&logoColor=white)](Bao_Cao_Thuc_Hanh_Tao_Bang_HTML.docx)
[![Demo](https://img.shields.io/badge/Demo-GitHub_Pages-6366F1?style=for-the-badge)](https://proyctk03-eng.github.io/thuc-hanh-tao-bang-html/)

---

## 1. Mục Đích & Bài Toán
- **Mục đích**: Luyện tập tạo bảng cơ bản trong HTML sử dụng các thẻ `<table>`, `<tr>`, `<th>`, `<td>` để hiển thị dữ liệu có cấu trúc.
- **Bài toán**: Tạo một bảng hiển thị danh sách học sinh với các cột: **Họ và Tên**, **Tuổi**, **Lớp**.

---

## 2. Mã Nguồn HTML Chuẩn Theo Đề Bài (`index.html`)

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Bảng đơn giản trong HTML</title>
    </head>
    <body>
        <h2>Danh sách học sinh</h2>
        <table border="1">
            <tr>
                <th>Họ và Tên</th>
                <th>Tuổi</th>
                <th>Lớp</th>
            </tr>
            <tr>
                <td>Nguyễn Văn A</td>
                <td>15</td>
                <td>10A1</td>
            </tr>
            <tr>
                <td>Trần Thị B</td>
                <td>16</td>
                <td>11B2</td>
            </tr>
            <tr>
                <td>Lê Văn C</td>
                <td>17</td>
                <td>12C3</td>
            </tr>
        </table>
    </body>
</html>
```

---

## 3. Ảnh Chụp Màn Hình Trình Duyệt Web (Minh Chứng Nộp Bài)

Theo yêu cầu trong phần **HƯỚNG DẪN NỘP BÀI** (*"Chụp màn hình kết quả hiển thị trên trình duyệt để nộp bài"*):

![Browser Screenshot](browser_table_result_screenshot.png)

---

## 4. Sơ Đồ Cấu Trúc Thẻ & So Sánh Nâng Cấp CSS

### 4.1. Phân tầng cấu trúc HTML Table
![HTML Table Architecture](html_table_tags_architecture.png)

### 4.2. So sánh bảng HTML thuần (border="1") và bảng chuẩn hóa CSS
![Modern CSS Table Comparison](modern_css_styled_table.png)

---

## 5. Ý Nghĩa & Vai Trò Các Thẻ HTML Table

| Thẻ / Thuộc Tính | Ý Nghĩa | Chức Năng Cốt Lõi |
|:---|:---|:---|
| **`<table>`** | Table Element | Thẻ bao bọc cấp cao nhất định nghĩa cấu trúc bảng dữ liệu. |
| **`border="1"`** | Border Attribute | Thuộc tính quy định độ dày đường viền bao quanh bảng (1 pixel). |
| **`<tr>`** | Table Row | Định nghĩa một hàng ngang trong bảng. |
| **`<th>`** | Table Header | Ô tiêu đề cột. Mặc định trình duyệt hiển thị **in đậm** và căn giữa. |
| **`<td>`** | Table Data | Ô chứa dữ liệu thông thường. Mặc định hiển thị chữ thường và căn lề trái. |

---

## 6. Hướng Dẫn Nộp File Báo Cáo
- File báo cáo chính thức được xuất ra định dạng **`.docx`** theo đúng yêu cầu đề bài:
  👉 **`Bao_Cao_Thuc_Hanh_Tao_Bang_HTML.docx`** (Dung lượng: **195 KB**, đáp ứng giới hạn tối đa 2 MB).
- File PDF dự phòng:
  👉 **`Bao_Cao_Thuc_Hanh_Tao_Bang_HTML.pdf`** (Dung lượng: **479 KB**).

---

## 7. Thông Tin Học Viên
- **Học viên**: `proyctk03-eng`
- **Môn học**: Nhập môn Lập trình Web & HTML
- **Hoàn thành**: Tháng 10/2026
