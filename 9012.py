import sys

line = int(input())

def chk_correct(str):
  stack = []
  for i in str:
    if i == ')':
      if len(stack) != 0:
        node = stack.pop()
        if node == '(':
          continue
        else:
          return "NO"
      else:
        return "NO"    
      
    elif i == ']':
      if len(stack) != 0:
        node = stack.pop()
        if node == '[':
          continue
        else:
          return "NO"
      else:
        return "NO"
    else:
      stack.append(i)
  if len(stack) == 0:
    return 'YES'
  else:
    return 'NO'


for _ in range(line):
  str = sys.stdin.readline().rstrip()
  print(chk_correct(str))