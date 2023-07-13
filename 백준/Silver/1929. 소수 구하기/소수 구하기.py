import sys
input = sys.stdin.readline

m, n = map(int,input().split())

numList = [True] * (n+1)
numList[0] = False; numList[1] = False;
for i in range(2,len(numList)):
    if numList[i] is True:
        for j in range(i*2,len(numList),i):
            numList[j] = False
    else:
        continue
primeLst = [idx for idx in range(len(numList)) if numList[idx] == True]
for arg in primeLst:
    if m <= arg and arg <= n:
        print(arg)