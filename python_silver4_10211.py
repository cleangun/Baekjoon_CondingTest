# Baekjoon silver4 10211 - Maximum SubArray
import sys

input = sys.stdin.readline
loop = int(input())

# main
for _ in range(loop):
  n = int(input())

  dp = [int(digit) for digit in input().rstrip().split()]
  for idx in range(1, n):
    dp[idx] = max(dp[idx], dp[idx] + dp[idx - 1])
  print(max(dp))
