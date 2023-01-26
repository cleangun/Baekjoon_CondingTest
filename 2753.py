year = int(input())

def success():
  print('1')

if year % 4 == 0 and year % 100 != 0:
  success()
elif year % 400 == 0:
  success()
else:
  print('0')