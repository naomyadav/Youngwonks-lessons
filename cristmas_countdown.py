#Christmas Countdown By Copilot


import os
import sys
import time
import signal
import shutil
from datetime import datetime, timedelta

def _clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def _prompt_yes_no(prompt, default=True):
    default_str = "Y/n" if default else "y/N"
    try:
        resp = input(f"{prompt} [{default_str}]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return default
    if resp == "":
        return default
    return resp[0] == "y"

def _get_target_christmas(year_choice):
    now = datetime.now()
    if year_choice == "next":
        year = now.year if now.month < 12 or (now.month == 12 and now.day <= 25) else now.year + 1
    elif year_choice == "this":
        year = now.year
    else:
        try:
            year = int(year_choice)
            if year < now.year:
                year = now.year
        except Exception:
            year = now.year
    return datetime(year, 12, 25, 0, 0, 0)

def _format_delta(delta: timedelta):
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        return "It's already past that date!"
    days, rem = divmod(total_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days} day{'s' if days!=1 else ''}")
    parts.append(f"{hours:02d}h")
    parts.append(f"{minutes:02d}m")
    parts.append(f"{seconds:02d}s")
    return ", ".join(parts)

def _handle_exit(signum, frame):
    print("\nExiting. Happy holidays!")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, _handle_exit)
    signal.signal(signal.SIGTERM, _handle_exit)

    print("Christmas Countdown — friendly mode")
    print("----------------------------------")
    print("You can count down to the next Christmas, this year's Christmas, or a specific year.")
    year_choice = input("Enter 'next', 'this', or a 4-digit year [next]: ").strip().lower() or "next"
    target = _get_target_christmas(year_choice)

    clear_each = _prompt_yes_no("Clear the screen each update?", default=True)
    show_header = _prompt_yes_no("Show header info each update?", default=True)
    try:
        interval = float(input("Update interval in seconds [1]: ").strip() or "1")
        if interval <= 0:
            interval = 1.0
    except Exception:
        interval = 1.0

    try:
        while True:
            columns, _ = shutil.get_terminal_size(fallback=(80, 24))
            now = datetime.now()
            delta = target - now
            if clear_each:
                _clear_screen()
            if show_header:
                title = f"Countdown to Christmas {target.year}".center(columns)
                print(title)
                print("-" * min(len(title), columns))
            if delta.total_seconds() < 0:
                print("🎉 It's Christmas (or past the selected date)!")
                if _prompt_yes_no("Count down to next year's Christmas instead?", default=True):
                    target = _get_target_christmas("next")
                    continue
                break
            print("Time remaining:", _format_delta(delta))
            # friendly idle tick
            time.sleep(interval)
    except KeyboardInterrupt:
        _handle_exit(None, None)
    sys.exit(0)