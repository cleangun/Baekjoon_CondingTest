import sys

stack = []
str_list = sys.stdin.readline().rstrip()
answer = 0

# print(str_list)

# 함수 정의 - 미완성 작업중

for i in str_list:
  # print("----------------")
  # print(f" i = {i}")
  if i == ')':
    t = 0
    while len(stack) != 0:
      top = stack.pop()
      # print(" if Success!!")
      # print(f"stack : {stack}")
      # print(f"top : {top}")
      if top == "(":

        if t == 0:
          stack.append(2)
        else:
          stack.append(2 * t)
        # print(f"t => {t}")
        # print(f"stack => {stack}")
        break
      elif top == "[":
        print(0)
        exit(0)
      else:
        # print(f"top = {top}")
        # print(f"int(top) = {int(top)}")
        t = t + int(top)

  elif i == ']':
    t = 0
    while len(stack) != 0:
      top = stack.pop()
      # print(" if Success!!")
      # print(f"stack : {stack}")
      # print(f"top : {top}")
      if top == "[":
        if t == 0:
          stack.append(3)
        else:
          stack.append(3 * t)
        # print(f"t => {t}")
        # print(f"stack => {stack}")
        break
      elif top == "(":
        print(0)
        exit(0)
      else:
        # print(f"top = {top}")
        # print(f"int(top) = {int(top)}")
        t = t + int(top)
  else:
    stack.append(i)
    # print(f"stack = {stack}")

print(f"fianl : {stack}")

for i in stack:
  if i == '(' or i == '[':
    print(0)
    exit(0)
  else:
    answer += i
print(answer)
