import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    count = 0
    major = 0
    max = 0
    getlist = list(map(int,input().rstrip().split()))
    size = getlist[0]
    getlist = sorted(getlist[1:])
    
    before_num = 0
    
    
    for num in sorted(getlist[1:]):
        if count == 0:
            major = num
        if major == num:
            count += 1
            if count > max:
                max = count
        else:
            count = max
            count -= 1
    print(major)
    
        
    
    
    
