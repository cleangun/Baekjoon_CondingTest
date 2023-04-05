
# import sys - knapsack 문제

# input = sys.stdin.readline

# n, limit = map(int, input().split())
# kg_list = list(map(int, input().split()))

# cnt = 1
# dp = [[0] * (limit + 1) for i in range(n)]

# def knapsack(kg_list, cnt, limit, sum):
#   if sum > limit:
#     return cnt
#   if sum <= limit and (len(kg_list) == 0):
#     cnt += 1
#     return cnt

#   kg = kg_list[0]
#   cnt = knapsack(kg_list[1:], cnt, limit, sum + kg)
#   # print(f"if 1 cnt = {cnt}")
#   cnt = knapsack(kg_list[1:], cnt, limit, sum)
#   # print(f"if 0 cnt = {cnt}")

#   return cnt

# print(knapsack(kg_list, 0, limit, 0))
