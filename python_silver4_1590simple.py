n, t = map(int, input().split())
result = []
for _ in range(n):
  s, i, c = map(int, input().split())
  li = [s + i * j for j in range(c)]
  if li[-1] < t:
    continue
  ss, e = 0, c - 1
  a = 0
  while ss <= e:
    m = (ss + e) // 2
    if li[m] >= t:
      a = m
      e = m - 1
    else:
      ss = m + 1
  result.append(li[a] - t)
print(min(result) if result else -1)