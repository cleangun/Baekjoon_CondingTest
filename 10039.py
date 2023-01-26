sum = 0
for i in range(5):
  x = int(input())
  sum += x if x > 40 else 40

print(int(sum/5))