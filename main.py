import sys


def merge_sort(array):
  if len(array) < 2:
    return array
  mid = len(array) // 2

  low_arr = merge_sort(array[:mid])
  high_arr = merge_sort(array[mid:])

  print("-----------------")
  print(f"low_arr = {low_arr}")
  print(f"high_arr = {high_arr}")
  print()

  merged_arr = []

  l = h = 0
  cnt = 0
  while l < len(low_arr) and h < len(high_arr):
    cnt += 1
    print(f" while cnt = {cnt}")
    print(f" Array = {array}")
    print(f"compare index = {low_arr[l]}({len(low_arr[l])}) / {high_arr[h]}({len(high_arr[h])})")
    if len(low_arr[l]) < len(high_arr[h]):
      merged_arr.append(low_arr[h])
      print(f"....low_arr append....")
      print(f"l = {l}")
      print(f"h = {h}")
      print(f"len(high_arr) = {len(high_arr)}")
      print(f"len(low_arr) = {len(low_arr)}")
      print(f"low_Arr = {low_arr}")
      print(f"l = {l} / merged_arr = {merged_arr}")
      l += 1
      print(f"l = {l}")
      print(f"h = {h}")
      if l < len(low_arr):
        print(f"next low turn = {low_arr[l]}")
      else:
        print("next low turn is None")
      
    elif len(low_arr[l]) > len(high_arr[h]):
      merged_arr.append(high_arr[h])
      print(f"....high_arr append....")
      print(f"l = {l}")
      print(f"h = {h}")
      print(f"len(low_arr) = {len(low_arr)}")
      print(f"len(high_arr) = {len(high_arr)}")
      print(f"high_Arr = {high_arr}")
      print(f"h = {h} / merged_arr = {merged_arr}")
      h += 1
      print(f"l = {l}")
      print(f"h = {h}")
      if h < len(high_arr):
        print(f"next high turn = {high_arr[h]}")
      else:
        print("next high turn is None")
    else:
      print(f".... high low arr append ....")
      merged_arr.append(low_arr[h])
      merged_arr.append(high_arr[h])
      l += 1
      h += 1
  print("while Escape!!!")
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  print(merged_arr)
  print()
  return merged_arr


# ------------ main --------------
stack = []
n = int(sys.stdin.readline())
for _ in range(n):
  stack.append(sys.stdin.readline().rstrip())

print(f"didnt merged : {stack}")
print()
print()
print(merge_sort(stack))
