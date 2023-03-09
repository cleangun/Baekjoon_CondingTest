arr = set()
for i in range(1,10000):
  sum = i
  temp = str(i)
  for idx in temp:
    sum += int(idx)
  arr.update([sum])

for i in range(1,10000):
  if i in arr:
    continue
  else:
    print(i)