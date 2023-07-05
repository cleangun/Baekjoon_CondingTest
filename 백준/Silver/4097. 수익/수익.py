import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    dp = [int(input()) for i in range(n)]
    for idx in range(1, len(dp)):
        dp[idx] = max(dp[idx], dp[idx] + dp[idx-1])
    print(max(dp))