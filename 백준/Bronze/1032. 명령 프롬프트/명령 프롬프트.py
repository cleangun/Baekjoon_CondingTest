import sys
input = sys.stdin.readline

cmd_arr = []
for _ in range(int(input())):
    cmd_arr.append(input().rstrip())
    
if len(cmd_arr) == 1:
    print(cmd_arr[0])
    exit(0)

result = ""
for idx in range(len(cmd_arr[0])):
    ch = cmd_arr[0][idx]
    special = 0 # 0은 . / 1은 그냥 같은 단어
    for other in cmd_arr[1:]:
        if other[idx] == ch:
            if other[idx] == ".":
                special = 0
            else:
                special = 1
            continue
        else:
            result += "?"
            special = -1
            break
    if special == 1:
        result += ch
        continue
    elif special == 0:
        result += "."
print(result)
    