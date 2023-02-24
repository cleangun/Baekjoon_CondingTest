import sys

input = sys.stdin.readline

N, kg = map(int, input().split())

lis = []
bag = [[0] * (kg + 1) for i in range(N + 1)]

for _ in range(N):
  lis.append(list(map(int, input().split())))

for idx, (w, v) in enumerate(lis):
  print(f"idx = {idx} , w = {w} , v = {v}")
  for weight in range(1, kg + 1):
    if w <= weight:
      bag[idx + 1][weight] = max(bag[idx][weight], bag[idx][weight - w] + v)
    else:
      bag[idx + 1][weight] = bag[idx][weight]

print(lis)

print("------------------------")
for i in range(len(bag)):
  print(bag[i])

print(bag[N][kg])
