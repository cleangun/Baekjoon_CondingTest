p, q = map(int, input().split())
measureList = []
for i in range(1, p+1):
  if p % i == 0:
    measureList.append(i)
if not len(measureList) <= q-1:
  print(measureList[q-1])
else:
  print(0)
