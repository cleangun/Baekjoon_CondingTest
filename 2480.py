rollingCount = list(map(int, input().split()))
max = rollingCount[0]
same = 0
count = 1

for i in range(len(rollingCount) - 1):
  for j in range(i+1,len(rollingCount)):
    if rollingCount[i] == rollingCount[j]:
      count += 1
      same = rollingCount[i]
    elif rollingCount[j] > max:
      max = rollingCount[j]

if count <= 1:
  print(max * 100)
elif count == 2:
  print(1000 + (same * 100))
elif count >= 3:
  print(10000 + (same * 1000))