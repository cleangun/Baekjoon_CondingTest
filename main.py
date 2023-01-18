H, M, S = map(int, input().split())
D = int(input())

S += D % 60
D = D // 60
if S >= 60:
  M += 1
  S -= 60

M += D % 60
D = D // 60
if M >= 60:
  H += 1
  M -= 60

H += D % 24
if H >= 24:
  H -= 24

print(H, M, S)



h,m,s = map(int,input().split(" "))
sec = int(input())

s1 = (s+sec)%60
m1 = (s+sec)//60
m2 = (m+m1)%60
h1 = (m+m1)//60
h2 = (h+h1)%24

print(h2,m2,s1)