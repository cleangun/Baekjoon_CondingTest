# 수 이어 쓰기 - 1515 baekjoon
import sys
input = sys.stdin.readline

num_str = input().rstrip()


i = 0
while True:
  i += 1
  num = str(i)
  while len(num) > 0 and len(num_str) > 0:  #i를 새로받고 , 확인할 list가 남을때까지
    if num[0] == num_str[0]:  # i가 찾고 있는 수를 찾았을때
      num_str = num_str[1:]
    num = num[1:]  # 계속 앞의 숫자를 짤라주기 위함
  if num_str == '':  # 찾을 대상이 비었을 때 => 정답 찾음
    print(i)
    break
      
    