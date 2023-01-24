pride = int(input())

if pride <= 100 and pride >= 90:
  print('A')
elif pride < 90 and pride >= 80:
  print('B')
elif pride < 80 and pride >= 70:
  print('C')
elif pride < 70 and pride >= 60:
  print('D')
else:
  print('F')