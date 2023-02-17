a,b,c = map(int,input().split())

dm = a%b
list = []

for _ in range(c):
  tmp = (dm*10) // b
  dm = (dm*10) % b
  list.append(tmp)

print(list)
print(list[c])
  