import sys
input = sys.stdin.readline

n = int(input())

hotkey = []
for _ in range(n):
    func_String = input().rstrip()
    idx_order = []
    num = 0
    for idx,ch in enumerate(func_String):
        if ch == " ":
            continue
        if (idx == 0) or (func_String[idx-1] == " "):
            if len(idx_order) == 0:
                idx_order.append([ch,idx])
                num += 1
                continue
            else:
                idx_order.insert(num,[ch,idx])
                num += 1
        else:
            idx_order.append([ch,idx])
    for ch,idx in idx_order:
        if ch.upper() not in hotkey:
            hotkey.append(ch.upper())
            cp_String = list(func_String)
            cp_String[idx] = "["+func_String[idx]+"]"
            func_String = "".join(cp_String)
            break
    print(func_String)
        