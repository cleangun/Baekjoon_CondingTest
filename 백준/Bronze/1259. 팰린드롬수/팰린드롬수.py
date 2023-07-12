import sys
input = sys.stdin.readline

while True:
    n = [ int(i) for i in input().rstrip() ]
    if n[0] == 0:
        break
    mid = len(n)//2
    isPandrome = True
    for idx in range(mid):
        if n[idx] != n[-(idx+1)]:
            isPandrome = False
            break
    if isPandrome:
        print("yes")
    else:
        print("no")
        