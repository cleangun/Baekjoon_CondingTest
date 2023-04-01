# baekjoon - 팰린드룸 만들기 silver3
# 알고보니 그냥 사전순 정렬;;;
# 값이 많은 알파벳순 인줄 알았는데 문제 이해 잘못함
import sys

input = sys.stdin.readline

str_list = dict()
for ch in input().rstrip():
  if ch not in str_list:
    str_list[ch] = 1
  else:
    str_list[ch] += 1
str_list = [[k, v] for k, v in sorted(str_list.items())]
# str_list = [[k, v] for k, v in sorted(str_list.items(), key=lambda x: (-x[1], x[0]))]

front_list = []
back_list = []
odd_check = 0
odd_idx = 0
for idx in range(len(str_list)):
  while str_list[idx][1] >= 2:
    front_list.append(str_list[idx][0])
    back_list.append(str_list[idx][0])
    str_list[idx][1] -= 2
  if str_list[idx][1] > 0:
    odd_check += 1
    odd_idx = idx
    if odd_check >= 2:
      print("I'm Sorry Hansoo")
      exit(0)

if odd_check == 1:
  front_list.append(str_list[odd_idx][0])
for ch in front_list:
  print(ch, end="")
for ch in reversed(back_list):
  print(ch, end="")
