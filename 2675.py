count = int(input())

for i in range(count):
  temp_list = list(input().split())
  string_list = list(temp_list[1])
  loop = int(temp_list[0])
  temp_list.clear()
  for j in range(len(string_list)):
    for m in range(loop):
      temp_list.append(string_list[j])
      print(f"{string_list[j]}", end="")
      if (j == len(string_list) - 1 and m == loop - 1):
        print(f"{string_list[j]}")