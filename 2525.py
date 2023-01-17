hour, minute = map(int, input().split())
ovendelay = int(input())

hour += int(ovendelay / 60)
minute += int(ovendelay % 60)

if minute >= 60:
  hour += 1
  minute -= 60
if hour >= 24:
  hour -= 24

print(hour, minute)