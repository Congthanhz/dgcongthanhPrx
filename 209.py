
import os
import sys
import time
import requests

# Colors
RESET = "\033[0m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
GRAY = "\033[1;30m"
BOLD = "\033[1m"


def typewriter_effect(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def download_animation(message="Đang tải tool từ server", duration=2.5):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{BLUE}[~] {message} {chars[i % len(chars)]}   {RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1
    print()

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message="Đang kiểm tra mạng"):
    for i in range(3):
        sys.stdout.write(f"\r{YELLOW}{message}{'.' * (i+1)}   {RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def check_internet():
    test_url = "https://github.com"
    while True:
        loading_animation("Đang kiểm tra mạng")
        try:
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                print(f"{GREEN}[✓] Kết nối mạng thành công!{RESET}")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print(f"{RED}[!] Lỗi kết nối (status code {response.status_code}){RESET}")
        except requests.exceptions.RequestException:
            print(f"{RED}[!] Không thể kết nối mạng!{RESET}")

        retry = input(f"{YELLOW}[?] Bạn có muốn thử lại? (y/n): {RESET}").lower()
        if retry != "y":
            print(f"{RED}[!] Tool đã thoát do không có mạng.{RESET}")
            exit()

check_internet()

# Banner
banner = f"""\n{CYAN}{BOLD}                         👤 𝑨𝒅𝒎𝒊𝒏 𝑷𝒂𝒏𝒆𝒍 👤
{MAGENTA}{BOLD}╔══════════════════════════════════╦════════════════════════════╗
║           𝙎𝙪𝙥𝙥𝙤𝙧𝙩                ║             𝘿𝙚𝙩𝙖𝙞𝙡         ║
╠══════════════════════════════════╬════════════════════════════╣
║ 𝚉𝚊𝚕𝚘 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 / 𝙱𝚞𝚢 𝙺𝚎𝚢           ║ 𝟶𝟹𝟾𝟻 𝟾𝟾𝟷 𝟶𝟽𝟺               ║
║ 𝙿𝚘𝚠𝚎𝚛                            ║ 𝙰𝚍𝚖𝚒𝚗 / 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛          ║
║ 𝚂𝚔𝚒𝚕𝚕𝚜                           ║ 𝙿𝚢𝚝𝚑𝚘𝚗, 𝙽𝚎𝚝𝚠𝚘𝚛𝚔𝚒𝚗𝚐, 𝚃𝚘𝚘𝚕𝚜  ║
║ 𝚃𝚘𝚘𝚕 𝚂𝚝𝚊𝚝𝚞𝚜                      ║ 𝙾𝚗𝚕𝚒𝚗𝚎                     ║
║ ᴀᴅᴍɪɴ ᴛᴏᴏʟ                       ║ ᴅᴜᴏɴɢ ᴄᴏɴɢ ᴛʜᴀɴʜ           ║
║ 𝚅𝚎𝚛𝚜𝚒𝚘𝚗                          ║ 𝚟𝟷.𝟶.𝟸-𝚜𝚝𝚊𝚋𝚕𝚎              ║
╚══════════════════════════════════╩════════════════════════════╝\n{RESET}"""
typewriter_effect(banner, delay=0.0015)
time.sleep(0.8)

print('\033[1;37m╒════════════╤══════════════════════════════╕\n'
      '│ Lựa chọn   │ Tên Tool                     │\n'
      '╞════════════╪══════════════════════════════╡\n'
      '│ 1          │ ᴛᴏᴏʟ ᴛʀᴇᴏ ɴɢᴏ̂ɴ               │\n'
      '│ 2          │ ᴛᴏᴏʟ ᴛʀᴇᴏ ɴʜᴀ̂ʏ               │\n'
      '│ 3          │ ᴛᴏᴏʟ ɴʜᴀ̂ʏ + ʀᴇ́ᴏ              │\n'
      '│ 4          │ ᴛᴏᴏʟ ᴛᴅꜱ ꜰᴜʟʟ ᴊᴏʙ            │\n'
      '│ 5          │ ᴛᴏᴏʟ ᴛᴅꜱ ᴘʀᴏ𝟧                │\n'
      '│ 6          │ ᴛᴏᴏʟ ᴛᴛᴄ ᴘʀᴏ𝟧                │\n'
      '│ 7          │ ᴛᴏᴏʟ ᴛᴛᴄ ɪɴꜱᴛᴀɢʀᴀᴍ           │\n'
      '│ 8          │ ᴛᴏᴏʟ ʀᴇɢ ᴀᴄᴄ ꜰᴀᴄᴇʙᴏᴏᴋ        │\n'
      '│ 9          │ ᴛᴏᴏʟ ɴᴜᴏ̂ɪ ꜰʙ                 │\n'
      '│ 10         │ ᴛᴏᴏʟ ꜱᴘᴀᴍ ʟᴏᴄᴋᴇᴛ ᴍᴀx ꜱᴘᴇᴇᴅ   │\n'
      '│ 0          │ ᴛʜᴏᴀ́ᴛ                        │\n'      
      '╘════════════╧══════════════════════════════╛\033[0m\n')







links = {
    "1": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/a.py",
    "2": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/b.py",
    "3": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/c.py",
    "4": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/6.py",
    "5": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/7.py",
    "6": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/9.py",
    "7": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/10.py",
    "8": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/11.py",
    "9": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/12.py"
  "10": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/loc.py"    
}

while True:
    print()
    choice = input(f"{WHITE}╭────────────────────────────\n"
                   f"│ {RED}[/] 𝙀𝙣𝙩𝙚𝙧 𝙎𝙚𝙡𝙚𝙘𝙩 𝙏𝙤𝙤𝙡 : ➤ {WHITE}").strip()               
                  
    if choice == "0":
        print(f"{RED}[!] Cảm ơn bạn đã sử dụng tool của dgcongthanh đẹp trai vcl!{RESET}")
        time.sleep(1.5)
        break

    elif choice in links:
        url = links[choice].strip()
        if not url.startswith("http"):
            print(f"{RED}[!] URL không hợp lệ: {url}{RESET}")
            time.sleep(1)
            continue
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            download_animation()  # <-- sửa đúng chỗ này (thụt lề vào trong try)
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"{RED}[!] Không thể tải tool! HTTP {response.status_code}{RESET}")
                time.sleep(1.2)
                continue
            code = response.text.strip()
            if not code:
                print(f"{RED}[!] File tải về trống! Kiểm tra lại link: {url}{RESET}")
                time.sleep(1.2)
                continue
            exec(code)
            break
        except requests.exceptions.ConnectionError:
            print(f"{RED}[!] Mất kết nối mạng khi đang tải tool!{RESET}")
        except requests.exceptions.Timeout:
            print(f"{RED}[!] Máy chủ không phản hồi, vui lòng thử lại sau.{RESET}")
        except Exception as e:
            print(f"{RED}[!] Lỗi khi thực thi tool: {e}{RESET}")
        time.sleep(1.2)

    else:
        print(f"{RED}[!] Lựa chọn không hợp lệ. Vui lòng thử lại!{RESET}")
        time.sleep(1)
