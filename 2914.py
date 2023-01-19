count = int(input())
rs = 0.0
for i in range(count):
  calc_list = list(input().split())

  for j in range(len(calc_list)):
    if (j == 0):
      rs = float(calc_list[j])
      continue
    elif (calc_list[j] == '@'):
      rs *= 3
    elif (calc_list[j] == '%'):
      rs += 5
    elif (calc_list[j] == '#'):
      rs -= 7
  print("{:.2f}".format(float(rs)))