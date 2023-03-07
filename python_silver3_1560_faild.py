import sys

input = sys.stdin.readline

# function
def marking(arr,x,y,N):
  ori = [x,y]
  if arr[y][x] == 0:
    return arr
  while (x < (N-1)) and (y < (N-1)):
    x += 1
    y += 1
    arr[y][x] = 0
  x,y = ori
  while x > 0 and y < (N - 1):
    x -= 1
    y += 1
    arr[y][x] = 0
  return arr

# Main
N = int(input())

grd = list([[1]*N for i in range(N)])

for y in range(len(grd)):
  for x in range(len(grd[y])):
    grd = marking(grd,x,y,N)

cnt = 0
for i in grd:
  print(i)
  cnt += i.count(1)

print(cnt)
