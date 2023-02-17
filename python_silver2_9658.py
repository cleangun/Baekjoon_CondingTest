# 첫 번째 점화식 쌓기
N = int(input())
arr = [0 for _ in range(1001)]
arr[1] = 'CY'
arr[2] = 'SK'
arr[3] = 'CY'
arr[4] = 'SK'
arr[5] = 'SK'
arr[6] = 'SK' # 3 1 1 1
arr[7] = 'SK' # 4 1 1 1
arr[8] = 'CY' # 1 4 1 1 1

for i in range(9, N+1):
  if arr[i-1] == 'SK' and arr[i-3] == 'SK' and arr[i-4] == 'SK':
    arr[i] = 'CY'
  else:
    arr[i] = 'SK'

for i in range(1,100):
  print(arr[i])

print(arr[N])