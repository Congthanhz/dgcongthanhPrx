import os
import sys
import time
import socket
import requests

# Màu
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

def download_animation(message="ᴆᴀɴɢ ᴛᴀ̉ɪ ᴛᴏᴏʟ ᴛᴜ̛̀ ꜱᴇʀᴠᴇʀ ", duration=2.5):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{BLUE}[~] {message} {chars[i % len(chars)]}   {RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1
    print()

def loading_animation(message="ᴆᴀɴɢ ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ᴍᴀ̣ɴɢ ..."):
    for i in range(3):
        sys.stdout.write(f"\r{YELLOW}{message}{'.' * (i+1)}   {RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def check_internet(max_retry=3, delay_between=2):
    test_host = "github.com"
    attempts = 0
    while attempts < max_retry:
        loading_animation("ᴆᴀɴɢ ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ᴍᴀ̣ɴɢ ...")
        try:
            socket.create_connection((test_host, 80), timeout=3)
            print(f"{GREEN}[✓] ᴆᴀ̃ ᴄᴏ́ ᴋᴇ̂́ᴛ ɴᴏ̂́ɪ ᴍᴀ̣ɴɢ ...{RESET}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        except OSError:
            attempts += 1
            print(f"{RED}[!] ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴋᴇ̂́ᴛ ɴᴏ̂́ɪ ᴍᴀ̣ɴɢ ... ᴛʜᴜ̛̉ ʟᴀ̣ɪ ({attempts}/{max_retry}){RESET}")
            time.sleep(delay_between)
    print(f"{RED}[!] ᴆᴀ̃ ᴛʜᴜ̛̉ {max_retry} ʟᴀ̂̀ɴ ᴍᴀ̀ ᴠᴀ̂̃ɴ ᴋʜᴏ̂ɴɢ ᴄᴏ́ ᴍᴀ̣ɴɢ. ᴛᴏᴏʟ ꜱᴇ̃ ᴛʜᴏᴀ́ᴛ.{RESET}")
    sys.exit(1)

# Khởi động
os.system('cls' if os.name == 'nt' else 'clear')
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

# Menu
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
      '│ 11         │ ᴛᴏᴏʟ ꜱᴘᴀᴍ ɴɢʟ.ʟɪɴᴋ           │\n'
      '│ 12         │ ᴛᴏᴏʟ ɢᴇᴛ ᴠᴀ̀ ʟᴏ̣ᴄ ᴘʀᴏxʏ ʟɪᴠᴇ   │\n'
      '│ 13         │ ᴛᴏᴏʟ ɢᴇᴛ ᴍᴀ̃ ᴍᴀɪʟ ᴀ̉ᴏ          │\n'
      '│ 14         │ ᴛᴏᴏʟ ꜱᴘᴀᴍ ɢᴍᴀɪʟ [ ᴠɪᴘ ]      │\n'
      '│ 0          │ ᴛʜᴏᴀ́ᴛ                        │\n'
      '╘════════════╧══════════════════════════════╛\033[0m\n')

# Link các tool
links = {
    "1": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/a.py",
    "2": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/b.py",
    "3": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/c.py",
    "4": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/6.py",
    "5": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/7.py",
    "6": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/9.py",
    "7": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/10.py",
    "8": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/11.py",
    "9": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/main/12.py",
    "10": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/loc.py",
    "11": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/nl.py",
    "12": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/get.py",
    "13": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/mail.py",
    "14": "https://raw.githubusercontent.com/Congthanhz/dgcongthanhPrx/refs/heads/main/nn.py",
}

# Vòng lặp
while True:
    print()
    choice = input(f"{WHITE}╭────────────────────────────\n│ {RED}[/] 𝙀𝙣𝙩𝙚𝙧 𝙎𝙚𝙡𝙚𝙘𝙩 𝙏𝙤𝙤𝙡 : ➤ {WHITE}").strip()

    if choice == "0":
        print(f"{RED}[!] Cảm ơn bạn đã sử dụng tool của dgcongthanh đẹp trai vcl!{RESET}")
        time.sleep(1.5)
        break

    elif choice in links:
        url = links[choice].strip()
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            check_internet()
            download_animation()
            response = requests.get(url, timeout=10)
            code = response.text.strip()
            exec(code)
            break
        except Exception:
            print(f"{RED}[!] ᴋʜᴏ̂ɴɢ ᴛʜᴇ̂̉ ᴛᴀ̉ɪ ᴛᴏᴏʟ [/] ᴠᴜɪ ʟᴏ̀ɴɢ ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ʟᴀ̣ɪ ᴍᴀ̣ɴɢ...{RESET}")
            time.sleep(1.2)
    else:
        print(f"{RED}[!] ʟᴜ̛̣ᴀ ᴄʜᴏ̣ɴ ᴋʜᴏ̂ɴɢ ʜᴏ̛̣ᴘ ʟᴇ̣̂. ᴠᴜɪ ʟᴏ̀ɴɢ ᴛʜᴜ̛̉ ʟᴀ̣ɪ !{RESET}")
        time.sleep(1)