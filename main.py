# 수 이어 쓰기 - 1515 baekjoon
import sys
input = sys.stdin.readline

num_str = input().rstrip()

numlist = []
min = 0
print(num_str)

def find_min(minum,chkNum):
  frt_num = chkNum
  back_num = chkNum*10
  print(f"chkNum = {chkNum}")
  print(f"back_num = {back_num}")
  if frt_num <= minum:
    tenCnt = 0
    while 1:
      if frt_num > minum:
        if back_num < frt_num and back_num is not int(0):
          print(f"back turn..!!")
          temp = back_num
          while temp <= minum:
            temp += 1
            if temp % 10 == 0:
              return frt_num
          return temp
        else:
          return frt_num
      else:
        frt_num += 10
        tenCnt += 1
        print(f"frt_num changed = {frt_num}")

      if tenCnt % 10 == 0:
        back_num *= 10
  else:
    return frt_num
  
min = int(num_str[0])
for ch in num_str[1:]:
  print()
  print(f"before min = {min}")
  min = find_min(min,int(ch))
  print(f"after min = {min}")

print(min)