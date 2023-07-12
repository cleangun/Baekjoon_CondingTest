import sys
input = sys.stdin.readline

k, n = map(int,input().rstrip().split())
linelst = []
for _ in range(k):
    linelst.append(int(input()))
    
start = 0
end = max(linelst)+1
result = 0
while True:
    mid = (start+end) // 2
    if abs(start-end) <= 1:
        break
    cnt = sum([num // mid for num in linelst])
    if cnt >= n:
        if mid > result:
            result = mid
        start = mid
    elif cnt < n:
        end = mid
print(result)