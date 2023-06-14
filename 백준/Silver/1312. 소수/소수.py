import sys
input = sys.stdin.readline

a,b, n = map(int,input().split())

# 한 번에 클리어
# num = (a*(10**n)) / b
# result = str(num*10)[n]
# print(result)

cnt = 0
num = a%b
res = 0
while cnt < n:
    num *= 10
    moc = num // b
    num = num % b
    cnt += 1
    if cnt == n:
        res = moc
        break
print(res)