import sys
input = sys.stdin.readline

getStr = input().rstrip()
arr = []
before = ""
idx = -1
for ch in getStr:
    if before != ch:
        arr.append(ch)
        idx += 1
    else:
        arr[idx] = arr[idx] + ch
    before = ch

for idx in range(len(arr)):
    if arr[idx].count(".") >= 1:
        continue
    if len(arr[idx])%2 == 1:
        print(-1)
        exit(0)
    if len(arr[idx])%4 == 0:
        arr[idx] = arr[idx].replace("X","A")
    else:
        axis = (len(arr[idx])//4)*4
        arr[idx] = arr[idx].replace("X","A",axis)
        arr[idx] = arr[idx].replace("X","B",2)
print("".join(arr))