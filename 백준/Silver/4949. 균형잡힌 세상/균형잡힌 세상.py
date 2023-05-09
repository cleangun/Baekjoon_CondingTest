import sys
input = sys.stdin.readline



while True:
    input_str = input().rstrip()
    stack = []

    if input_str == ".":
        break

    for ch in input_str[:-1]:
        if ch == "(" or ch == ")" or ch == "[" or ch == "]":
            if len(stack) == 0:
                stack.append(ch)
            elif (stack[-1] == "[" and ch == "]") or (stack[-1] == "(" and ch == ")"):
                stack.pop(-1)
            else:
                stack.append(ch)
    print("yes") if len(stack) == 0 else print("no")