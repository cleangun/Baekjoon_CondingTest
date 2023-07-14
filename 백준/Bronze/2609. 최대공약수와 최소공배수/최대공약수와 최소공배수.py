import sys
input = sys.stdin.readline

n1,n2 = map(int,input().split())

minnum = min(n1,n2)
maxnum = max(n1,n2)

num = 1
for d in range(1,minnum+1):
    num = minnum // d
    if (minnum % num) == 0:
        if (maxnum % num) == 0:
            print(num)
            break
print(n1*n2//num)