import requests, json, random, string, re, time, os, sys, platform

MAIL_FILE = "mailinfo.json"

# ───── Hiệu ứng ─────
def slow_print(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_dots(message="Đang xử lý", repeat=3, delay=0.4):
    for _ in range(repeat):
        for dots in [".", "..", "..."]:
            sys.stdout.write(f"\r{message}{dots}   ")
            sys.stdout.flush()
            time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def pause():
    input("\n[↩️] ɴʜᴀ̂́ɴ ᴇɴᴛᴇʀ ᴆᴇ̂̉ ǫᴜᴀʏ ʟᴀ̣ɪ ᴍᴇɴᴜ...")

# ───── Xử lý Email ─────
def generate_email():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

def get_domain():
    try:
        r = requests.get("https://api.mail.tm/domains", timeout=10)
        domains = r.json().get("hydra:member", [])
        return domains[0]["domain"] if domains else None
    except:
        return None

def create_account(email):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    try:
        r = requests.post("https://api.mail.tm/accounts", json={"address": email, "password": password})
        if r.status_code == 201:
            save_info(email, password)
            return True
        return False
    except:
        return False

def login(email, password):
    try:
        r = requests.post("https://api.mail.tm/token", json={"address": email, "password": password})
        return r.json().get("token") if r.status_code == 200 else None
    except:
        return None

def wait_for_otp(token, timeout=60):
    headers = {"Authorization": f"Bearer {token}"}
    print()
    slow_print(f"[⌛] ᴆᴀɴɢ ᴆᴏ̛̣ɪ ᴍᴀ̃ ᴏᴛᴘ ᴛʀᴏɴɢ ᴇᴍᴀɪʟ ( ᴛᴏ̂́ɪ ᴆᴀ {timeout} ɢɪᴀ̂ʏ )...", delay=0.03)

    for remaining in range(timeout, 0, -1):
        try:
            r = requests.get("https://api.mail.tm/messages", headers=headers)
            if r.status_code == 200:
                messages = r.json().get("hydra:member", [])
                if messages:
                    msg_id = messages[0]["id"]
                    detail = requests.get(f"https://api.mail.tm/messages/{msg_id}", headers=headers).json()
                    content = detail.get("text", "")
                    print("\n")
                    slow_print(f"📨 Từ: {detail['from']['address']}")
                    slow_print("----- Nội dung -----")
                    slow_print(content, delay=0.005)
                    slow_print("--------------------")

                    found = re.findall(r"\b\d{4,8}\b", content)
                    if found:
                        slow_print(f"[✅] ᴍᴀ̃ xᴀ́ᴄ ᴍɪɴʜ : {found[0]}")
                    else:
                        slow_print("[!] ᴋʜᴏ̂ɴɢ ᴛɪ̀ᴍ ᴛʜᴀ̂́ʏ ᴍᴀ̃ .")
                    return
        except:
            pass

        sys.stdout.write(f"\r⌛ Còn lại: {remaining:>2} giây...   ")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\r[❌] ᴋʜᴏ̂ɴɢ ɴʜᴀ̣̂ɴ ᴆᴜ̛ᴏ̛̣ᴄ ᴍᴀ̃ ᴛʀᴏɴɢ ᴛʜᴏ̛̀ɪ ɢɪᴀɴ ᴄʜᴏ ᴘʜᴇ́ᴘ.       \n")
    sys.stdout.flush()

# ───── Lưu / Xóa ─────
def save_info(email, password):
    with open(MAIL_FILE, "w") as f:
        json.dump({"email": email, "password": password}, f)

def load_info():
    if not os.path.exists(MAIL_FILE):
        return None, None
    with open(MAIL_FILE, "r") as f:
        data = json.load(f)
        return data.get("email"), data.get("password")

def delete_info():
    if os.path.exists(MAIL_FILE):
        os.remove(MAIL_FILE)

# ───── MENU 2 CHỨC NĂNG ─────
def main_menu():
    while True:
        clear_screen()
        slow_print("📌 ᴛᴏᴏʟ ᴆᴜ̛ᴏ̛̣ᴄ ᴛᴀ̣ᴏ ʙᴏ̛̉ɪ @ᴅɢᴄᴏɴɢᴛʜᴀɴʜ 🦅", delay=0.05)
        slow_print("📬 ᴛᴏᴏʟ ɢᴇᴛ ᴍᴀ̃ ɢᴍᴀɪʟ ᴀ̉ᴏ", delay=0.03)        
        print("1️⃣ ᴛᴀ̣ᴏ ᴇᴍᴀɪʟ ᴍᴏ̛́ɪ + xᴏ́ᴀ ᴇᴍᴀɪʟ ᴄᴜ̃")
        print("2️⃣ ʟᴀ̂́ʏ ᴍᴀ̃ ᴏᴛᴘ ")
        print("0️⃣ ᴇxɪᴛ")
        choice = input("\n➤ ɴʜᴀ̣̂ᴘ ʟᴜ̛̣ᴀ ᴄʜᴏ̣ɴ : ").strip()

        if choice == "1":
            clear_screen()
            delete_info()
            slow_print("[🔁] ᴅᴇʟᴇᴛᴇ ᴏʟᴅ ᴇᴍᴀɪʟꜱ ✅")
            username = generate_email()
            domain = get_domain()
            if not domain:
                slow_print("[❌] ᴄᴀɴɴᴏᴛ ɢᴇᴛ ᴅᴏᴍᴀɪɴ ")
                pause()
                continue
            email_full = f"{username}@{domain}"
            if create_account(email_full):
                slow_print(f"[📧] ɴᴇᴡ ᴇᴍᴀɪʟ ᴄʀᴇᴀᴛᴇᴅ : {email_full}")
            else:
                slow_print("[❌] ᴇʀʀᴏʀ ᴄʀᴇᴀᴛɪɴɢ ᴀᴄᴄᴏᴜɴᴛ ")
            pause()

        elif choice == "2":
            clear_screen()
            email, password = load_info()
            if not email:
                slow_print("[!] ᴋʜᴏ̂ɴɢ ᴛɪ̀ᴍ ᴛʜᴀ̂́ʏ ᴇᴍᴀɪʟ. ᴠᴜɪ ʟᴏ̀ɴɢ ᴄʜᴏ̣ɴ ᴍᴜ̣ᴄ 𝟣 ᴛʀᴜ̛ᴏ̛́ᴄ.")
                pause()
                continue
            slow_print(f"[📩] ᴜꜱᴇ ᴇᴍᴀɪʟ : {email}")
            token = login(email, password)
            if token:
                wait_for_otp(token)
            else:
                slow_print("[❌] ᴄᴀɴɴᴏᴛ ʟᴏɢ ɪɴ. ")
            pause()

        elif choice == "0":
            slow_print("ᴄʜᴜ́ᴄ ʙᴀ̣ɴ 𝟣 ɴɢᴀ̀ʏ ᴠᴜɪ ᴠᴇ̉ @ᴅɢᴄᴏɴɢᴛʜᴀɴʜ", delay=0.03)
            break

        else:
            slow_print("[!] ʟᴜ̛̣ᴀ ᴄʜᴏ̣ɴ ᴋʜᴏ̂ɴɢ ʜᴏ̛̣ᴘ ʟᴇ̣̂. ")
            pause()

if __name__ == "__main__":
    main_menu()
