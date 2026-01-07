import os
import sys
import subprocess
import random
import requests
import time
import threading
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

def install_dependencies():
    requirements = ['requests', 'colorama', 'tqdm']
    for package in requirements:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def show_watermark():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "######################################")
    print(Fore.GREEN + "#                V-RIP               #")
    print(Fore.BLUE +  "#      POWERED BY SCRAPPEY ENGINE    #")
    print(Fore.MAGENTA + "#        VIEW BOT v2.2 - XBYPASS     #")
    print(Fore.CYAN +    "#  https://scrappey.com/?via=V-RIP   #")
    print(Fore.WHITE +   "#     (Ctrl+Click to open link)      #")
    print(Fore.GREEN + "#           made by blade            #")
    print(Fore.GREEN + "######################################")
    print(f"\n{Fore.YELLOW}{Style.BRIGHT} [!] NOTICE: Due to site's anti-spam system,")
    print(f"{Fore.YELLOW}     some views might be lost or not counted.")

API_ENDPOINT = "https://publisher.scrappey.com/api/v1"

def log(msg, level="INFO"):
    color = {"INFO": Fore.CYAN, "SUCCESS": Fore.GREEN, "ERROR": Fore.RED, "WARNING": Fore.YELLOW}.get(level, Fore.WHITE)
    emoji = {"INFO": "ℹ️", "SUCCESS": "✅", "ERROR": "❌", "WARNING": "⚠️"}.get(level, "")
    print(f"\n{color}{emoji} [{level}] {msg}{Style.RESET_ALL}")

def main():
    install_dependencies()
    show_watermark()
    
    print(f"\n{Fore.WHITE}{Style.BRIGHT} > System Ready.")
    print(f"{Fore.RED}{Style.BRIGHT} > Cost: 4 credits per view.")
    print(f"{Fore.CYAN}{Style.BRIGHT} > Bypass Method: XBYPASS v2.2 (Deep Sync)\n")
    
    api_key = input(f"{Fore.YELLOW}🔑 SCRAPPEY API KEY: {Style.RESET_ALL}").strip()
    target_url = input(f"{Fore.YELLOW}🌐 TARGET URL: {Style.RESET_ALL}").strip()
    max_views = int(input(f"{Fore.YELLOW}🔁 TOTAL VIEWS: {Style.RESET_ALL}").strip())

    countries = ["UnitedStates", "UnitedKingdom", "Canada", "Germany", "France", "Netherlands", "Japan"]
    successful_views = 0

    while successful_views < max_views:
        i = successful_views + 1
        country = random.choice(countries)
        print(f"{Fore.CYAN}ℹ️ [INFO] Syncing View {i}/{max_views} (Proxy: {country})...")
        shared_state = {"done": False, "status": "ERROR", "msg": "Failed", "retry": False}
        
        def run_api():
            session_id = f"vrip_{random.randint(10000, 99999)}_{time.time()}"
            payload = {
                "cmd": "request.get",
                "url": target_url,
                "browser": ["chrome"],
                "render": True,
                "screenshot": True,
                "no_cache": True,
                "session": session_id,
                "proxyCountry": country,
                "premiumProxy": True,
                "mouseMovements": True,
                "customHeaders": {
                    "referer": "https://www.google.com/search?q=guns.lol",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                    "accept-language": "en-US,en;q=0.9"
                },
                "wait": 45000,
                "wait_for_selector": "body"
            }
            try:
                r = requests.post(API_ENDPOINT, params={"key": api_key}, json=payload, timeout=260)
                if r.status_code == 200:
                    shared_state["status"], shared_state["msg"] = "SUCCESS", f"View #{i} Synced! ✅"
                else:
                    shared_state["retry"] = True
            except:
                shared_state["retry"] = True
            finally:
                shared_state["done"] = True

        thread = threading.Thread(target=run_api, daemon=True)
        thread.start()

        bar_format = f"V-RIP v2.2: {{percentage:3.0f}}% |{Fore.MAGENTA}{{bar}}{Style.RESET_ALL}|"
        with tqdm(total=100, desc="⏳ Syncing", ncols=70, bar_format=bar_format, ascii=". /", leave=True) as pbar:
            while not shared_state["done"]:
                if pbar.n < 99:
                    time.sleep(2.2)
                    pbar.update(1)
                else:
                    time.sleep(1)
            pbar.update(100 - pbar.n)

        if not shared_state["retry"] and shared_state["status"] == "SUCCESS":
            log(shared_state["msg"], "SUCCESS")
            successful_views += 1
            wait_time = random.randint(40, 70) if successful_views % 3 == 0 else random.randint(15, 25)
            print(f"{Fore.YELLOW}🚀 [Cool-down] Waiting {wait_time}s...")
            time.sleep(wait_time)
        else:
            log("Server Busy - Retrying View #" + str(i), "WARNING")
            time.sleep(15)

    print(Fore.GREEN + Style.BRIGHT + "\n🔥 TASK COMPLETED! CHECK PANEL NOW! 🔥")
    input("\nPress Enter to close...")

if __name__ == "__main__":
    main()