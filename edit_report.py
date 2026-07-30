from PIL import Image, ImageDraw, ImageFont

src = "/Users/lvlv/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1fd07259429617306276fc230973204a/Message/MessageTemp/e11f2cdbfa69ac5641adce9261ec4158/Image/72681785391410_.pic.jpg"
dst = "/Users/lvlv/Library/CloudStorage/OneDrive-个人/HOTA-S1/Claw/hota_s1_repo/assets/report_edited.png"

img = Image.open(src)
draw = ImageDraw.Draw(img)

font_big = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 82, index=0)
font_num = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 28, index=0)
font_cost = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 28, index=0)

def cover(x1, y1, x2, y2):
    draw.rectangle([x1, y1, x2, y2], fill=(255, 255, 255))

def right_top(text, x_right, y_top, font, fill):
    w = draw.textlength(text, font=font)
    draw.text((x_right - w, y_top), text, font=font, fill=fill, anchor="lt")

def center_top(text, x_center, y_top, font, fill):
    w = draw.textlength(text, font=font)
    draw.text((x_center - w / 2, y_top), text, font=font, fill=fill, anchor="lt")

# 1. 大字 6（訊息對話開始次數上方）
cover(200, 515, 925, 585)
center_top("6", 562, 525, font_big, "#8E8E93")

# 2. 每次訊息對話開始成本 -> 76.76
cover(900, 695, 1085, 735)
right_top("76.76", 1080, 700, font_num, "#000000")

# 3. 連結點擊次數 3 -> 8
cover(1040, 795, 1085, 830)
right_top("8", 1080, 800, font_num, "#000000")

# 4. 新聯繫對象人數 -> 5
cover(1000, 895, 1085, 930)
right_top("5", 1080, 900, font_num, "#000000")

# 5. 每位新聯絡人的成本 -> 92.11
cover(950, 945, 1085, 980)
right_top("92.11", 1080, 950, font_num, "#000000")

# 6. 回流聯繫對象人數 -> 1
cover(1000, 1045, 1085, 1080)
right_top("1", 1080, 1050, font_num, "#000000")

# 7. 每位回流聯繫對象的成本 -> 460.54
cover(900, 1095, 1085, 1130)
right_top("460.54", 1080, 1100, font_num, "#000000")

# 8. 花費 -> CN¥460.54(共 CN¥500.00)
cover(500, 1710, 1085, 1780)
right_top("CN¥460.54(共 CN¥500.00)", 1080, 1745, font_cost, "#000000")

img.save(dst)
print("saved", dst)
