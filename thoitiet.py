import requests
import time
import os
from datetime import datetime

API_KEY = "liggdzut123"
DEBUG = False
TYPING_DELAY = 0.5  # giây delay giữa các dòng
CHAR_DELAY = 0.03   # giây delay nếu in từng ký tự
TYPE_CHAR_BY_CHAR = False  # đặt True nếu muốn từng ký tự hiện ra như đang gõ

os.system("clear")

def kelvin_to_celsius(k):
    return round(k - 273.15, 1)

def type_print(text: str):
    if TYPE_CHAR_BY_CHAR:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(CHAR_DELAY)
        print()
    else:
        print(text)
        time.sleep(TYPING_DELAY)

def get_weather(city_name: str):
    api_url = f"https://liggdzut.x10.mx/api/weather.php?city={city_name}&key={API_KEY}"
    
    try:
        response = requests.get(api_url)

        if response.status_code != 200:
            if DEBUG:
                type_print(f"[DEBUG] Lỗi HTTP {response.status_code}: {response.text}")
            type_print("⚠️ ᴋʜᴏ̂ɴɢ ᴛʜᴇ̂̉ ʟᴀ̂́ʏ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ ᴛʜᴏ̛̀ɪ ᴛɪᴇ̂́ᴛ. ᴠᴜɪ ʟᴏ̀ɴɢ ᴛʜᴜ̛̉ ʟᴀ̣ɪ ꜱᴀᴜ.")
            return

        try:
            data = response.json()
        except ValueError:
            if DEBUG:
                type_print(f"[DEBUG] JSON không hợp lệ: {response.text}")
            type_print("⚠️ ᴘʜᴀ̉ɴ ʜᴏ̂̀ɪ ᴍᴀ́ʏ ᴄʜᴜ̉ ᴋʜᴏ̂ɴɢ ʜᴏ̛̣ᴘ ʟᴇ̣̂. ᴠᴜɪ ʟᴏ̀ɴɢ ᴛʜᴜ̛̉ ʟᴀ̣ɪ.")
            return

        if "error" in data:
            if DEBUG:
                type_print(f"[DEBUG] Lỗi từ API: {data['error']}")
            type_print("⚠️ ᴛʜᴀ̀ɴʜ ᴘʜᴏ̂́ ᴋʜᴏ̂ɴɢ ᴛᴏ̂̀ɴ ᴛᴀ̣ɪ ʜᴏᴀ̣̆ᴄ ᴋʜᴏ̂ɴɢ ʜᴏ̂̃ ᴛʀᴏ̛̣.")
            return

        name = data.get("name", city_name)
        weather = data.get("weather", [{}])[0]
        main = data.get("main", {})
        wind = data.get("wind", {})
        sys = data.get("sys", {})
        
        type_print(f"🌤️ Thời Tiết Tại {name} :\n")
        type_print(f"🌡️  Nhiệt Độ: {kelvin_to_celsius(main.get('temp', 0))}°C ( Cảm Nhận : {kelvin_to_celsius(main.get('feels_like', 0))}°C )")
        type_print(f"💧 Độ Ẩm: {main.get('humidity', '?')}%")
        type_print(f"🌬️ Gió: {wind.get('speed', '?')} m/s")
        type_print(f"⛅ Trạng Thái: {weather.get('description', '').capitalize()}")
        type_print(f"🌄 Mặt Trời Mọc: {datetime.fromtimestamp(sys.get('sunrise', 0)).strftime('%H:%M:%S')}")
        type_print(f"🌇 Mặt Trời Lặn: {datetime.fromtimestamp(sys.get('sunset', 0)).strftime('%H:%M:%S')}")
    
    except requests.exceptions.RequestException as e:
        if DEBUG:
            type_print(f"[DEBUG] Lỗi kết nối: {e}")
        type_print("⚠️ ᴋʜᴏ̂ɴɢ ᴛʜᴇ̂̉ ᴋᴇ̂́ᴛ ɴᴏ̂́ɪ ᴛᴏ̛́ɪ ᴍᴀ́ʏ ᴄʜᴜ̉.")

if __name__ == "__main__":
    city = input("ɴʜᴀ̣̂ᴘ ᴛᴇ̂ɴ ᴛʜᴀ̀ɴʜ ᴘʜᴏ̂́ : ").strip()
    type_print("⏳ ᴆᴀɴɢ ʟᴀ̂́ʏ ᴅᴜ̛̃ ʟɪᴇ̣̂ᴜ ᴛʜᴏ̛̀ɪ ᴛɪᴇ̂́ᴛ...")
    get_weather(city)