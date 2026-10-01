# -*- coding: utf-8 -*-
"""
================================================================================
              ✦  T E C H   M A S T E R   ✦  FF INFO TOOL
================================================================================
Tool Name : TECH MASTER
Category  : Free Fire Account Information Lookup
Platform  : Termux / Linux / Windows
Language  : Python 3
Author    : TECH MASTER
Version   : 2.0 (Premium Edition)
================================================================================
"""

import os
import sys
import time
import json
import shutil

# ──────────────────────────────────────────────────────────────────────────────
# Auto-install missing dependencies
# ──────────────────────────────────────────────────────────────────────────────
def _ensure_dependencies():
    required = ["requests"]
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            print(f"\033[1;33m[!] '{pkg}' not found. Installing...\033[0m")
            os.system(f"{sys.executable} -m pip install {pkg}")

_ensure_dependencies()

import requests


# ──────────────────────────────────────────────────────────────────────────────
# Premium Color Palette (ANSI 256 / Truecolor + fallback)
# ──────────────────────────────────────────────────────────────────────────────
class Colors:
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    DIM         = "\033[2m"
    UNDERLINE   = "\033[4m"

    # Standard colors
    BLACK       = "\033[30m"
    RED         = "\033[91m"
    GREEN       = "\033[92m"
    YELLOW      = "\033[93m"
    BLUE        = "\033[94m"
    MAGENTA     = "\033[95m"
    CYAN        = "\033[96m"
    WHITE       = "\033[97m"

    # Backgrounds
    BG_RED      = "\033[41m"
    BG_GREEN    = "\033[42m"
    BG_YELLOW   = "\033[43m"
    BG_BLUE     = "\033[44m"
    BG_MAGENTA  = "\033[45m"
    BG_CYAN     = "\033[46m"
    BG_GRAY     = "\033[100m"

    # Extended palette
    ORANGE      = "\033[38;5;208m"
    PINK        = "\033[38;5;205m"
    PURPLE      = "\033[38;5;93m"
    LIME        = "\033[38;5;118m"
    GOLD        = "\033[38;5;220m"
    SKY         = "\033[38;5;39m"
    VIOLET      = "\033[38;5;129m"
    TURQUOISE   = "\033[38;5;80m"


# Gradient list — cycles for rainbow text effect
GRADIENT = [Colors.RED, Colors.ORANGE, Colors.GOLD, Colors.LIME,
            Colors.GREEN, Colors.TURQUOISE, Colors.SKY, Colors.BLUE,
            Colors.VIOLET, Colors.PURPLE, Colors.PINK, Colors.MAGENTA]


# ──────────────────────────────────────────────────────────────────────────────
# Utility helpers
# ──────────────────────────────────────────────────────────────────────────────
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def term_width(default=80):
    try:
        return shutil.get_terminal_size((default, 24)).columns
    except Exception:
        return default


def center(text, width=None):
    w = width or term_width()
    return text.center(w)


def gradient_text(text):
    """Print text with smooth rainbow gradient color."""
    out = []
    for i, ch in enumerate(text):
        out.append(f"{GRADIENT[i % len(GRADIENT)]}{ch}")
    return "".join(out) + Colors.RESET


def strip_ansi(text):
    import re
    return re.sub(r'\033\[[0-9;]*m', '', text)


def visible_len(text):
    return len(strip_ansi(text))


def pad_line(left, right, width=None):
    """Pad a line so left+right is centered visually."""
    w = width or term_width()
    pad_total = max(0, w - visible_len(left) - visible_len(right))
    return left + (" " * pad_total) + right


def hr(char="═", color=Colors.CYAN, width=None):
    w = width or term_width()
    return f"{color}{char * w}{Colors.RESET}"


def thin_hr(width=None):
    return hr("─", Colors.CYAN, width)


# ──────────────────────────────────────────────────────────────────────────────
# Animated spinner for live feedback
# ──────────────────────────────────────────────────────────────────────────────
class Spinner:
    FRAMES = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]

    def __init__(self, message="Working", color=Colors.CYAN):
        self.message = message
        self.color = color
        self.running = False

    def __enter__(self):
        import threading
        self.running = True
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()
        return self

    def _spin(self):
        i = 0
        while self.running:
            frame = self.FRAMES[i % len(self.FRAMES)]
            sys.stdout.write(f"\r{self.color}{frame}{Colors.RESET} {Colors.BOLD}{self.message}...{Colors.RESET} ")
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        sys.stdout.write(f"\r{Colors.GREEN}✔{Colors.RESET} {Colors.BOLD}{self.message} done.   \n")
        sys.stdout.flush()


