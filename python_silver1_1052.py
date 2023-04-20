# Baekjoon silver1 1052 - 물병
# 비트마스킹 알고리즘 문제이다.
import sys
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())

count = 0
while bin(n).count('1') > k:
    print(f"bin(n) : {bin(n)[2:]}")
    n += 1
    count += 1
print(f"final = {bin(n)[2:]}")
print(count)


# --- 실패 코드 ---
# result = 0
# level = 1
# count = 0
# while n > k:
#     if ((n//2)+(n%2)) <= k:
#         break
#     count += 1
#     if ((n % 2) == 1):
#         result += ((level*2) - ((n%2)*level))
#         print(f"<{count}>")
#         print(f"n = {n}")
#         print(f"level append : +{level}")
#         print(f"result = {result}")
#         n = (n//2) + 1
#         print(f"after n = {n}")
#         print("-----------------")
#     else:
#         n = n//2
#     level *= 2
# print(f"n = {n}")
# print(f"level = {level}")
# print(f"result = {result}")

