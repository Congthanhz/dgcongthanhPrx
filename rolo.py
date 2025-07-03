import requests
import time
import os
os.system("clear")

def hien_cham(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def lay_thong_tin_roblox(username):
    url = "https://liggdzut.x10.mx/api/roblox.php"
    params = {
        "key": "liggdzut123",
        "username": username
    }

    try:
        hien_cham("🔄 ᴆᴀɴɢ ᴛʀᴜʏ ᴠᴀ̂́ɴ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ ᴛᴜ̛̀ ᴍᴀ́ʏ ᴄʜᴜ̉...\n", 0.03)
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("status") != "success":
            hien_cham("⚠️ ᴋʜᴏ̂ɴɢ ᴛɪ̀ᴍ ᴛʜᴀ̂́ʏ ᴛʜᴏ̂ɴɢ ᴛɪɴ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ.", 0.03)
            return

        info = data["data"]
        basic = info.get("basicInfo", {})

        hien_cham(f"✅ ᴛʜᴏ̂ɴɢ ᴛɪɴ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ ʀᴏʙʟᴏx : {basic.get('displayName', username)}\n", 0.03)
        hien_cham(f"- ᴛᴇ̂ɴ ɴɢᴜ̛ᴏ̛̀ɪ ᴅᴜ̀ɴɢ : {basic.get('name', '')}")
        hien_cham(f"- ᴍᴏ̂ ᴛᴀ̉ : {basic.get('description', '(không có)')}")
        hien_cham(f"- ɴɢᴀ̀ʏ ᴛᴀ̣ᴏ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ : {basic.get('created', '')[:10]}")
        hien_cham(f"- ʜᴜʏ ʜɪᴇ̣̂ᴜ xᴀ́ᴄ ᴍɪɴʜ : {'✔️ Có' if basic.get('hasVerifiedBadge') else '❌ Không'}")
        hien_cham(f"- ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ ʙɪ̣ ᴋʜᴏ́ᴀ : {'🔒 Có' if basic.get('isBanned') else '🔓 Không'}")
        hien_cham(f"- ɢᴏ́ɪ ᴘʀᴇᴍɪᴜᴍ : {'✅ Có' if info.get('isPremium') else '❌ Không'}")
        hien_cham(f"- ꜱᴏ̂́ ʙᴀ̣ɴ ʙᴇ̀ : {info.get('friendCount', 0)}")
        hien_cham(f"- ꜱᴏ̂́ ɴɢᴜ̛ᴏ̛̀ɪ ᴛʜᴇᴏ ᴅᴏ̃ɪ : {info.get('followersCount', 0)}")

        # Tên cũ
        if "usernameHistory" in info:
            hien_cham("\n📜 ᴄᴀ́ᴄ ᴛᴇ̂ɴ ᴆᴀ̃ ᴛᴜ̛̀ɴɢ ꜱᴜ̛̉ ᴅᴜ̣ɴɢ :")
            for item in info["usernameHistory"]:
                hien_cham(f"  • {item['name']}")

        # Nhóm
        if "groups" in info:
            hien_cham("\n👥 ɴʜᴏ́ᴍ ᴆᴀɴɢ ᴛʜᴀᴍ ɢɪᴀ :")
            for group_item in info["groups"]:
                group = group_item["group"]
                role = group_item["role"]
                ten_nhom = group.get("name", "")
                ten_vai_tro = role.get("name", "")
                hien_cham(f"  • {ten_nhom} ({ten_vai_tro})")

    except:
        hien_cham("❌ ᴆᴀ̃ xᴀ̉ʏ ʀᴀ ʟᴏ̂̃ɪ ᴋʜɪ ᴋᴇ̂́ᴛ ɴᴏ̂́ɪ ʜᴏᴀ̣̆ᴄ xᴜ̛̉ ʟʏ́ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ.", 0.03)

if __name__ == "__main__":
    hien_cham("\n🎮 ᴄᴏ̂ɴɢ ᴄᴜ̣ ᴋɪᴇ̂̉ᴍ ᴛʀᴀ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ ʀᴏʙʟᴏx \n", 0.04)
    ten = input("👉 ɴʜᴀ̣̂ᴘ ᴛᴇ̂ɴ ᴛᴀ̀ɪ ᴋʜᴏᴀ̉ɴ ʀᴏʙʟᴏx : ").strip()
    lay_thong_tin_roblox(ten)