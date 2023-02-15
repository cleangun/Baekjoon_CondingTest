N = int(input())

A = list(map(int,input().split()))
P = list.copy(A)

print(f"P = {P}")
print(f"A = {A}")
print("----------")

for i in range(N):
  P[A.index(min(A))] = i
  A[A.index(min(A))] = max(A) + 1

  print(f"index = {i}")
  print(f"P = {P}")
  print(f"A = {A}")
  
print(*P)
