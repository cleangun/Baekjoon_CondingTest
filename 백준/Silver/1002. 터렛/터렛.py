import sys
import math
input = sys.stdin.readline
sqrt = math.sqrt

T = int(input())

# 답은 0, 1, 2중에 하나다
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    if (distance == 0) and (r1 == r2):
        print(-1)        
    elif (r1 + r2 == distance) or (abs(r1 - r2) == distance):
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)
    
    