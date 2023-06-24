import sys
import math
input = sys.stdin.readline
sqrt = math.sqrt


n = int(input())
dp = [ 4 for i in range(n+1) ]
dp[0] = 0


for i in range(1,n+1):
    for j in range(1,i+1):
        val = j*j # 제곱수 계산
        if val > i:
            break
        dp[i] = min(dp[i], dp[i-val]+1)
print(dp[n])
    
