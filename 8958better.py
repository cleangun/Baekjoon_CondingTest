import sys

input = sys.stdin.readline

count = int(input().strip())

for _ in range(count):
  answer = 0

  inputData = input().strip().split('X')
  print(inputData)
  for i in inputData:
    if i != '':
      answer += (len(i) * (len(i) + 1) ) // 2

  print(answer)