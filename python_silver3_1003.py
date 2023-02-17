import sys

# def fibonacci(num):
#   global cnt_zero
#   global cnt_one
#   if num == 0:
#       cnt_zero += 1
#       return`
#   elif num == 1:
#     cnt_one += 1
#     return
#   elif num == 2:
#     cnt_zero += 1
#     cnt_one += 1
#     return
#   elif num == 3:
#     cnt_zero += 1
#     cnt_one += 2
#     return
#   elif num == 4:
#     cnt_zero += 2
#     cnt_one += 3
#     return
    
#   else:
#     fibonacci(num-1)
#     fibonacci(num-2)
#     return

for _ in range(int(sys.stdin.readline())):
  num = int(sys.stdin.readline())
  list = [1,0]
  for _ in range(0,num):
    tmp = list[1]
    list[1] = sum(list)
    list[0] = tmp
  print(list[0], list[1])
  
    