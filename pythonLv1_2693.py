line = int(input())

for _ in range(line):
  arr = list(map(int,input().split()))
  arr.sort(reverse=True)
  print(arr[2])