# D-Day 문제 - silver5
import sys

input = sys.stdin.readline

fyear, fmonth, fday = map(int, input().rstrip().split())
syear, smonth, sday = map(int, input().rstrip().split())

lpyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cmyear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def find_leap(year):
  if year % 4 == 0:
    if year % 400 == 0:  # 윤년
      return True
    elif year % 100 == 0:  # 평년
      return False
    else:  # 윤년
      return True
  else:  # 평년
    return False


result = []
if find_leap(fyear):
  result.append((sum(lpyear[fmonth - 1:]) - fday))
else:
  result.append((sum(cmyear[fmonth - 1:]) - fday))

if find_leap(syear):
  result.append(sum(lpyear[:smonth - 1]) + sday)
else:
  result.append(sum(lpyear[:smonth - 1]) + sday)

for year in range(fyear + 1, syear):
  if find_leap(year):
    result.append(366)
  else:
    result.append(365)

print(f"D-{sum(result)}")
