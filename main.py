import os, sys, time, random

# --- VIP COLORS ---
G = '\033[92m'  # Green
G_DIM = '\033[2;92m' # Dim Green
W = '\033[0m'   # White
Y = '\033[93m'  # Yellow

def zeeshan_logo():
    logo = f"""{G}
  ______ ______ ______  _____ _    _          _   _ 
 |___  /|  ____|  ____|/ ____| |  | |   /\   | \ | |
    / / | |__  | |__  | (___ | |__| |  /  \  |  \| |
   / /  |  __| |  __|  \___ \|  __  | / /\ \ | . ` |
  / /__ | |____| |____ ____) | |  | |/ ____ \| |\  |
 /_____||______|______|_____/|_|  |_/_/    \_\_| \_|
       {Y}[ THE HEARTLESS - VIP EDITION ]{G}"""
    print(logo)

def typewriter(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def quick_matrix():
    """Sirf 3-4 second ka background effect"""
    chars = "01ZEESHAN_KHAN_HEARTLESS"
    cols = os.get_terminal_size().columns
    
    # 3 second ka loop (approx 30-40 lines)
    for _ in range(35):
        line = ""
        for _ in range(cols):
            if random.random() < 0.15: # Character density
                line += G_DIM + random.choice(chars) + W
            else:
                line += " "
        print(line)
        time.sleep(0.06)

def start_app():
    os.system('clear')
    zeeshan_logo()
    print(f"\n{G}[!] Initializing VIP Protocols...{W}")
    time.sleep(1)
    
    # Hollywood Dialogue
    print(f"{G}--------------------------------------------------{W}")
    typewriter(f"{G}oh oh ho... System override successful.{W}")
    typewriter(f"{G}Wellllllllcome back, Zeeshaaaaaan khan the Heartless.{W}")
    typewriter(f"{G}All protocols are now under your command.{W}")
    print(f"{G}--------------------------------------------------{W}")
    
    time.sleep(1)
    quick_matrix() # 3 Second Matrix
    
    # Final Transition to Menu
    os.system('clear')
    zeeshan_logo()
    print(f"\n{G}[+] SYSTEM READY. WELCOME MASTER.{W}")
    print(f"\n{Y}--- MAIN MENU ---{W}")
    print("[1] Start Cloner")
    print("[2] Plan Z (AI Generator)")
    print("[3] Script Doctor")
    print("[4] Exit")
    input(f"\n{G}Choose Option: {W}")

if __name__ == "__main__":
    start_app()
    