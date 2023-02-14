import sys

stack = []
str_list = sys.stdin.readline().rstrip()
answer = 0

# 함수 정의 - 미완성 작업중

for i in str_list:
  if i == ')':
    t = 0
    while len(stack) != 0:
      top = stack.pop()
      if top == "(":
        if t == 0:
          stack.append(2)
        else:
          stack.append(2 * t)
        break
      elif top == "[":
        print(0)
        exit(0)
      else:
        t = t + int(top)

  elif i == ']':
    t = 0
    while len(stack) != 0:
      top = stack.pop()
      if top == "[":
        if t == 0:
          stack.append(3)
        else:
          stack.append(3 * t)
        break
      elif top == "(":
        print(0)
        exit(0)
      else:
        t = t + int(top)
  else:
    stack.append(i)

print(f"fianl : {stack}")

for i in stack:
  if i == '(' or i == '[' or ')' or ']':
    print(0)
    exit(0)
  else:
    answer += i
print(answer)
