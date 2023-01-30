line = int(input())
list1 = []
# list1 = ['OOXXOXXOOO',
# 'OOXXOOXXOO',
# 'OXOXOXOXOXOXOX',
# 'OOOOOOOOOO',
# 'OOOOXOOOOXOOOOX']
for i in range(line):
  list1.append(input())

for i in range(len(list1)):
  sum = 0
  count = 0
  string_list = list(list1[i])
  for j in range(len(string_list)):
    if string_list[j] == 'O':
      count += 1
      sum += count
    elif string_list[j] == 'X':
      count = 0
  print(sum)