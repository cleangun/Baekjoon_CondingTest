#큰 수의 법칙
#추정 난이도 : bronze2
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
max_multier = m - (m // (k + 1))
min_multier = m // (k + 1)
print((max_multier * arr[-1]) + (min_multier * arr[-2]))
