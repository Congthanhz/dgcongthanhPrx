import requests
import time
import sys

def slow_type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    banner = [
        "=============================",
        "🔍 ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ᴛʜᴏ̂ɴɢ ᴛɪɴ ᴛɪᴋᴛᴏᴋ 🛡️",
        "============================="
    ]
    for line in banner:
        slow_type(line, delay=0.05)
        time.sleep(0.2)

def loading_bar():
    total = 30
    for i in range(total + 1):
        bar = '█' * i + '-' * (total - i)
        percent = int(i / total * 100)
        sys.stdout.write(f'\r⏳ ʟᴏᴀᴅɪɴɢ ... |{bar}| {percent}%')
        sys.stdout.flush()
        time.sleep(0.07)
    print("\n✅ ʜᴏᴀ̀ɴ ᴛᴀ̂́ᴛ ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ...\n")

def fetch_tiktok_info(username):
    url = "http://liggdzut.x10.mx/api/infott.php"
    api_key = "liggdzut123"
    params = {
        "username": username,
        "key": api_key
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()

        if "uniqueId" not in data:
            return None

        return {
            "👤 Username": data.get("uniqueId", ""),
            "📝 Nickname": data.get("nickname", ""),
            "📌 Bio": data.get("signature", ""),
            "👥 Follower": data.get("followerCount", 0),
            "➡️ Following": data.get("followingCount", 0),
            "❤️ Likes": data.get("heartCount", 0),
            "🎬 Videos": data.get("videoCount", 0),
            "🤝 Friends": data.get("friendCount", 0),
            "✔️ Verified": "✅" if data.get("verified", False) else "❌",
            "🔐 Private": "🔒" if data.get("privateAccount", False) else "🌐",
            "🌐 Language": data.get("language", ""),
            "🖼️ Avatar Link": data.get("avatarLarger", "")
        }

    except:
        return "error"

def show_info_slow(info):
    slow_type("📋 ᴆᴀɴɢ ᴛʀᴜʏ xᴜᴀ̂́ᴛ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ...\n", delay=0.05)
    time.sleep(0.3)
    for field, value in info.items():
        slow_type(f"{field:<17}: {value}", delay=0.02)
        time.sleep(0.2)

def main():
    intro()
    while True:
        username = input("\nɴʜᴀ̣̂ᴘ ᴜꜱᴇʀɴᴀᴍᴇ ᴛɪᴋᴛᴏᴋ ( ʜᴏᴀ̣̆ᴄ 'ᴇxɪᴛ' ᴆᴇ̂̉ ᴛʜᴏᴀ́ᴛ ) : ").strip()
        if username.lower() == "exit":
            slow_type("</>ᴅɢᴄᴏɴɢᴛʜᴀɴʜ >< ᴛᴀ̣ᴍ ʙɪᴇ̣̂ᴛ 🔰", delay=0.03)
            break

        slow_type(f"\n🔍 Đang tìm @{username} ...", delay=0.03)
        loading_bar()

        info = fetch_tiktok_info(username)
        if info == "error":
            slow_type("[!] ᴋʜᴏ̂ɴɢ ᴛʜᴇ̂̉ ʟᴀ̂́ʏ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ. ᴠᴜɪ ʟᴏ̀ɴɢ ᴛʜᴜ̛̉ ʟᴀ̣ɪ.", delay=0.03)
        elif info is None:
            slow_type(f"[!] ᴋʜᴏ̂ɴɢ ᴛɪ̀ᴍ ᴛʜᴀ̂́ʏ ᴛʜᴏ̂ɴɢ ᴛɪɴ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ @{username}", delay=0.03)
        else:
            show_info_slow(info)

if __name__ == "__main__":
    main()