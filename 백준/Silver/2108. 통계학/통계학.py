import sys
input = sys.stdin.readline

numlst = []
n = int(input())

for _ in range(n):
    numlst.append(int(input()))
numlst.sort()
cntDict = {}
for num in numlst:
    if num not in cntDict:
        cntDict[num] = 1
    else:
        cntDict[num] += 1
max_keys = [key for key,value in cntDict.items() if value == max(cntDict.values())]
# 산술평균
print(round(sum(numlst) / n))
# 중앙값
print(numlst[n//2])
# 최빈값
if len(max_keys) > 1:
    print(max_keys[1])
else:
    print(max_keys[0])
# 범위
print(abs(max(numlst) - min(numlst)))