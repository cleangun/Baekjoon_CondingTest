import sys

input = sys.stdin.readline

N, T = map(int, input().split())

interval = []

for _ in range(N):
  interval.append(list(map(int, input().rstrip().split())))

late_cnt = 0
result = 1e9


def remain_AI(st_drive, itv, lst, target):
  while st_drive < target and lst >= 1:
    st_drive += itv
    lst -= 1
  return st_drive - target


for st_drive, itv, lst in interval:
  # 도착하자마자
  if st_drive == T:  # 도착하자마자 버스 있음
    print(0)
    exit(0)

  # 운행 후 : 해당 운행이 끝날때보다 늦게 도착 => 탈 수 없음
  if (st_drive + (itv * (lst - 1))) < T:
    late_cnt += 1
    continue

  # 운행 중
  if st_drive < T:  # 운행시간내에 도착하는데 버스 얼마나 기다려야하는지 계산
    diff = remain_AI(st_drive, itv, lst - 1, T)
    if diff < result:
      result = diff
  # 운행 전 , 운행 중
  elif st_drive > T:  # 도착이후에 시작하는 버스들이 얼마나 있는지 확인
    diff = st_drive - T
    if diff < result:
      result = diff

if late_cnt == len(interval):  # 탈 수 있는 버스가 없음
  print(-1)
  exit(0)

print(result)
