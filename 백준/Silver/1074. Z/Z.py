import sys
input = sys.stdin.readline
def recursion(n,r,c):
    if n == 0:
        return 0
    size = 2 ** (n-1)
    
    if r < size and c < size:
        return recursion(n-1,r,c)
    elif r < size and c >= size: # 오른쪽 위
        return size**2 + recursion(n-1, r, c-size)
    elif r >= size and c < size: # 왼쪽 아래
        return 2*size**2 + recursion(n-1, r-size, c)
    else: # 오른쪽 아래
        return 3*size**2 + recursion(n-1, r-size, c-size)
n,r,c = map(int,input().split())

print(recursion(n,r,c))