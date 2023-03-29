# baekjoon 1107 - 리모컨
# 수많은 실패, 수많은 반례
# 결국 정답은 Brute Force;;;
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(str, input().split()))
cnt = abs(100 - n)

for i in range(1000001):
  target = str(i)

  for j in target:
    if j in broken:
      break

  else:
    cnt = min(cnt, len(target) + abs(i - n))
print(cnt)

# 아래는 내 시도 (Brute Force 사용 X)
# 결과는 실패 ( 30퍼까지 성공 -> ValueError 해결 실패)

#-----------------------------------------------------
# import sys
# input = sys.stdin.readline

# t = int(input())
# first_cnt = abs(t - 100)
# numlist = list([i for i in range(0, 10)])
# n = int(input())

# if n == 0:
#   print(first_cnt if first_cnt < len(str(t)) else len(str(t)))
#   exit(0)

# for idx in list(map(int, input().split())):
#   numlist[idx] = -1

# if numlist.count(-1) == 10:
#   print(first_cnt)
#   exit(0)

# combine = ""
# string_t = str(t)
# for idx in range(len(string_t)):
#   number = int(string_t[idx])
#   if number in numlist:
#     combine += str(number)
#   else:
#     pluslen = len(string_t[idx:]) - 1
#     last_num = int(string_t[idx:])
#     big = ""
#     small = ""

#     for numidx in range(number, len(numlist)):
#       if numlist[numidx] != -1:
#         big += str(numlist[numidx])
#         for j in range(pluslen):
#           big += str(min([x for x in numlist if x != -1]))
#         break
#     if len(big) == 0:
#       big += str(min([x for x in numlist if (x != -1) and (x != 0)]))
#       for _ in range(len(string_t)):
#         big += str(min([x for x in numlist if x != -1]))

#     for numidx in range(number, -1, -1):
#       if numlist[numidx] != -1:
#         small = str(numlist[numidx])
#         for j in range(pluslen):
#           small += str(max([x for x in numlist if x != -1]))
#         break
#     if len(small) == 0:
#       for _ in range(len(string_t) - 1):
#         small += str(max([x for x in numlist if x != -1]))

#     biggap = abs(last_num - int(big))
#     smallgap = abs(last_num - int(small))

#     if biggap == smallgap:
#       combine += small
#     elif biggap > smallgap:
#       combine += small
#     else:
#       combine += big

#     break
# last_cnt = len(combine)
# combine = int(combine)
# last_cnt += abs(t - combine)
# print(first_cnt if first_cnt < last_cnt else last_cnt)

#-----------------------------------------------------------------
