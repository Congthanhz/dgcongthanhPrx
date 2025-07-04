import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
\033[97m════════════════════════════════════════════════  
\033[1;97m[<>] ᴀᴅᴍɪɴ : ᴅᴜᴏɴɢ ᴄᴏɴɢ ᴛʜᴀɴʜ
\033[1;97m[<>] ᴍᴀɪɴ ꜰᴜɴᴄᴛɪᴏɴ : ɢᴇᴛ ᴋᴇʏ ᴛᴏᴏʟ
\033[97m════════════════════════════════════════════════  
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except requests.RequestException as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
        print("\033[97m════════════════════════════════════════════════")
        
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))
    try:
        with open('ip_key.json', 'w') as file:
            file.write(encrypted_data)
    except requests.RequestException as e:
        print(f"Lỗi khi lưu file: {e}")

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except (FileNotFoundError, json.JSONDecodeError, base64.binascii.Error):
        print("Lỗi khi đọc file ip_key.json. File có thể đã bị hỏng.")
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'DCT{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://dgcongthanh.x10.mx/?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    gio_gioi_han = 23
    return now.hour >= gio_gioi_han

def get_shortened_link_phu(url):
    """
    Hàm để rút gọn URL bằng một dịch vụ API.
    """
    try:
        token = "684bd7552c6eae50cf7e34bd"  # Thay bằng API Token Của Bạn
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Error"}
    except requests.RequestException:
        return {"status": "error", "message": "Error"}


# === TÍCH HỢP VIP KEY QUA JSON ===
def load_vip_keys():
    if not os.path.exists("vip_keys.json"):
        return {}
    with open("vip_keys.json", "r") as f:
        return json.load(f)

def log_vip_key_use(ip, key, expiration_date):
    with open("vip_key_logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] IP: {ip} Dùng KEY VIP: {key} , Hết Hạn: {expiration_date}\n")

def check_vip_key(key_input, user_ip):
    vip_keys = load_vip_keys()
    if key_input in vip_keys:
        expire_str = vip_keys[key_input]["expire"]
        expiration_date = datetime.fromisoformat(expire_str)

        # Nếu key đã có IP đã sử dụng
        bound_ip = vip_keys[key_input].get("ip")
        if bound_ip and bound_ip != user_ip:
            print("[1;31mᴋᴇʏ ᴠɪᴘ ᴆᴀ̃ ᴄᴏ́ ɴɢᴜ̛ᴏ̛̀ɪ ꜱᴜ̛̉ ᴅᴜ̣ɴɢ.")
            return False

        if expiration_date > datetime.now():
            print(f"[1;32m👨‍💻 𝑪𝒐𝒓𝒓𝒆𝒄𝒕 𝑲𝒆𝒚 𝑽𝒊𝒑 - 𝑯𝒆̂́𝒕 𝒉𝒂̣𝒏: {expiration_date}")
            time.sleep(3)
            vip_keys[key_input]["ip"] = user_ip  # Gắn IP lần đầu sử dụng
            with open("vip_keys.json", "w") as f:
                json.dump(vip_keys, f, indent=2)
            log_vip_key_use(user_ip, key_input, expiration_date)
            luu_thong_tin_ip(user_ip, key_input, expiration_date)
            sleep(2)
            return True
        else:
            print("[1;31mᴋᴇʏ ᴠɪᴘ ᴆᴀ̃ ʜᴇ̂́ᴛ ʜᴀ̣ɴ.")
    else:
        print("[1;31mᴋᴇʏ ᴠɪᴘ ᴋʜᴏ̂ɴɢ ʜᴏ̛̣ᴘ ʟᴇ̣̂.")
    return False



# === KHỞI TẠO FILE MẶC ĐỊNH NẾU CHƯA TỒN TẠI ===
def tao_file_mac_dinh():
    if not os.path.exists("vip_keys.json"):
        sample = {
            "VIP2025z": {"expire": (datetime.now() + timedelta(days=30)).isoformat()},
            "VIP2025-Hellez": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-Pleo": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-dz": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-abcvz": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-DevPls": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-mzthanh": {"expire": (datetime.now() + timedelta(days=7)).isoformat()},
            "VIP2025-FreeToolVip": {"expire": (datetime.now() + timedelta(days=7)).isoformat()}
        }
        with open("vip_keys.json", "w") as f:
            json.dump(sample, f, indent=2)

    if not os.path.exists("ip_key.json"):
        with open("ip_key.json", "w") as f:
            f.write(encrypt_data("{}"))

# Gọi khởi tạo ngay đầu main
tao_file_mac_dinh()


def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mᴄʜᴀ̀ᴏ ᴍᴜ̛̀ɴɢ ʙᴀ̣ɴ ᴛʀᴏ̛̉ ʟᴀ̣ɪ '!!")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mʜᴇ̂́ᴛ ᴛʜᴏ̛̀ɪ ɢɪᴀɴ ꜱᴜ̛̉ ᴅᴜ̣ɴɢ !!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mɴʜᴀ̣̂ᴘ 𝟣 ᴆᴇ̂̉ ʟᴀ̂́ʏ ᴋᴇʏ \033[1;33m( ꜰʀᴇᴇ )")
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;36mɴʜᴀ̣̂ᴘ 𝟤 ᴆᴇ̂̉ ᴠᴀ̀ᴏ ᴋᴇʏ ᴠɪᴘ \033[1;31m( ᴠɪᴘ )")
                print("\033[97m════════════════════════════════════════════════")
                        
                while True:
                    try:
                        choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇꜱ : ")
                        print("\033[97m════════════════════════════════════════════════")
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mʟɪɴᴋ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴋᴇʏ \033[1;36m: ', link_key_yeumoney)
                                print("\033[97m════════════════════════════════════════════════")

                            while True:
                                keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33m𝙋𝙡𝙚𝙖𝙨𝙚 𝙀𝙣𝙩𝙚𝙧 𝙆𝙚𝙮 : \033[1;32m')
                                if keynhap == key:
                                    print('𝑪𝒐𝒓𝒓𝒆𝒄𝒕 𝑲𝒆𝒚 𝑷𝒍𝒆𝒂𝒔𝒆 𝑼𝒔𝒆')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35m𝑾𝒓𝒐𝒏𝒈 𝑲𝒆𝒚 𝑷𝒍𝒆𝒂𝒔𝒆 𝑪𝒉𝒆𝒄𝒌 𝑨𝒈𝒂𝒊𝒏 \033[1;36m:', link_key_yeumoney)
                        
                        elif choice == "2":
                            while True:
                                key_vip = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mɴʜᴀ̣̂ᴘ ᴋᴇʏ ᴠɪᴘ : \033[1;31m')
                                if check_vip_key(key_vip, ip_address):
                                    return
                                else:
                                    print('\033[1;91mᴋᴇʏ ᴠɪᴘ ꜱᴀɪ ʜᴏᴀ̣̆ᴄ ʜᴇ̂́ᴛ ʜᴀ̣ɴ.')
                            print("\033[97m════════════════════════════════════════════════")

                        else:
                            print("\033[1;91mɪɴᴠᴀʟɪᴅ ꜱᴇʟᴇᴄᴛɪᴏɴ !!")

                    except ValueError:
                        print("ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31m ᴛʜᴀɴᴋꜱ ᴅᴇᴠ ᴅɢᴄᴏɴɢᴛʜᴀɴʜ")
                        sys.exit()

if __name__ == '__main__':
    main()
    
    

da_bao_loi = False

while True:
    try:
        res = requests.get('https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/209.py')
        exec(res.text)
    except requests.RequestException:
        if not da_bao_loi:
            time.sleep(2)
            message1 = "Không Có Kết Nối ..."
            for char in message1:
                sys.stdout.write(Fore.RED + Style.BRIGHT + char)
                sys.stdout.flush()
                time.sleep(0.1)
            print()
            
            time.sleep(1)  # chờ thêm 2s
            message2 = "ᴆɪ̣ᴛ ᴍᴇ̣ ᴆᴏ̀ɪ ʙᴜɢ ᴛᴏᴏʟ ᴛʜᴀ̀ɴʜᴅᴇᴘᴢᴀɪ ᴀ̀ ᴄᴜ ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴄᴜ̛̉ᴀ ɴʜᴇ́ !!"
            for char in message2:
                sys.stdout.write(Fore.YELLOW + Style.BRIGHT + char)
                sys.stdout.flush()
                time.sleep(0.1)
            print()
            exit()