# ──────────────────────────────────────────────────────────────────────────────
# Banner — premium gradient + dual brand lines
# ──────────────────────────────────────────────────────────────────────────────
BANNER_LINES = [
    " _______        ______   __  __    __  __    __  __    ______  __  __ ",
    "/_  __(_)___   /_  __/  / / / /   / / / /   / / / /   /_  __/ / / / /",
    " / / / / __ \\   / /    / /_/ /   / /_/ /   / /_/ /     / /   / /_/ / ",
    "/ / / / /_/ /  / /    / __  /   / __  /   / __  /     / /   / __  /  ",
    "/_/ /_/\\____/  /_/    /_/ /_/   /_/ /_/   /_/ /_/     /_/   /_/ /_/   ",
]

SUBLINE_1 = "★  FREE  FIRE  ACCOUNT  INTELLIGENCE  TOOL  ★"
SUBLINE_2 = "v2.0  ✦  PREMIUM  EDITION"


def print_banner():
    clear_screen()
    w = term_width()

    # Top divider with gradient dots
    top = f"{Colors.GOLD}◆{Colors.RESET}"
    print()
    print(center(f"{Colors.GOLD}{'◆' * 22}{Colors.RESET}", w))

    # Gradient ASCII art
    print()
    for line in BANNER_LINES:
        print(center(gradient_text(line), w))
    print()

    # Subtitle
    sub = f"{Colors.CYAN}{Colors.BOLD}{SUBLINE_1}{Colors.RESET}"
    print(center(sub, w))

    sub2 = f"{Colors.YELLOW}{SUBLINE_2}{Colors.RESET}"
    print(center(sub2, w))

    print()
    print(center(f"{Colors.GOLD}{'◆' * 22}{Colors.RESET}", w))
    print()

    # Decorative info strip
    info_line = (
        f"{Colors.WHITE}➤ Author : {Colors.LIME}T E C H  M A S T E R{Colors.RESET}"
        f"   {Colors.DIM}|{Colors.RESET}   "
        f"{Colors.WHITE}➤ Platform : {Colors.SKY}Termux / Linux / Windows{Colors.RESET}"
    )
    print(center(info_line, w))
    print()


# ──────────────────────────────────────────────────────────────────────────────
# Box / Card printers
# ──────────────────────────────────────────────────────────────────────────────
def print_box_title(title, color=Colors.GOLD, width=None):
    w = width or min(term_width(), 78)
    pad = max(0, w - visible_len(title) - 4)
    left = 2
    right = pad - left
    line = (
        f"{color}╔{'═' * (w - 2)}╗{Colors.RESET}\n"
        f"{color}║{Colors.RESET} {' ' * left}{Colors.BOLD}{title}{Colors.RESET}{' ' * right}{color}║{Colors.RESET}\n"
        f"{color}╚{'═' * (w - 2)}╝{Colors.RESET}"
    )
    print(center(line, w))


def print_section_divider(width=None):
    w = width or min(term_width(), 78)
    print(center(f"{Colors.CYAN}{'─' * w}{Colors.RESET}", w))


# ──────────────────────────────────────────────────────────────────────────────
# Data formatter — styled cards for dict/list
# ──────────────────────────────────────────────────────────────────────────────
ICONS = {
    "default": "▸",
    "id":      "🆔",
    "name":    "👤",
    "level":   "🎯",
    "rank":    "🏆",
    "kills":   "💥",
    "death":   "☠️",
    "match":   "🎮",
    "win":     "🥇",
    "lose":    "💔",
    "pet":     "🐾",
    "skill":   "⚡",
    "weapon":  "🔫",
    "banner":  "🎨",
    "avatar":  "🖼️",
    "bio":     "📝",
    "region":  "🌍",
    "season":  "📅",
    "credit":  "💰",
    "diamond": "💎",
    "gold":    "🪙",
    "uid":     "🆔",
    "nickname":"👤",
    "account":"👤",
    "booyah":  "🥇",
    "headshot":"🎯",
    "damage":  "💥",
    "playtime":"⏱️",
    "created": "📅",
    "last":    "🕐",
    "time":    "🕐",
    "date":    "📅",
    "status":  "📡",
    "guild":   "🛡️",
    "clan":    "🛡️",
    "team":    "👥",
    "friends": "👥",
    "like":    "❤️",
    "likes":   "❤️",
    "title":   "🎖️",
    "tier":    "🎖️",
}


