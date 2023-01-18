hour, minute, second = map(int, input().split())
delaySecond = int(input())

second += delaySecond % 60
delaySecond = delaySecond // 60
if second >= 60:
  minute += 1
  second -= 60

minute += delaySecond % 60
delaySecond = delaySecond // 60
if minute >= 60:
  hour += 1
  minute -= 60

hour += delaySecond % 24
if hour >= 24:
  hour -= 24

print(hour, minute, second)
  