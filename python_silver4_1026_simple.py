import sys

# 함수 - visited에는 인덱스 번호를 담는다

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for _ in range(N):
  # print("before")
  # print(f"A = {A}")
  # print(f"B = {B}")

  tmp_A = min(A)
  tmp_B = max(B)
  A.pop(A.index(tmp_A))
  B.pop(B.index(tmp_B))
  sum += tmp_A * tmp_B

  # print("after")
  # print(f"A = {A}")
  # print(f"B = {B}")

print(sum)
