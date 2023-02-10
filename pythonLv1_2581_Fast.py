#2581 최적의 속도
import sys

dmc_list = []
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
dmc_sum = 0

for chk_num in range(M, N + 1):
  if chk_num > 1:
    if chk_num == 2:
      dmc_list.append(2)
      continue
    elif (chk_num % 2 == 0):
      continue
    else:
      error = False
      for increaseNum in range(3, int(chk_num**0.5) + 1, 2):
        if not error:
          if chk_num % increaseNum == 0:
            error = True
            continue
        else:
          break
      if error == 0:
        dmc_list.append(chk_num)

if len(dmc_list) == 0:
  print(-1)
else:
  print(sum(dmc_list))
  print(min(dmc_list))
