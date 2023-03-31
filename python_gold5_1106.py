# Baekjoon 1106 - Gold5 - 호텔문제
# 첫째줄에 C, N
# 둘째줄에 N개만큼 호텔의 cost와 해당 비용을 지불했을때 얻을 수 있는 people의 수가 주어짐
# 하지만 C는 최소한 C만큼 얻어야하므로 people의 용량이 오버해도 상관없음
# => 최소한의 개수만 구하면 된다.
# DFS로 풀려고 했지만 틀렸고, 0-1 Knapsack알고리즘을 사용하는 것을 권장 받았다

import sys

input = sys.stdin.readline

c, n = map(int, input().split())
datalist = []
for _ in range(n):
  datalist.append(list(map(int, input().split())))

datalist.sort(key=lambda x: x[1] / x[0], reverse=True)

# 최고의 효율을 가진 index  => datalist[0]
if (c >= datalist[0][1]) and ((c % datalist[0][1]) == 0):
  print((c // datalist[0][1]) * datalist[0][0])
  exit(0)

dp = [1e7 for _ in range(c + 100)]  # dp 리스트 매우 큰값으로 초기화
dp[0] = 0  # 0명 모을 땐, 0원

for cost, people in datalist:  # 각 비용, 비용으로 얻을 수 있는 고객수에 대해
  for idx in range(people, c + 100):  # num_people 부터 C+100 까지 반복
    dp[idx] = min(dp[idx - people] + cost, dp[idx])  # i명일 때, 최소비용 갱신
  # print()
  # for idx,i in enumerate(dp):
  #   print(f"{idx} : {i}")
print(min(dp[c:]))

# 실패 - DFS
# DFS로 문제푸는 것은 성공 - 그러나 최악의 경우 19s까지 돌게 되므로 실패
# def dfs(data, idx, remain, cnt, result):
#   if remain <= 0:
#     if cnt < result:
#       result = cnt
#     return result
#   if (idx >= len(data)) or (cnt > result):
#     return result

#   cost, human = data[idx]
#   for multiple in range((remain // human) + 1, -1, -1):
#     result = dfs(data, idx + 1, remain - (multiple * human),
#                  (cnt + (multiple * cost)), result)
#   return result

# result = 1e9
# print(dfs(datalist, 0, c, 0, result))
