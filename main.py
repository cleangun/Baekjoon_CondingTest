import sys

input = sys.stdin.readline

n, l = map(int, input().split())

# https://hooongs.tistory.com/334
# => N = (x+1) + (x+2) + (x+3) + ... + (x+L)
# => N = Lx + L(L+1)/2
# => Lx = N - (L * (L+1) / 2)

for i in range(l, 101):
  x = n - (i * (i + 1) / 2)

  if x % i == 0:
    x = int(x / i)

    if x >= -1:  # x+1, x+2 이렇게 가니까 0부터 나와야하니까 -1보다 크거                   # 나 같아야함
      for j in range(1, i + 1):
        print(x + j, end=" ")
      print()
      break
else:
  print(-1)
