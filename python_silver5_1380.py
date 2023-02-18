import sys

n = 1
cnt = 0
while n >= 1:
  n = int(sys.stdin.readline())
  if n >= 1:
    cnt += 1
    student = []
    stack = []
    for _ in range(n): # 학생들 이름 받기
      student.append(sys.stdin.readline().rstrip())
    for _ in range((2*n) - 1):
      num, alpha = sys.stdin.readline().split()
      if num in stack:
        stack.remove(num)
      else:
        stack.append(num)
    print(f"{cnt} {student[int(stack.pop()) - 1]}")
  else:
    break