def pick_icon(key):
    k = key.lower()
    for needle, icon in ICONS.items():
        if needle in k:
            return icon
    return ICONS["default"]


def format_value(value):
    """Pretty-print a scalar value."""
    if value is None:
        return f"{Colors.DIM}—{Colors.RESET}"
    if isinstance(value, bool):
        return f"{Colors.GREEN}YES{Colors.RESET}" if value else f"{Colors.RED}NO{Colors.RESET}"
    if isinstance(value, (int, float)):
        try:
            return f"{Colors.GOLD}{value:,}{Colors.RESET}"
        except Exception:
            return f"{Colors.GOLD}{value}{Colors.RESET}"
    return f"{Colors.WHITE}{value}{Colors.RESET}"


def format_data(data, indent=0):
    """Recursively format JSON response into colorful cards."""
    lines = []
    prefix = " " * indent

    if isinstance(data, dict):
        for key, value in data.items():
            label = key.replace("_", " ").title()
            icon = pick_icon(key)

            if isinstance(value, dict):
                lines.append(f"{prefix}{Colors.SKY}{icon} {Colors.BOLD}{label}{Colors.RESET}")
                lines.extend(format_data(value, indent + 4))
            elif isinstance(value, list):
                if not value:
                    lines.append(f"{prefix}{Colors.SKY}{icon} {Colors.BOLD}{label}{Colors.RESET} : {Colors.DIM}none{Colors.RESET}")
                else:
                    lines.append(f"{prefix}{Colors.SKY}{icon} {Colors.BOLD}{label}{Colors.RESET}")
                    for idx, item in enumerate(value, 1):
                        if isinstance(item, (dict, list)):
                            lines.append(f"{prefix}    {Colors.PINK}─── Item #{idx} ───{Colors.RESET}")
                            lines.extend(format_data(item, indent + 6))
                        else:
                            lines.append(f"{prefix}    {Colors.LIME}●{Colors.RESET} [{Colors.CYAN}{idx}{Colors.RESET}] {format_value(item)}")
            else:
                lines.append(f"{prefix}{Colors.SKY}{icon} {Colors.BOLD}{label:<22}{Colors.RESET} :  {format_value(value)}")
    elif isinstance(data, list):
        for idx, item in enumerate(data, 1):
            if isinstance(item, (dict, list)):
                lines.append(f"{prefix}{Colors.PINK}─── Item #{idx} ───{Colors.RESET}")
                lines.extend(format_data(item, indent + 4))
            else:
                lines.append(f"{prefix}{Colors.LIME}●{Colors.RESET} [{Colors.CYAN}{idx}{Colors.RESET}] {format_value(item)}")
    else:
        lines.append(f"{prefix}{Colors.WHITE}{data}{Colors.RESET}")
    return lines


# ──────────────────────────────────────────────────────────────────────────────
# Header for result section
# ──────────────────────────────────────────────────────────────────────────────
def print_result_header(uid, region):
    w = min(term_width(), 78)
    print()
    print_section_divider(w)
    title = f"  {Colors.GOLD}✦{Colors.RESET}  {Colors.BOLD}{Colors.WHITE}FREE FIRE ACCOUNT DASHBOARD{Colors.RESET}  {Colors.GOLD}✦{Colors.RESET}  "
    print(center(title, w))
    sub = (
        f"{Colors.CYAN}UID{Colors.RESET}  : {Colors.LIME}{uid}{Colors.RESET}     "
        f"{Colors.CYAN}REGION{Colors.RESET} : {Colors.LIME}{region}{Colors.RESET}"
    )
    print(center(sub, w))
    print_section_divider(w)


