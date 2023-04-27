import sys
input = sys.stdin.readline
l,r = map(int,input().split())

minimum_count = 0

if len(str(l)) == len(str(r)):
    for i in range(len(str(l))):
        if str(l)[i] == str(r)[i]:
            if str(l)[i] == '8':
                minimum_count += 1
        else:
            break
print(minimum_count)