import argparse
import requests
from pathlib import Path

parser = argparse.ArgumentParser(description="Get AoC input file")
parser.add_argument("-y", "--year", type=int, default=2024, help="Year to grab file from")
parser.add_argument("-d", "--day", type=int, default=1, help="Day to grab file from")
parser.add_argument("-c", "--cookie", type=Path, default=Path("cookie.txt"), help="Path to cookie file (default cookie.txt)")

args = parser.parse_args()

if not args.cookie.exists():
    print("error: cokkie file does not exist")
    exit(1)
    
with args.cookie.open() as f:
    cookie = f.read().strip()
    
useragent = "zevaryx/adventofcode on GitHub"

headers = {"User-Agent": useragent}
cookies = {"session": cookie}

r = requests.get(f"https://adventofcode.com/{args.year}/day/{args.day}/input", headers=headers, cookies=cookies)

r.raise_for_status()

output = Path(f"{args.year}/day{args.day}/input.txt")

with output.open("w+") as f:
    f.write(r.content.decode("UTF8"))
    
print(f"Got input for {args.year} day {args.day}! Saved to {output}")