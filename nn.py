import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
from tqdm import tqdm
from colorama import Fore, Style, init
import time
import sys
import os

init(autoreset=True)

def slow_print(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_input(prompt, delay=0.04):
    slow_print(prompt, delay)
    return input()

def print_banner():
    print("=" * 60)
    slow_print("🛠️  𝘼𝙐𝙏𝙊𝙈𝘼𝙏𝙄𝘾 𝙀𝙈𝘼𝙄𝙇 𝙎𝙀𝙉𝘿𝙄𝙉𝙂 𝙏𝙊𝙊𝙇 📌", 0.02)
    print("=" * 60)
    time.sleep(0.5)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_security_instruction():
    print("🔒 ʙᴜ̛ᴏ̛́ᴄ 𝟣: ʙᴀ̣̂ᴛ xᴀ́ᴄ ᴍɪɴʜ 𝟤 ʙᴜ̛ᴏ̛́ᴄ ᴠᴀ̀ᴏ : ")
    print("https://myaccount.google.com/security\n")
    print("ʙᴀ̣̂ᴛ xᴀ́ᴄ ᴍɪɴʜ 𝟤 ʙᴜ̛ᴏ̛́ᴄ (𝟤-ꜱᴛᴇᴘ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ)")
    print("---")
    print("🔑 ʙᴜ̛ᴏ̛́ᴄ 𝟤: ᴛᴀ̣ᴏ ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ\n")
    print("ꜱᴀᴜ ᴋʜɪ ʙᴀ̣̂ᴛ 𝟤 ʙᴜ̛ᴏ̛́ᴄ, ǫᴜᴀʏ ʟᴀ̣ɪ ᴛʀᴀɴɢ ʙᴀ̉ᴏ ᴍᴀ̣̂ᴛ ᴛʀᴇ̂ɴ")
    print("ᴄʜᴏ̣ɴ “ᴍᴀ̣̂ᴛ ᴋʜᴀ̂̉ᴜ ᴜ̛́ɴɢ ᴅᴜ̣ɴɢ”")
    print("ᴆᴀ̆ɴɢ ɴʜᴀ̣̂ᴘ ʟᴀ̣ɪ ɴᴇ̂́ᴜ ᴄᴀ̂̀ɴ")
    print("ᴄʜᴏ̣ɴ ᴜ̛́ɴɢ ᴅᴜ̣ɴɢ (ᴠɪ́ ᴅᴜ̣: ᴍᴀɪʟ) ᴠᴀ̀ ᴛʜɪᴇ̂́ᴛ ʙɪ̣ → ɴʜᴀ̂́ɴ ᴛᴀ̣ᴏ")
    print("ᴄᴏᴘʏ ᴍᴀ̣̂ᴛ ᴋʜᴀ̂̉ᴜ 𝟣𝟨 ᴋʏ́ ᴛᴜ̛̣ ʜɪᴇ̣̂ɴ ʀᴀ\n")
    print("#ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ ᴠɪ́ ᴅᴜ̣ ʟᴀ̀ : ᴊᴇᴛꜱʙᴇɪꜱᴠᴅᴜᴡᴏʙꜱ")
    print("🔴 ᴘʜᴀ̉ɪ ɢʜɪ ʟɪᴇ̂̀ɴ ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ ɴʜᴜ̛ ᴛʀᴇ̂ɴ ᴠᴅ ᴋʜᴏ̂ɴɢ ᴄᴀ́ᴄʜ ʀᴀ !!\n")

def check_user_input():
    while True:
        check = input("📖 ɴʜᴀ̣̂ᴘ 'ʜᴅ' ᴆᴇ̂̉ xᴇᴍ ʜᴜ̛ᴏ̛́ɴɢ ᴅᴀ̂̃ɴ ʟᴀ̂́ʏ ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ , ʜᴏᴀ̣̆ᴄ ɴʜᴀ̂́ɴ ᴇɴᴛᴇʀ ᴆᴇ̂̉ ᴠᴀ̀ᴏ ᴛᴏᴏʟ : ").strip().lower()
        if check == "hd":
            clear_screen()
            slow_print("\n📘 ᴆᴀɴɢ ʜɪᴇ̂̉ɴ ᴛʜɪ̣ ʜᴜ̛ᴏ̛́ɴɢ ᴅᴀ̂̃ɴ ...", 0.03)
            time.sleep(0.5)
            print_security_instruction()
            slow_print("\n🌪️ ᴆᴏ̣ᴄ ʜᴜ̛ᴏ̛́ɴɢ ᴅᴀ̂̃ɴ ʟᴀ̂́ʏ ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ ᴠᴀ̀ ᴄʜᴀ̣ʏ ʟᴀ̣ɪ ᴛᴏᴏʟ !!", 0.04)
            sys.exit(0)
        elif check == "":
            break
        else:
            print(Fore.RED + "❌ ʟᴜ̛̣ᴀ ᴄʜᴏ̣ɴ ᴋʜᴏ̂ɴɢ ʜᴏ̛̣ᴘ ʟᴇ̣̂. ᴠᴜɪ ʟᴏ̀ɴɢ ɴʜᴀ̣̂ᴘ 'hd' ʜᴏᴀ̣̆ᴄ ɴʜᴀ̂́ɴ Enter.\n")

# Start
check_user_input()
print_banner()

slow_print("ᴛᴏᴏʟ ᴆᴜ̛ᴏ̛̣ᴄ ᴛᴀ̣ᴏ ʙᴏ̛̉ɪ @ᴅɢᴄᴏɴɢᴛʜᴀɴʜ 🦅", 0.03)

sender_email = slow_input("📧 ɴʜᴀ̣̂ᴘ ɢᴍᴀɪʟ ᴄᴜ̉ᴀ ʙᴀ̣ɴ : ").strip()
sender_pass = getpass("🔑 ɴʜᴀ̣̂ᴘ ᴀᴘᴘ ᴘᴀꜱꜱᴡᴏʀᴅ ɢᴍᴀɪʟ ( ꜱᴇ̃ ᴀ̂̉ɴ ᴋʜɪ ɢᴏ̃ ) : ")

subject = slow_input("📌 ɴʜᴀ̣̂ᴘ ᴛɪᴇ̂ᴜ ᴆᴇ̂̀ ᴇᴍᴀɪʟ : ").strip()
body_template = slow_input("📝 ɴʜᴀ̣̂ᴘ ɴᴏ̣̂ɪ ᴅᴜɴɢ ᴇᴍᴀɪʟ : ").strip()
raw_emails = slow_input("📋 ɴʜᴀ̣̂ᴘ ᴇᴍᴀɪʟ ɴɢᴜ̛ᴏ̛̀ɪ ɴʜᴀ̣̂ɴ (ᴄᴏ́ ɢᴜ̛̉ɪ ɴʜɪᴇ̂̀ᴜ ᴄᴀ́ᴄʜ ɴʜᴀᴜ ʙᴀ̆̀ɴɢ ᴅᴀ̂́ᴜ ᴘʜᴀ̂̉ʏ) : ").strip()
recipients = []

for raw in raw_emails.split(','):
    email = raw.strip()
    if not email:
        continue
    name = slow_input(f"👤 ɴʜᴀ̣̂ᴘ ᴛᴇ̂ɴ ɴɢᴜ̛ᴏ̛̀ɪ ɴʜᴀ̣̂ɴ ᴄʜᴏ {email} ( ɴʜᴀ̂́ɴ ᴇɴᴛᴇʀ ɴᴇ̂́ᴜ ᴋʜᴏ̂ɴɢ ᴄᴀ̂̀ɴ ) : ").strip()
    recipients.append({'email': email, 'name': name or email.split('@')[0]})

repeat_count = slow_input("🔁 ɴʜᴀ̣̂ᴘ ꜱᴏ̂́ ʟᴀ̂̀ɴ ɢᴜ̛̉ɪ ( ᴍᴀ̣̆ᴄ ᴆɪ̣ɴʜ = 1 ) : ").strip()
repeat_count = int(repeat_count) if repeat_count.isdigit() and int(repeat_count) > 0 else 1

total_sends = repeat_count * len(recipients)
slow_print(f"\n🚀 ꜱᴏ̂́ ʟᴀ̂̀ɴ ɢᴜ̛̉ɪ : {repeat_count} — ᴛᴏ̂̉ɴɢ : {total_sends} ʟᴜ̛ᴏ̛̣ᴛ ɢᴜ̛̉ɪ\n", 0.02)
slow_print("⏳ ᴆᴀɴɢ ᴛʜɪᴇ̂́ᴛ ʟᴀ̣̂ᴘ ᴋᴇ̂́ᴛ ɴᴏ̂́ɪ ᴛᴏ̛́ɪ ɢᴍᴀɪʟ ...", 0.02)
time.sleep(1)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_pass)

    progress = tqdm(total=total_sends, desc="📤 ꜱᴇɴᴅɪɴɢ :", unit="email", ncols=70)

    for round_idx in range(repeat_count):
        for recipient in recipients:
            to_email = recipient["email"]
            name = recipient["name"]

            try:
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = to_email
                msg["Subject"] = subject
                body = body_template.replace("{{name}}", name).replace("{{email}}", to_email)
                msg.attach(MIMEText(body, "plain"))
                server.send_message(msg)
                time.sleep(1)
            except Exception as e:
                print(Fore.RED + f"\n❌ ᴇʀʀᴏʀ ꜱᴇɴᴅ ᴇᴍᴀɪʟ : {to_email}: {e}")
                time.sleep(1)

            progress.update(1)

    progress.close()

print()
slow_print("[✓] ᴇᴍᴀɪʟ ꜱᴇɴᴅɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ !!", 0.02)
slow_print("🛡️ ᴛᴏᴏʟ ʙʏ : @ᴅɢᴄᴏɴɢᴛʜᴀɴʜ ⚙️", 0.08)
