import requests
import time
import json
import sys

# Cấu hình gốc (giống PHP)
ZPROJECT_KEY = 'dcbfree'  # ✅ Key dùng nội bộ, không cần nhập từ người dùng
ZPROJECT_LIMIT = 5
ZPROJECT_MAX = sys.maxsize
ZPROJECT_API = 'https://ngl.link/api/submit'
ZPROJECT_DELAY = 0
ZPROJECT_TIMEOUT = 10
ZPROJECT_ADMIN = {
    'admin': 'dgcongthanh',
    'telegram': '@Duongcongthanhz'
}

def zprojectyeuem(trangthai, thongbao, dulieu=None):
    ketqua = {
        'trangthai': trangthai,
        'thongbao': thongbao,
        'dulieu': dulieu if dulieu else {},
        'admin': ZPROJECT_ADMIN
    }
    print(json.dumps(ketqua, indent=4, ensure_ascii=False))
    exit()

def zprojectmaiyeu(nguoidung, tinnhan):
    headers = {
        'Host': 'ngl.link',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Origin': 'https://ngl.link',
        'Referer': f'https://ngl.link/{nguoidung}'
    }
    data = {
        'username': nguoidung,
        'question': tinnhan,
        'deviceId': '0',
        'gameSlug': '',
        'referrer': ''
    }

    try:
        response = requests.post(ZPROJECT_API, headers=headers, data=data, timeout=ZPROJECT_TIMEOUT)
        return response.status_code == 200
    except:
        return False

def main():
    print("𝙏𝙤𝙤𝙡 𝙎𝙥𝙖𝙢 𝙣𝙜𝙡.𝙡𝙞𝙣𝙠\n")

    nguoidung = input("👉 Nhập username NGL: @").strip()
    tinnhan = input("💬 Nhập nội dung tin nhắn: ").strip()
    try:
        soluong = int(input("🔁 Nhập số lần gửi: ").strip())
    except:
        zprojectyeuem("loi", "Số lần gửi không hợp lệ.")

    if not nguoidung or not tinnhan:
        zprojectyeuem("loi", "Username hoặc tin nhắn không được để trống.")

    if soluong <= 0:
        zprojectyeuem("loi", "Số lượng tin nhắn phải lớn hơn 0.")

    thanhcong = 0
    thatbai = 0

    for i in range(soluong):
        if zprojectmaiyeu(nguoidung, tinnhan):
            thanhcong += 1
            thatbai = 0
        else:
            thatbai += 1
            if thatbai >= ZPROJECT_LIMIT:
                time.sleep(60)
                thatbai = 0
        time.sleep(ZPROJECT_DELAY)

    zprojectyeuem("thanhcong", "Attack Thành Công Ngl.", {
        "tong_gui": thanhcong,
        "tong_yeucau": soluong,
        "thatbai": soluong - thanhcong
    })

if __name__ == "__main__":
    main()