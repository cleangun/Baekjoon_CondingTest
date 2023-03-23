# # baekjoon 1980 - 햄버거사랑

result = []
n, m, t = map(int,input().split())

if t < n and t < m:
  print(f"0 {t}")
  exit(0)   # 추가된 부분

for coffee in range(0,t):
  pas = False
  target = t - coffee
  for tow in range(target//n,-1,-1):
    bul = (target - (tow*n)) // m
    if ((bul*m)+(tow*n)) == target:
      result.append(((bul+tow),coffee))
      pas = True
  if pas == True:
    break
result.sort()
cnt,cof = result.pop(-1)
print(cnt,end=" "); print(cof)