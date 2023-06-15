import sys
input = sys.stdin.readline

st_Arr = input().rstrip().split(".")

for idx in range(len(st_Arr)):
    if len(st_Arr[idx]) % 2 == 1:
        print(-1)
        exit(0)
    div, mod = divmod(len(st_Arr[idx]),4)
    tmp = 'A'*4*div + 'B'*mod
    st_Arr[idx] = tmp
print(".".join(st_Arr))