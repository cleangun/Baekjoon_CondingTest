#baekjoon 1920 - 수 찾기
import sys

input = sys.stdin.readline

n = int(input())
li = set(list(map(int, input().split())))
s = int(input())
for arg in list(map(int, input().split())):
  if arg in li:
    print(1)
    continue
  print(0)
