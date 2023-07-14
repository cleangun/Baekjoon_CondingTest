import sys
input = sys.stdin.readline

n1,n2 = map(int,input().split())

minnum = min(n1,n2)
maxnum = max(n1,n2)

d = 1
while (minnum // d) > 0:
    num = minnum // d
    if (minnum % num) == 0:
        if (maxnum % num) == 0:
            print(num)
            break
    d += 1
d = 1
while True:
    num = maxnum * d
    if (num % minnum) == 0:
        print(num)
        break
    d += 1