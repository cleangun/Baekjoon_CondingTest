from collections import deque, defaultdict

def bfs(k, num):
  visited = [0]*(len(video.keys()) + 1)
  cnt = 0
  q = deque()
  q.append(num)
  visited[num] = 1

  while q:
    n = q.popleft()
    for v in video[n]:
      if not visited[v[0]] and v[1] >= k:
        visited[v[0]] = 1
        cnt += 1
        q.append(v[0])

  return cnt

N, Q = map(int, input().split())
video = defaultdict(list)
for _ in range(N -  1):
  a , b, r = map(int, input().split())
  video[a].append([b,r])
  video[b].append([a,r])

for _ in range(Q):
  k , v = map(int, input().split())
  print(bfs(k , v))