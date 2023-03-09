import sys

N = int(sys.stdin.readline())

ans = []
stack = []
i = 0

for _ in range(N):
    find_num = int(sys.stdin.readline())
    if find_num > i:
        while i < find_num:
            i += 1
            stack.append(i)
            ans.append("+")
    if find_num == stack[-1]:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        exit(0)

for i in ans:
    print(i)