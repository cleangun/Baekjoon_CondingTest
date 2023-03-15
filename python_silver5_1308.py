# D-Day 문제 - silver5
from datetime import datetime
import sys

input = sys.stdin.readline


def get_1000_year(start_year):
  result = 0
  for year in range(start_year, start_year + 1000):
    if year % 400 == 0:
      result += 366
    elif year % 100 == 0:
      result += 365
    elif year % 4 == 0:
      result += 366
    else:
      result += 365
  return result


today = list(map(int, input().rstrip().split()))
dday = list(map(int, input().rstrip().split()))

year1000 = get_1000_year(today[0])

today = datetime(year=today[0], month=today[1], day=today[2])
dday = datetime(year=dday[0], month=dday[1], day=dday[2])
days = (dday - today).days
if days >= year1000:
  print("gg")
else:
  print(f"D-{days}")
