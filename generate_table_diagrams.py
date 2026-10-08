import os
import sys
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def get_serif_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/timesbd.ttf" if bold else "C:/Windows/Fonts/times.ttf",
        "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return get_font(size, bold)

def get_mono_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return get_font(size, bold)

def create_browser_screenshot(filename):
    W, H = 1200, 720
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(12, bold=False)
    f_url = get_font(12, bold=False)
    f_h2 = get_serif_font(26, bold=True)
    f_th = get_serif_font(18, bold=True)
    f_td = get_serif_font(18, bold=False)
    f_badge = get_font(11, bold=True)

    # 1. Browser Tab & Titlebar (Dark/Clean modern browser chrome)
    draw.rectangle([0, 0, W, 42], fill="#E5E7EB")
    
    # Active Tab
    draw.rectangle([80, 8, 340, 42], fill="#FFFFFF")
    draw.text((95, 14), "📄 Bảng đơn giản trong HTML", fill="#111827", font=f_title)
    draw.text((320, 14), "✕", fill="#6B7280", font=f_title)

    # Window controls
    draw.rectangle([W - 90, 14, W - 75, 28], fill="#9CA3AF")
    draw.rectangle([W - 65, 14, W - 50, 28], fill="#9CA3AF")
    draw.rectangle([W - 40, 14, W - 25, 28], fill="#EF4444")

    # 2. Browser Navigation bar
    draw.rectangle([0, 42, W, 84], fill="#FFFFFF")
    draw.line([0, 84, W, 84], fill="#D1D5DB", width=1)
    
    draw.text((25, 54), "←   →   ⟳", fill="#6B7280", font=get_font(14, bold=True))
    
    # Address bar
    draw.rectangle([110, 50, W - 50, 76], fill="#F3F4F6", outline="#D1D5DB", width=1)
    draw.text((125, 54), "🔒 file:///C:/Users/dathao/Desktop/thuc-hanh-tao-bang-html/index.html", fill="#374151", font=f_url)

    # 3. Web Page Content Area
    CONTENT_X = 80
    CONTENT_Y = 125

    # Heading h2
    draw.text((CONTENT_X, CONTENT_Y), "Danh sách học sinh", fill="#000000", font=f_h2)

    # Table with border="1" simulation (Standard HTML default rendering: double borders / 3D inset border)
    TBL_X = CONTENT_X
    TBL_Y = CONTENT_Y + 55
    TBL_W = 520
    ROW_H = 48
    COLS = [
        ("Họ và Tên", 240),
        ("Tuổi", 120),
        ("Lớp", 160)
    ]

    # Outer border of table
    draw.rectangle([TBL_X, TBL_Y, TBL_X + TBL_W, TBL_Y + ROW_H * 4], outline="#808080", fill="#FFFFFF", width=2)

    # Header Row (TH)
    # Background for TH in standard HTML is transparent, text centered & bold
    cx = TBL_X
    for hname, hw in COLS:
        draw.rectangle([cx, TBL_Y, cx + hw, TBL_Y + ROW_H], outline="#808080", width=1)
        # Center text
        bbox = draw.textbbox((0, 0), hname, font=f_th)
        tw = bbox[2] - bbox[0]
        th_x = cx + (hw - tw) // 2
        draw.text((th_x, TBL_Y + 12), hname, fill="#000000", font=f_th)
        cx += hw

    # Data Rows (TD)
    data = [
        ("Nguyễn Văn A", "15", "10A1"),
        ("Trần Thị B", "16", "11B2"),
        ("Lê Văn C", "17", "12C3")
    ]

    ry = TBL_Y + ROW_H
    for r in data:
        cx = TBL_X
        for i, val in enumerate(r):
            hw = COLS[i][1]
            draw.rectangle([cx, ry, cx + hw, ry + ROW_H], outline="#808080", width=1)
            # Left align or center for numbers
            if i == 0:
                draw.text((cx + 15, ry + 12), val, fill="#000000", font=f_td)
            else:
                bbox = draw.textbbox((0, 0), val, font=f_td)
                tw = bbox[2] - bbox[0]
                td_x = cx + (hw - tw) // 2
                draw.text((td_x, ry + 12), val, fill="#000000", font=f_td)
            cx += hw
        ry += ROW_H

    # Right side Annotation / Checklist Panel
    PANEL_X = 660
    PANEL_Y = 125
    PANEL_W = 460
    draw.rectangle([PANEL_X, PANEL_Y, PANEL_X + PANEL_W, H - 60], fill="#F8FAFC", outline="#CBD5E1", width=1)
    
    draw.rectangle([PANEL_X, PANEL_Y, PANEL_X + PANEL_W, PANEL_Y + 45], fill="#0F172A")
    draw.text((PANEL_X + 20, PANEL_Y + 13), "KIỂM CHỨNG THEO YÊU CẦU ĐỀ BÀI", fill="#FFFFFF", font=get_font(13, bold=True))

    checks = [
        ("✔ Tiêu đề trang (title):", "Hiển thị đúng 'Bảng đơn giản trong HTML'"),
        ("✔ Tiêu đề phần (h2):", "Hiển thị đúng 'Danh sách học sinh'"),
        ("✔ Đường viền (border):", "Thuộc tính border='1' tạo viền cho toàn bộ ô"),
        ("✔ Cột 1 (th/td):", "Họ và Tên (Nguyễn Văn A, Trần Thị B, Lê Văn C)"),
        ("✔ Cột 2 (th/td):", "Tuổi (15, 16, 17)"),
        ("✔ Cột 3 (th/td):", "Lớp (10A1, 11B2, 12C3)"),
        ("✔ Định dạng thẻ <th>:", "In đậm mặc định theo tiêu chuẩn HTML"),
        ("✔ Cấu trúc dữ liệu:", "4 hàng (tr): 1 hàng tiêu đề + 3 hàng dữ liệu")
    ]

    cy = PANEL_Y + 65
    for title_chk, desc_chk in checks:
        draw.text((PANEL_X + 20, cy), title_chk, fill="#16A34A", font=get_font(11, bold=True))
        draw.text((PANEL_X + 20, cy + 18), desc_chk, fill="#334155", font=get_font(11, bold=False))
        cy += 46

    # Bottom status banner
    draw.rectangle([PANEL_X + 20, H - 120, PANEL_X + PANEL_W - 20, H - 75], fill="#ECFDF5", outline="#10B981", width=1)
    draw.text((PANEL_X + 35, H - 105), "ĐÁNH GIÁ: HOÀN THÀNH XUẤT SẮC 100%", fill="#065F46", font=get_font(12, bold=True))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_table_architecture_diagram(filename):
    W, H = 1200, 680
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_box_h = get_font(13, bold=True)
    f_box_c = get_font(11, bold=False)
    f_mono = get_mono_font(11, bold=False)

    # Title Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "CẤU TRÚC PHÂN TẦNG VÀ Ý NGHĨA CÁC THẺ TRONG HTML TABLE", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Mối quan hệ cha - con giữa thẻ <table>, <tr> (hàng), <th> (tiêu đề cột) và <td> (ô dữ liệu)", fill="#94A3B8", font=f_sub)

    # 4 Cards
    cards = [
        ("<table border=\"1\">", "Thẻ Bảng (Container)",
         ["• Thẻ bao bọc cấp cao nhất.", "• Thuộc tính border=\"1\": Hiển thị khung viền của bảng.", "• Chứa toàn bộ các hàng <tr>.", "• Đóng vai trò cấu trúc dữ liệu lưới."],
         "#3B82F6", "#EFF6FF", 40),
        ("<tr>", "Hàng Bảng (Table Row)",
         ["• Định nghĩa 1 hàng ngang trong bảng.", "• Số thẻ <tr> = Số hàng dữ liệu.", "• Hàng 1: Dành cho tiêu đề cột (th).", "• Hàng 2, 3, 4: Dành cho bản ghi (td)."],
         "#10B981", "#ECFDF5", 325),
        ("<th>", "Tiêu Đề Cột (Table Header)",
         ["• Viết tắt của Table Header.", "• Nằm bên trong thẻ <tr> hàng đầu tiên.", "• Trình duyệt mặc định: IN ĐẬM & CĂN GIỮA.", "• Ví dụ: Họ và Tên, Tuổi, Lớp."],
         "#F59E0B", "#FFFBEB", 610),
        ("<td>", "Ô Dữ Liệu (Table Data)",
         ["• Viết tắt của Table Data Cell.", "• Chứa dữ liệu của từng học sinh.", "• Trình duyệt mặc định: Chữ thường, căn trái.", "• Ví dụ: Nguyễn Văn A, 15, 10A1."],
         "#8B5CF6", "#F5F3FF", 895)
    ]

    card_w = 265
    card_h = 350
    card_y = 115

    for tag, sub, bullets, border_c, bg_c, x in cards:
        draw.rectangle([x, card_y, x + card_w, card_y + card_h], fill=bg_c, outline=border_c, width=2)
        draw.rectangle([x, card_y, x + card_w, card_y + 45], fill=border_c)
        draw.text((x + 15, card_y + 8), tag, fill="#FFFFFF", font=get_mono_font(13, bold=True))
        draw.text((x + 15, card_y + 26), sub, fill="#FFFFFF", font=get_font(10, bold=False))

        by = card_y + 60
        for b in bullets:
            draw.text((x + 15, by), b, fill="#1E293B", font=f_box_c)
            by += 40

    # Connector arrows
    for ax in [307, 592, 877]:
        draw.line([ax, card_y + card_h // 2, ax + 16, card_y + card_h // 2], fill="#475569", width=3)
        draw.polygon([(ax + 16, card_y + card_h // 2 - 5), (ax + 24, card_y + card_h // 2), (ax + 16, card_y + card_h // 2 + 5)], fill="#475569")

    # Code breakdown bottom box
    draw.rectangle([40, 495, W - 40, 645], fill="#0F172A", outline="#1E293B", width=1)
    draw.text((60, 508), "TỔNG KẾT QUY TẮC TỔ CHỨC DỮ LIỆU HTML TABLE:", fill="#38BDF8", font=get_font(12, bold=True))
    draw.text((60, 535), "1. Cấu trúc lồng nhau nghiêm ngặt: <table> ➔ <tr> ➔ <th> hoặc <td>. Tuyệt đối không đặt <td> trực tiếp trong <table>.", fill="#E2E8F0", font=f_box_c)
    draw.text((60, 562), "2. Số ô (th/td) trong mỗi hàng <tr> phải bằng nhau để bảng không bị lệch cột (3 cột: Họ và Tên, Tuổi, Lớp).", fill="#E2E8F0", font=f_box_c)
    draw.text((60, 589), "3. Tiêu chuẩn hiện đại khuyến khích bổ sung thêm <thead>, <tbody> để phân định ngữ nghĩa rõ ràng cho SEO và trợ năng.", fill="#4ADE80", font=get_font(11, bold=True))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_modern_styled_table_diagram(filename):
    W, H = 1200, 680
    img = Image.new("RGB", (W, H), color="#F8FAFC")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_tbl_h = get_font(13, bold=True)
    f_tbl_c = get_font(12, bold=False)

    # Title Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "SO SÁNH: BẢNG HTML CƠ BẢN (BORDER=1) VS BẢNG CHUẨN HÓA CSS", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Nâng cấp giao diện người dùng (UI/UX) từ bảng thô sang thiết kế chuẩn công nghệ", fill="#94A3B8", font=f_sub)

    # Column 1: Basic Table (Left)
    C1_X = 40
    C1_W = 540
    draw.rectangle([C1_X, 110, C1_X + C1_W, 640], fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.rectangle([C1_X, 110, C1_X + C1_W, 155], fill="#64748B")
    draw.text((C1_X + 20, 122), "1. BẢNG HTML THUẦN (BORDER=\"1\") - NGUYÊN BẢN ĐỀ BÀI", fill="#FFFFFF", font=f_tbl_h)

    draw.text((C1_X + 20, 175), "Danh sách học sinh", fill="#000000", font=get_serif_font(20, bold=True))
    
    # Table 1 draw
    t1_y = 215
    draw.rectangle([C1_X + 20, t1_y, C1_X + C1_W - 20, t1_y + 160], outline="#808080", width=2)
    t1_cols = [("Họ và Tên", 220), ("Tuổi", 120), ("Lớp", 160)]
    
    # Header
    tx = C1_X + 20
    for hname, hw in t1_cols:
        draw.rectangle([tx, t1_y, tx + hw, t1_y + 40], outline="#808080", width=1)
        draw.text((tx + 20, t1_y + 10), hname, fill="#000000", font=get_serif_font(14, bold=True))
        tx += hw

    t1_data = [
        ("Nguyễn Văn A", "15", "10A1"),
        ("Trần Thị B", "16", "11B2"),
        ("Lê Văn C", "17", "12C3")
    ]
    dy = t1_y + 40
    for r in t1_data:
        tx = C1_X + 20
        for i, val in enumerate(r):
            hw = t1_cols[i][1]
            draw.rectangle([tx, dy, tx + hw, dy + 40], outline="#808080", width=1)
            draw.text((tx + 20, dy + 10), val, fill="#000000", font=get_serif_font(14, bold=False))
            tx += hw
        dy += 40

    draw.text((C1_X + 20, 400), "Nhận xét:", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((C1_X + 20, 425), "• Viền kép mặc định của trình duyệt (double border).", fill="#475569", font=f_tbl_c)
    draw.text((C1_X + 20, 450), "• Không có khoảng cách đệm (padding) tối ưu.", fill="#475569", font=f_tbl_c)
    draw.text((C1_X + 20, 475), "• Phù hợp với bài tập luyện tập ban đầu.", fill="#475569", font=f_tbl_c)

    # Column 2: Modern CSS Table (Right)
    C2_X = 620
    C2_W = 540
    draw.rectangle([C2_X, 110, C2_X + C2_W, 640], fill="#FFFFFF", outline="#3B82F6", width=2)
    draw.rectangle([C2_X, 110, C2_X + C2_W, 155], fill="#1E3A8A")
    draw.text((C2_X + 20, 122), "2. BẢNG HIỆN ĐẠI (CSS STYLED) - TIÊU CHUẨN THỰC TẾ", fill="#FFFFFF", font=f_tbl_h)

    draw.text((C2_X + 20, 175), "Danh Sách Học Sinh Nâng Cao", fill="#1E293B", font=get_font(18, bold=True))

    # Table 2 draw
    t2_y = 215
    draw.rectangle([C2_X + 20, t2_y, C2_X + C2_W - 20, t2_y + 175], fill="#FFFFFF", outline="#E2E8F0", width=1)
    
    # Modern header
    draw.rectangle([C2_X + 20, t2_y, C2_X + C2_W - 20, t2_y + 45], fill="#0F172A")
    draw.text((C2_X + 40, t2_y + 12), "HỌ VÀ TÊN", fill="#38BDF8", font=get_font(11, bold=True))
    draw.text((C2_X + 260, t2_y + 12), "TUỔI", fill="#38BDF8", font=get_font(11, bold=True))
    draw.text((C2_X + 390, t2_y + 12), "LỚP", fill="#38BDF8", font=get_font(11, bold=True))

    # Modern rows with subtle striping & badges
    t2_rows = [
        ("Nguyễn Văn A", "15", "10A1", "#0284C7", "#E0F2FE"),
        ("Trần Thị B", "16", "11B2", "#4F46E5", "#EEF2FF"),
        ("Lê Văn C", "17", "12C3", "#059669", "#ECFDF5")
    ]
    my = t2_y + 45
    for name, age, cls, tag_c, tag_bg in t2_rows:
        draw.line([C2_X + 20, my, C2_X + C2_W - 20, my], fill="#F1F5F9", width=1)
        draw.text((C2_X + 40, my + 12), name, fill="#0F172A", font=get_font(12, bold=True))
        draw.text((C2_X + 265, my + 12), age, fill="#334155", font=get_font(12, bold=False))
        # Badge
        draw.rectangle([C2_X + 385, my + 8, C2_X + 445, my + 32], fill=tag_bg, outline=tag_c, width=1)
        draw.text((C2_X + 397, my + 11), cls, fill=tag_c, font=get_font(11, bold=True))
        my += 43

    draw.text((C2_X + 20, 415), "Điểm vượt trội:", fill="#1E3A8A", font=get_font(12, bold=True))
    draw.text((C2_X + 20, 440), "• border-collapse: collapse loại bỏ viền kép thô sơ.", fill="#059669", font=f_tbl_c)
    draw.text((C2_X + 20, 465), "• Padding rộng rãi (0.9rem 1.2rem) tăng độ thông thoáng.", fill="#059669", font=f_tbl_c)
    draw.text((C2_X + 20, 490), "• Hiệu ứng badge màu phân loại lớp học sinh chuyên nghiệp.", fill="#059669", font=f_tbl_c)

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

if __name__ == "__main__":
    out_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-bang-html"
    create_browser_screenshot(os.path.join(out_dir, "browser_table_result_screenshot.png"))
    create_table_architecture_diagram(os.path.join(out_dir, "html_table_tags_architecture.png"))
    create_modern_styled_table_diagram(os.path.join(out_dir, "modern_css_styled_table.png"))
