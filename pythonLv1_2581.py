import sys

dmc_list = []
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def chk_demical(num):  #소수인지 확인
  if num == 2:
    dmc_list.append(2)
  if (num % 2 == 0) or (num < 2) :
    return False
  else:
    for increaseNum in range(3,num,2):
      if num % increaseNum == 0:
        return False
    return True

for chk_num in range(M,N+1):
  if chk_demical(chk_num):
    dmc_list.append(chk_num)


if len(dmc_list) == 0:
  print(-1)
else:
  print(sum(dmc_list))
  print(min(dmc_list))
  