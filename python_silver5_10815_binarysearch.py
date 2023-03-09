# silver5 숫자카드 - 10815

import sys
input = sys.stdin.readline

input()
slist = sorted(list(map(int,input().split())))
print(slist)
input()
chklist = map(int,input().split())
for i in chklist:
    l, r = 0, len(slist)-1
    while l <= r:
        mid = (l+r)//2
        if slist[mid] == i:
            print(1, end=" ")
            break
        elif slist[mid] > i:
            r = mid - 1
        else:
            l = mid + 1
    else:
        print(0, end=" ")

# binary search를 사용했을때의 코드이다
