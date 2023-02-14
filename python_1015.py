a_size = int(input())

array = list(map(int,input().split()))
sorted_list = []

# 원위치 값
result = [i for i in array]

# 값 정렬 후
array.sort()

for i in range(a_size):
  sorted_list.append([array[i], i])


for mat in result:
  for i in range(len(sorted_list)):
    if sorted_list[i][0] == mat:
      print(sorted_list[i][1],end=' ')
      del(sorted_list[i])
      break
  
