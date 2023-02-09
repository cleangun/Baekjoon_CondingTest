A, B = map(int, input().split())
list = []
for i in range(1, 1000):
  if i > B:
    break
  for num in range(i):
    list.append(i)
list.insert(0, 0)

for index in range(A, B + 1):
  list[0] += list[index]
print(list[0])
