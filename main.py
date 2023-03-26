# baekjoon gold5 1107 - 리모컨
import sys
input = sys.stdin.readline

#function
def find_more(full_num,last_num,numlist):
  # last_num = "457" / numlist [ 1 2 3 5 9 0]
  small = 0
  big = 0
  for turn in range(2):
    for i in range(len(last_num)-1,-1,-1):
      mid = int(last_num[0])
      if turn == 0:  # 작은 수를 구할 차례
        if i == (len(last_num)-1):
          while mid >= 0:
            if (mid < int(last_num[0])) and (mid in numlist):
              small += mid * (10**i)
              break
            mid -= 1
        else:
          if i == 0:
            small += max(numlist)
          else:
            small += max(numlist) * (10**i)
      else:  # 큰 수를 구할 차례
        if i == (len(last_num)-1):
          while mid <= 9:
            if (mid > int(last_num[0])) and (mid in numlist):
              big += mid * (10**i)
              break
            mid += 1
        else:
          if i == 0:
            big += min(numlist)
          else:
            big += min(numlist) * (10**i)
  return min([big,small], key=lambda x: abs(x - t))

#main
t = int(input())
n = int(input())
first_cnt = abs(int(t)-100)  # + - 버튼을 이용했을 때 횟수

numlist = list([i for i in range(0,10)])
if n != 0:
  for no_num in list(map(int,input().split())):
    numlist.remove(no_num)

# 예외 처리
if t == 100:
  print(0)
  exit(0)
if len(numlist)==0:
  print(first_cnt)
  exit(0)

combine = ""
for idx in range(len(str(t))):
  if int(str(t)[idx]) in numlist:
    combine += str(t)[idx]
  else:  # 해당 수가 없는 경우
    last_num = str(t)[idx:]
    combine += str(find_more(t,last_num,numlist))
    break
last_cnt = abs(t-int(combine)) + len(combine)
print(last_cnt if last_cnt < first_cnt else first_cnt)
      