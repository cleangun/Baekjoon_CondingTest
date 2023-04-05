# knapsack문제
# Baekjoon silver3 14501 - 퇴사
import sys

input = sys.stdin.readline
N = int(input())

knap = [[0, 0]]
for _ in range(N):
  cost, value = map(int, input().split())
  knap.append([cost, value])

dp = [0] * (N + 2)

for idx in range(1, N + 1):
  cost, value = knap[idx]
  if (idx + cost) <= N + 1:
    for j in range(idx + cost, N + 2):
      dp[j] = max(dp[idx] + value, dp[j])
# print(dp[1:])
print(max(dp))
