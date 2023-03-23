#큰 수의 법칙
#추정 난이도 : bronze2
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print( ((m -m // (k + 1)) * arr[-1] ) + 
			( (m // (k + 1)) * arr[-2]) )
