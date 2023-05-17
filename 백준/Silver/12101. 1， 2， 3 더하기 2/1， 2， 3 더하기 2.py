import sys
input = sys.stdin.readline
from itertools import permutations

n , m = map(int,input().rstrip().split())

res = set()

# 3의 갯수
for three in range(0,(n//3)+1):
    leftnum = n - (three*3)
    for two in range(0,(n//2)+1):
        tmp = []
        leftnum2 = leftnum - (two*2)
        if leftnum2 >= 0:
            one = leftnum2 // 1
            
            for digit in range(0,one):
                tmp.append(1)
            for digit in range(0,two):
                tmp.append(2)
            for digit in range(0,three):
                tmp.append(3)
            for i in permutations(tmp):
                res.add(i)
res = sorted(res)
try:
    print('+'.join(str(num) for num in res[m-1]))
except:
    print(-1)