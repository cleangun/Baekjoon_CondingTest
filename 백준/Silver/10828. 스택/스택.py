import sys
input = sys.stdin.readline

n = int(input())

stack = []

def switch(key):
    if key == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif key == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif key =="size":
        print(len(stack))
    elif key =="pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        

for i in range(n):
    command_input = input().rstrip().split(" ")
    
    if len(command_input) == 2 and command_input[0] == "push" and command_input[1].isdigit():
        stack.append(int(command_input[1]))
        continue
    
    switch(command_input[0])
        