def print_result_footer():
    w = min(term_width(), 78)
    print()
    print_section_divider(w)
    thanks = f"{Colors.GREEN}{Colors.BOLD}✔  Data fetched successfully via TECH MASTER{Colors.RESET}"
    print(center(thanks, w))
    print_section_divider(w)


# ──────────────────────────────────────────────────────────────────────────────
# Core action — fetch & render account info
# ──────────────────────────────────────────────────────────────────────────────
def fetch_ff_info():
    print_banner()

    # ── Input section
    print_box_title("  ENTER  ACCOUNT  DETAILS  ", Colors.GOLD)

    print()
    uid = input(f"   {Colors.CYAN}➤{Colors.RESET} {Colors.BOLD}Enter UID   {Colors.DIM}:{Colors.RESET} ").strip()
    if not uid:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ Error:{Colors.RESET} {Colors.WHITE}UID cannot be empty!{Colors.RESET}\n")
        time.sleep(1.5)
        return

    print()
    region = input(f"   {Colors.CYAN}➤{Colors.RESET} {Colors.BOLD}Enter Region {Colors.DIM}:{Colors.RESET} ").strip().upper()
    if not region:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ Error:{Colors.RESET} {Colors.WHITE}Region cannot be empty!{Colors.RESET}\n")
        time.sleep(1.5)
        return

    print()
    print_section_divider()

    # ── Network section with spinner
    api_url = f"https://ffinfo-ob55-api-top.vercel.app/ffinfo?uid={uid}&region={region}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; Termux) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    print_result_header(uid, region)

    try:
        with Spinner(f"{Colors.CYAN}Connecting to TECH MASTER API{Colors.RESET}", Colors.CYAN):
            response = requests.get(api_url, headers=headers, timeout=20)
    except requests.exceptions.Timeout:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ TIMEOUT:{Colors.RESET} The API server is taking too long to respond.")
        return
    except requests.exceptions.ConnectionError:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ CONNECTION ERROR:{Colors.RESET} Please check your internet connection.")
        return
    except requests.exceptions.RequestException as e:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ NETWORK ERROR:{Colors.RESET} {e}")
        return

    if response.status_code == 200:
        try:
            json_data = response.json()
            print()
            for line in format_data(json_data):
                print(line)
        except ValueError:
            print()
            for line in response.text.splitlines():
                print(f"   {Colors.LIME}●{Colors.RESET} {Colors.WHITE}{line}{Colors.RESET}")
    elif response.status_code == 404:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ NOT FOUND:{Colors.RESET} Account with UID {Colors.YELLOW}{uid}{Colors.RESET} not found in region {Colors.YELLOW}{region}{Colors.RESET}.")
    else:
        print(f"\n   {Colors.RED}{Colors.BOLD}✖ API ERROR:{Colors.RESET} Received status code {Colors.YELLOW}{response.status_code}{Colors.RESET}.")
        print(f"   {Colors.DIM}{response.text[:300]}{Colors.RESET}")

    print_result_footer()


# ──────────────────────────────────────────────────────────────────────────────
# Main loop
# ──────────────────────────────────────────────────────────────────────────────
def main():
    first = True
    while True:
        fetch_ff_info()

        print()
        print(f"   {Colors.CYAN}➤{Colors.RESET} {Colors.BOLD}Do you want to lookup another UID?{Colors.RESET} "
              f"{Colors.DIM}[{Colors.RESET}{Colors.GREEN}y{Colors.RESET}{Colors.DIM}/{Colors.RESET}{Colors.RED}n{Colors.RESET}{Colors.DIM}]{Colors.RESET} : ", end="")
        choice = input().strip().lower()

        if choice != "y":
            clear_screen()
            print_banner()
            print()
            print(center(
                f"{Colors.GOLD}◆{Colors.RESET}  "
                f"{Colors.BOLD}{Colors.WHITE}Thanks for using {Colors.GOLD}T E C H  M A S T E R{Colors.WHITE}!{Colors.RESET}  "
                f"{Colors.GOLD}◆{Colors.RESET}", term_width()))
            print(center(f"{Colors.CYAN}Follow for more premium tools ✦{Colors.RESET}", term_width()))
            print()
            time.sleep(1.5)
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}{Colors.BOLD}✖ Interrupted.{Colors.RESET} Exiting TECH MASTER...\n")
        sys.exit(0)
