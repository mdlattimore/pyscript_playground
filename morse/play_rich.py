import time
from rich import print as rp
colors = ["red", "blue", "yellow", "green"]

for color in colors:
    rp(f"[{color}]X", end="", flush=True)
    time.sleep(1)
    print("\b", end="", flush=True)