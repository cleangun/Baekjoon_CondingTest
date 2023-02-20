import sys

# function
def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2
  # print(f"mid = {mid}")
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
    else:  # 두 단어의 길이가 같은 경우
      if low_arr[l] == high_arr[h]:  # 같은 단어일 경우
        merged_arr.append(low_arr[l])
        l += 1
        h += 1
      else:  # 다른 단어일 경우
        if low_arr[l] < high_arr[h]:  #  low_arr이 사전순으로 앞 일 경우
          merged_arr.append(low_arr[l])
          l += 1
        else: # low_arr이 사전순으로 뒤 일 경우
          merged_arr.append(high_arr[h])
          h += 1

  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  return merged_arr
          
        


# --- main ---

line = int(sys.stdin.readline())
arr = []

for _ in range(line):
  arr.append(sys.stdin.readline().rstrip())

for i in merge_sort(arr):
  print(i)