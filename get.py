import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.style import Style
from art import text2art
from datetime import datetime

console = Console()

PROXY_SOURCES = [
    "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol=http&proxy_format=ipport&format=text&timeout=5000",
    "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc",
    "https://api.openproxy.space/lists/http",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://api.getproxylist.com/proxy?protocol[]=http"
]

CHECK_URL = "http://httpbin.org/ip"
OUTPUT_FILE = "proxy.txt"
REQUIRED_PROXIES = 500

proxy_list = []
live_proxies = []
lock = threading.Lock()

def print_banner():
    banner = text2art("dgcongthanh", font="standard")
    console.clear()
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print("[bold green]Proxy Tool By @dgcongthanh[/bold green]")
    time.sleep(1)

def fetch_proxies(api):
    try:
        r = requests.get(api, timeout=8)
        if r.status_code == 200:
            if "proxyscrape" in api or "raw.githubusercontent" in api:
                return [p for p in r.text.splitlines() if ":" in p]
            elif "geonode" in api or "openproxy" in api:
                return [f"{p['ip']}:{p['port']}" for p in r.json()['data']]
            elif "getproxylist" in api:
                d = r.json()
                return [f"{d['ip']}:{d['port']}"]
    except:
        console.print(f"[red]Lỗi khi kết nối: {api}[/red]")
    return []

def gather_proxies():
    with Progress(SpinnerColumn(style="yellow"), TextColumn("{task.description}"), BarColumn()) as progress:
        task = progress.add_task("Đang lấy proxy từ các nguồn...", total=len(PROXY_SOURCES))
        with ThreadPoolExecutor(max_workers=20) as ex:
            results = ex.map(fetch_proxies, PROXY_SOURCES)
            for res in results:
                proxy_list.extend(res)
                progress.advance(task)
    proxy_list[:] = list(dict.fromkeys(proxy_list))
    console.print(Panel.fit(f"Đã thu thập {len(proxy_list)} proxy.", border_style="green"))

def check_proxy(proxy):
    try:
        r = requests.get(CHECK_URL, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=2)
        if r.status_code == 200:
            with lock:
                live_proxies.append(proxy)
    except:
        pass

def main():
    print_banner()
    console.print("[bold green]Bắt đầu kiểm tra proxy...[/bold green]")
    start_time = time.time()
    attempt = 1

    while len(live_proxies) < REQUIRED_PROXIES:
        proxy_list.clear()
        gather_proxies()

        if not proxy_list:
            console.print("[bold red]Không lấy được proxy từ nguồn nào![/bold red]")
            break

        with Progress(SpinnerColumn(), TextColumn("{task.description}"), BarColumn()) as progress:
            task = progress.add_task("Đang Kiểm Tra ...", total=len(proxy_list))
            with ThreadPoolExecutor(max_workers=200) as ex:
                results = list(ex.map(check_proxy, proxy_list))
                for _ in results:
                    progress.advance(task)

        console.print(Panel.fit(f"Lần {attempt}: Có {len(live_proxies)} Proxy Hoạt Động.", border_style="cyan"))
        attempt += 1
        time.sleep(1)

    if live_proxies:
        with open(OUTPUT_FILE, "w") as f:
            for p in live_proxies:
                f.write(f"http://{p}\n")
        console.print(Panel.fit(f"[bold green]Đã lưu {len(live_proxies)} proxy vào {OUTPUT_FILE}.[/bold green]", border_style="green"))

    duration = time.time() - start_time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    console.print(Panel.fit(f"\n[bold cyan]Hoàn tất lúc {now}\nThời gian xử lý: {duration:.2f}s\nProxy hoạt động: {len(live_proxies)}[/bold cyan]", border_style="blue"))

if __name__ == "__main__":
    main()
