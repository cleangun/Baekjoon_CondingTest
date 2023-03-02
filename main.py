import sys

input = sys.stdin.readline


def intCount(str):
  s = 0
  for arg in str:
    if arg.isdigit():
      s += int(arg)
  return s


def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2
  low_arr = merge_sort(arr[:mid])
  high_arr = merge_sort(arr[mid:])

  merged_arr = []
  l = h = 0

  while l < len(low_arr) and h < len(high_arr):
    if len(low_arr[l]) < len(high_arr[h]):
      merged_arr.append(low_arr[l])
      l += 1
    elif len(low_arr[l]) > len(high_arr[h]):
      merged_arr.append(high_arr[h])
      h += 1
    else:
      if intCount(low_arr[l]) < intCount(high_arr[h]):
        merged_arr.append(low_arr[l])
        l += 1
      elif intCount(low_arr[l]) > intCount(high_arr[h]):
        merged_arr.append(high_arr[h])
        h += 1
      else:
        if low_arr[l] < high_arr[h]:
          merged_arr.append(low_arr[l])
          l += 1
        else:
          merged_arr.append(high_arr[h])
          h += 1
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  return merged_arr


N = int(input())

sn = []
for _ in range(N):
  sn.append(input().rstrip())

for arg in merge_sort(sn):
  print(arg)
