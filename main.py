import sys

def merge_sort(array):
  if len(array) < 2:
    return list(array)
  print(len(array), end=' ')
  print(f"array : {array}")
  mid = len(array) // 2
  print(f"mid = {mid}")
  print()
  low_arr = merge_sort(array[:mid])
  high_arr = merge_sort(array[mid:])

  merged_arr = []

  l = h = 0
  while l < len(low_arr) and h < len(high_arr):
    if len(low_arr[l]) < len(high_arr[h]):
      merged_arr.append(low_arr[h])
      l += 1
    elif len(low_arr[l]) > len(high_arr[h]):
      merged_arr.append(high_arr[h])
      h += 1
    else:
      merged_arr.append(low_arr[h])
      merged_arr.append(high_arr[h])
      l += 1
      h += 1
      
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  print(merged_arr)
  return merged_arr

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
  stack.append(sys.stdin.readline().rstrip())

print(f"didnt merged : {stack}")
print(merge_sort(stack))