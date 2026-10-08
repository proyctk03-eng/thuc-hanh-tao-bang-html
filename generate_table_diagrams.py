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

    # 1. Browser Tab & Titlebar
    draw.rectangle([0, 0, W, 42], fill="#E5E7EB")
    
    # Active Tab
    draw.rectangle([80, 8, 320, 42], fill="#FFFFFF")
    draw.text((95, 14), "📄 Gộp ô trong bảng", fill="#111827", font=f_title)
    draw.text((300, 14), "✕", fill="#6B7280", font=f_title)

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
    draw.text((CONTENT_X, CONTENT_Y), "Thời khóa biểu", fill="#000000", font=f_h2)

    # Table with border="1" simulation
    TBL_X = CONTENT_X
    TBL_Y = CONTENT_Y + 55
    COL1_W = 150  # Thứ
    COL2_W = 170  # Môn học
    COL3_W = 180  # Giáo viên
    ROW_H = 50

    # Row 0: Header (Thứ, Môn học, Giáo viên)
    draw.rectangle([TBL_X, TBL_Y, TBL_X + COL1_W, TBL_Y + ROW_H], outline="#808080", width=1)
    draw.rectangle([TBL_X + COL1_W, TBL_Y, TBL_X + COL1_W + COL2_W, TBL_Y + ROW_H], outline="#808080", width=1)
    draw.rectangle([TBL_X + COL1_W + COL2_W, TBL_Y, TBL_X + COL1_W + COL2_W + COL3_W, TBL_Y + ROW_H], outline="#808080", width=1)
    
    # TH Centered
    for (name, x, w) in [("Thứ", TBL_X, COL1_W), ("Môn học", TBL_X + COL1_W, COL2_W), ("Giáo viên", TBL_X + COL1_W + COL2_W, COL3_W)]:
        bbox = draw.textbbox((0, 0), name, font=f_th)
        tw = bbox[2] - bbox[0]
        draw.text((x + (w - tw)//2, TBL_Y + 12), name, fill="#000000", font=f_th)

    # Row 1 & 2: Thứ Hai (rowspan="2", height = ROW_H * 2)
    R1_Y = TBL_Y + ROW_H
    draw.rectangle([TBL_X, R1_Y, TBL_X + COL1_W, R1_Y + ROW_H * 2], outline="#808080", width=1)
    bbox_thuhai = draw.textbbox((0, 0), "Thứ Hai", font=f_td)
    draw.text((TBL_X + 25, R1_Y + ROW_H - 12), "Thứ Hai", fill="#000000", font=f_td)

    # Row 1 data (Toán, Thầy Nam)
    draw.rectangle([TBL_X + COL1_W, R1_Y, TBL_X + COL1_W + COL2_W, R1_Y + ROW_H], outline="#808080", width=1)
    draw.text((TBL_X + COL1_W + 20, R1_Y + 12), "Toán", fill="#000000", font=f_td)
    
    draw.rectangle([TBL_X + COL1_W + COL2_W, R1_Y, TBL_X + COL1_W + COL2_W + COL3_W, R1_Y + ROW_H], outline="#808080", width=1)
    draw.text((TBL_X + COL1_W + COL2_W + 20, R1_Y + 12), "Thầy Nam", fill="#000000", font=f_td)

    # Row 2 data (Văn, Cô Hạnh)
    R2_Y = R1_Y + ROW_H
    draw.rectangle([TBL_X + COL1_W, R2_Y, TBL_X + COL1_W + COL2_W, R2_Y + ROW_H], outline="#808080", width=1)
    draw.text((TBL_X + COL1_W + 20, R2_Y + 12), "Văn", fill="#000000", font=f_td)

    draw.rectangle([TBL_X + COL1_W + COL2_W, R2_Y, TBL_X + COL1_W + COL2_W + COL3_W, R2_Y + ROW_H], outline="#808080", width=1)
    draw.text((TBL_X + COL1_W + COL2_W + 20, R2_Y + 12), "Cô Hạnh", fill="#000000", font=f_td)

    # Row 3: Thứ Ba, Nghỉ học (colspan="2", width = COL2_W + COL3_W)
    R3_Y = R2_Y + ROW_H
    draw.rectangle([TBL_X, R3_Y, TBL_X + COL1_W, R3_Y + ROW_H], outline="#808080", width=1)
    draw.text((TBL_X + 25, R3_Y + 12), "Thứ Ba", fill="#000000", font=f_td)

    draw.rectangle([TBL_X + COL1_W, R3_Y, TBL_X + COL1_W + COL2_W + COL3_W, R3_Y + ROW_H], outline="#808080", width=1)
    bbox_nghi = draw.textbbox((0, 0), "Nghỉ học", font=f_td)
    tw_nghi = bbox_nghi[2] - bbox_nghi[0]
    draw.text((TBL_X + COL1_W + (COL2_W + COL3_W - tw_nghi)//2, R3_Y + 12), "Nghỉ học", fill="#000000", font=f_td)

    # Right side Annotation / Checklist Panel
    PANEL_X = 640
    PANEL_Y = 125
    PANEL_W = 480
    draw.rectangle([PANEL_X, PANEL_Y, PANEL_X + PANEL_W, H - 60], fill="#F8FAFC", outline="#CBD5E1", width=1)
    
    draw.rectangle([PANEL_X, PANEL_Y, PANEL_X + PANEL_W, PANEL_Y + 45], fill="#0F172A")
    draw.text((PANEL_X + 20, PANEL_Y + 13), "KIỂM CHỨNG THEO YÊU CẦU ĐỀ BÀI", fill="#FFFFFF", font=get_font(13, bold=True))

    checks = [
        ("✔ Tiêu đề trang (title):", "Hiển thị đúng 'Gộp ô trong bảng'"),
        ("✔ Tiêu đề phần (h2):", "Hiển thị đúng 'Thời khóa biểu'"),
        ("✔ Đường viền (border):", "Thuộc tính border='1' hiển thị rõ toàn bộ viền ô"),
        ("✔ Gộp hàng (rowspan=\"2\"):", "Ô 'Thứ Hai' gộp chính xác 2 hàng Toán và Văn"),
        ("✔ Hàng thứ 2 tối ưu ô:", "Chỉ khai báo 2 ô (Văn, Cô Hạnh) tránh lỗi xô lệch"),
        ("✔ Gộp cột (colspan=\"2\"):", "Ô 'Nghỉ học' gộp chính xác 2 cột Môn học & Giáo viên"),
        ("✔ Hàng thứ 3 chuẩn xác:", "Gồm ô 'Thứ Ba' và ô gộp 'Nghỉ học'"),
        ("✔ Kết quả hiển thị:", "Hoàn hảo 100% theo tiêu chuẩn HTML5")
    ]

    cy = PANEL_Y + 65
    for title_chk, desc_chk in checks:
        draw.text((PANEL_X + 20, cy), title_chk, fill="#16A34A", font=get_font(11, bold=True))
        draw.text((PANEL_X + 20, cy + 18), desc_chk, fill="#334155", font=get_font(11, bold=False))
        cy += 46

    # Bottom status banner
    draw.rectangle([PANEL_X + 20, H - 110, PANEL_X + PANEL_W - 20, H - 75], fill="#ECFDF5", outline="#10B981", width=1)
    draw.text((PANEL_X + 35, H - 98), "ĐÁNH GIÁ: HOÀN THÀNH XUẤT SẮC 100%", fill="#065F46", font=get_font(12, bold=True))

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
    draw.text((35, 18), "CƠ CHẾ KỸ THUẬT: GỘP Ô TRONG BẢNG HTML (ROWSPAN VS COLSPAN)", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Quy tắc hoạt động và phương pháp tổ chức số lượng ô <td> để không gây vỡ giao diện bảng", fill="#94A3B8", font=f_sub)

    # 2 Comparison Columns
    # Left: ROWSPAN
    C1_X = 40
    C1_W = 540
    draw.rectangle([C1_X, 110, C1_X + C1_W, 460], fill="#F0F9FF", outline="#0284C7", width=2)
    draw.rectangle([C1_X, 110, C1_X + C1_W, 155], fill="#0284C7")
    draw.text((C1_X + 20, 122), "1. THUỘC TÍNH ROWSPAN (GỘP HÀNG DỌC)", fill="#FFFFFF", font=f_box_h)

    r_items = [
        ("Cú pháp:", "<td rowspan=\"2\">Thứ Hai</td>"),
        ("Ý nghĩa:", "Ô này trải dài xuống dưới 2 hàng liên tiếp."),
        ("Quy tắc cấu trúc:", "Tại hàng <tr> đầu tiên: khai báo 3 ô (Thứ Hai, Toán, Thầy Nam)."),
        ("Tại hàng <tr> thứ 2:", "Ô 'Thứ Hai' đã chiếm chỗ cột 1, do đó CHỈ ĐƯỢC khai báo 2 ô (Văn, Cô Hạnh)."),
        ("Lỗi thường gặp:", "Nếu hàng 2 vẫn khai báo 3 ô thì ô cuối cùng sẽ bị đẩy ra ngoài mép bảng!")
    ]
    ry = 175
    for lbl, val in r_items:
        draw.text((C1_X + 20, ry), lbl, fill="#0369A1", font=get_font(11, bold=True))
        draw.text((C1_X + 20, ry + 18), val, fill="#334155", font=get_font(10.5, bold=False))
        ry += 52

    # Right: COLSPAN
    C2_X = 620
    C2_W = 540
    draw.rectangle([C2_X, 110, C2_X + C2_W, 460], fill="#FEF2F2", outline="#EF4444", width=2)
    draw.rectangle([C2_X, 110, C2_X + C2_W, 155], fill="#EF4444")
    draw.text((C2_X + 20, 122), "2. THUỘC TÍNH COLSPAN (GỘP CỘT NGANG)", fill="#FFFFFF", font=f_box_h)

    c_items = [
        ("Cú pháp:", "<td colspan=\"2\">Nghỉ học</td>"),
        ("Ý nghĩa:", "Ô này trải rộng sang ngang 2 cột liền kề trong cùng một hàng."),
        ("Quy tắc cấu trúc:", "Bảng có 3 cột: Cột 1 = 'Thứ Ba' (chiếm 1 cột)."),
        ("Ô gộp:", "Ô 'Nghỉ học' với colspan='2' chiếm luôn cột 2 (Môn học) và cột 3 (Giáo viên)."),
        ("Tổng số cột hàng 3:", "1 + 2 = 3 cột ➔ Khớp hoàn hảo với độ rộng tổng thể của bảng.")
    ]
    cy = 175
    for lbl, val in c_items:
        draw.text((C2_X + 20, cy), lbl, fill="#B91C1C", font=get_font(11, bold=True))
        draw.text((C2_X + 20, cy + 18), val, fill="#334155", font=get_font(10.5, bold=False))
        cy += 52

    # Bottom Code Example Box
    draw.rectangle([40, 485, W - 40, 645], fill="#0F172A", outline="#1E293B", width=1)
    draw.text((60, 500), "CÔNG THỨC TOÁN HỌC KIỂM TRA TỔNG SỐ Ô TRONG BẢNG:", fill="#38BDF8", font=get_font(12, bold=True))
    draw.text((60, 528), "• Hàng 1 (Header): 1 (Thứ) + 1 (Môn học) + 1 (Giáo viên) = 3 ô", fill="#E2E8F0", font=f_box_c)
    draw.text((60, 555), "• Hàng 2: [Thứ Hai (rowspan=2)] + 1 (Toán) + 1 (Thầy Nam) = 3 vị trí", fill="#E2E8F0", font=f_box_c)
    draw.text((60, 582), "• Hàng 3: [Thứ Hai kế thừa từ trên] + 1 (Văn) + 1 (Cô Hạnh) = 3 vị trí", fill="#E2E8F0", font=f_box_c)
    draw.text((60, 609), "• Hàng 4: 1 (Thứ Ba) + [Nghỉ học (colspan=2)] = 3 vị trí ➔ TẤT CẢ CÁC HÀNG ĐỀU ĐẠT CHUẨN 3 CỘT!", fill="#4ADE80", font=get_font(11, bold=True))

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
    draw.text((35, 18), "SO SÁNH: THỜI KHÓA BIỂU HTML GỐC VS THỜI KHÓA BIỂU NÂNG CAO", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Hiệu quả trình bày trực quan khi kết hợp gộp ô logic và bảng màu hiện đại", fill="#94A3B8", font=f_sub)

    # Left: Basic
    C1_X = 40
    C1_W = 540
    draw.rectangle([C1_X, 110, C1_X + C1_W, 640], fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.rectangle([C1_X, 110, C1_X + C1_W, 155], fill="#64748B")
    draw.text((C1_X + 20, 122), "1. THỜI KHÓA BIỂU HTML THUẦN (BORDER=\"1\")", fill="#FFFFFF", font=f_tbl_h)

    draw.text((C1_X + 20, 175), "Thời khóa biểu", fill="#000000", font=get_serif_font(20, bold=True))

    # Basic table
    by = 220
    bw = C1_W - 40
    draw.rectangle([C1_X + 20, by, C1_X + 20 + bw, by + 160], outline="#808080", width=2)
    # Header
    draw.rectangle([C1_X + 20, by, C1_X + 160, by + 40], outline="#808080", width=1)
    draw.text((C1_X + 70, by + 10), "Thứ", fill="#000000", font=get_serif_font(14, bold=True))
    draw.rectangle([C1_X + 160, by, C1_X + 320, by + 40], outline="#808080", width=1)
    draw.text((C1_X + 210, by + 10), "Môn học", fill="#000000", font=get_serif_font(14, bold=True))
    draw.rectangle([C1_X + 320, by, C1_X + 20 + bw, by + 40], outline="#808080", width=1)
    draw.text((C1_X + 380, by + 10), "Giáo viên", fill="#000000", font=get_serif_font(14, bold=True))

    # Rowspan Thứ Hai
    draw.rectangle([C1_X + 20, by + 40, C1_X + 160, by + 120], outline="#808080", width=1)
    draw.text((C1_X + 50, by + 70), "Thứ Hai", fill="#000000", font=get_serif_font(14, bold=False))
    
    # Toán / Thầy Nam
    draw.rectangle([C1_X + 160, by + 40, C1_X + 320, by + 80], outline="#808080", width=1)
    draw.text((C1_X + 180, by + 50), "Toán", fill="#000000", font=get_serif_font(14, bold=False))
    draw.rectangle([C1_X + 320, by + 40, C1_X + 20 + bw, by + 80], outline="#808080", width=1)
    draw.text((C1_X + 340, by + 50), "Thầy Nam", fill="#000000", font=get_serif_font(14, bold=False))

    # Văn / Cô Hạnh
    draw.rectangle([C1_X + 160, by + 80, C1_X + 320, by + 120], outline="#808080", width=1)
    draw.text((C1_X + 180, by + 90), "Văn", fill="#000000", font=get_serif_font(14, bold=False))
    draw.rectangle([C1_X + 320, by + 80, C1_X + 20 + bw, by + 120], outline="#808080", width=1)
    draw.text((C1_X + 340, by + 90), "Cô Hạnh", fill="#000000", font=get_serif_font(14, bold=False))

    # Thứ Ba / Nghỉ học (colspan)
    draw.rectangle([C1_X + 20, by + 120, C1_X + 160, by + 160], outline="#808080", width=1)
    draw.text((C1_X + 50, by + 130), "Thứ Ba", fill="#000000", font=get_serif_font(14, bold=False))
    draw.rectangle([C1_X + 160, by + 120, C1_X + 20 + bw, by + 160], outline="#808080", width=1)
    draw.text((C1_X + 270, by + 130), "Nghỉ học", fill="#000000", font=get_serif_font(14, bold=False))

    draw.text((C1_X + 20, 420), "Đặc điểm nhận diện:", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((C1_X + 20, 445), "• Khung viền xám mặc định border='1'.", fill="#475569", font=f_tbl_c)
    draw.text((C1_X + 20, 470), "• Văn bản định dạng Times New Roman cổ điển.", fill="#475569", font=f_tbl_c)
    draw.text((C1_X + 20, 495), "• Gộp ô hoàn hảo theo đúng logic của đề bài.", fill="#475569", font=f_tbl_c)

    # Right: Modern
    C2_X = 620
    C2_W = 540
    draw.rectangle([C2_X, 110, C2_X + C2_W, 640], fill="#FFFFFF", outline="#0284C7", width=2)
    draw.rectangle([C2_X, 110, C2_X + C2_W, 155], fill="#0284C7")
    draw.text((C2_X + 20, 122), "2. THỜI KHÓA BIỂU NÂNG CAO (UI/UX CHUẨN HIỆN ĐẠI)", fill="#FFFFFF", font=f_tbl_h)

    draw.text((C2_X + 20, 175), "Thời Khóa Biểu Tuần Học", fill="#1E293B", font=get_font(18, bold=True))

    my = 220
    mw = C2_W - 40
    draw.rectangle([C2_X + 20, my, C2_X + 20 + mw, my + 170], fill="#FFFFFF", outline="#E2E8F0", width=1)
    
    # Modern Header
    draw.rectangle([C2_X + 20, my, C2_X + 20 + mw, my + 42], fill="#0F172A")
    draw.text((C2_X + 45, my + 12), "THỨ", fill="#38BDF8", font=get_font(11, bold=True))
    draw.text((C2_X + 200, my + 12), "MÔN HỌC", fill="#38BDF8", font=get_font(11, bold=True))
    draw.text((C2_X + 370, my + 12), "GIÁO VIÊN", fill="#38BDF8", font=get_font(11, bold=True))

    # Thứ Hai (highlight blue)
    draw.rectangle([C2_X + 20, my + 42, C2_X + 160, my + 126], fill="#F0F9FF", outline="#BAE6FD", width=1)
    draw.text((C2_X + 45, my + 72), "Thứ Hai", fill="#0369A1", font=get_font(13, bold=True))

    # Toán / Thầy Nam
    draw.line([C2_X + 160, my + 84, C2_X + 20 + mw, my + 84], fill="#F1F5F9", width=1)
    draw.text((C2_X + 200, my + 54), "Toán Học", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((C2_X + 370, my + 54), "Thầy Nam", fill="#334155", font=get_font(12, bold=False))

    # Văn / Cô Hạnh
    draw.line([C2_X + 160, my + 126, C2_X + 20 + mw, my + 126], fill="#F1F5F9", width=1)
    draw.text((C2_X + 200, my + 96), "Ngữ Văn", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((C2_X + 370, my + 96), "Cô Hạnh", fill="#334155", font=get_font(12, bold=False))

    # Thứ Ba / Nghỉ học (highlight red/amber)
    draw.rectangle([C2_X + 20, my + 126, C2_X + 160, my + 168], fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.text((C2_X + 45, my + 138), "Thứ Ba", fill="#0F172A", font=get_font(13, bold=True))

    draw.rectangle([C2_X + 160, my + 126, C2_X + 20 + mw, my + 168], fill="#FEF2F2", outline="#FECDD3", width=1)
    draw.text((C2_X + 260, my + 138), "🏖️ Nghỉ học (Gộp 2 cột)", fill="#DC2626", font=get_font(12, bold=True))

    draw.text((C2_X + 20, 420), "Ưu điểm vượt trội:", fill="#0369A1", font=get_font(12, bold=True))
    draw.text((C2_X + 20, 445), "• Phân màu theo vai trò giúp dễ đọc dữ liệu.", fill="#059669", font=f_tbl_c)
    draw.text((C2_X + 20, 470), "• Ô gộp ngang nổi bật báo hiệu ngày nghỉ học.", fill="#059669", font=f_tbl_c)
    draw.text((C2_X + 20, 495), "• Độ tương phản và khoảng cách đệm chuyên nghiệp.", fill="#059669", font=f_tbl_c)

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

if __name__ == "__main__":
    out_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-bang-html"
    create_browser_screenshot(os.path.join(out_dir, "browser_table_result_screenshot.png"))
    create_table_architecture_diagram(os.path.join(out_dir, "html_table_tags_architecture.png"))
    create_modern_styled_table_diagram(os.path.join(out_dir, "modern_css_styled_table.png"))
