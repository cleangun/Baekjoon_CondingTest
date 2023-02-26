import sys

input = sys.stdin.readline

N, T = map(int, input().split())

interval = []

for _ in range(N):
  interval.append(list(map(int, input().rstrip().split())))

# print(interval)

# print(min(interval))

early_cnt = 0
late_cnt = 0
min = 1e9
result = 1e9


def remain_AI(st_drive, itv, lst, target):
  while st_drive < target and lst >= 1:
    st_drive += itv
    lst -= 1
  return st_drive - target

for st_drive, itv, lst in interval:
  if st_drive == T:
    print(0)
    exit(0)
  if st_drive > T:  # 도착이후에 시작하는 버스들이 얼마나 있는지 확인
    early_cnt += 1
    if st_drive < min:
      min = st_drive
  elif (st_drive + (itv * (lst-1))) < T:  # 해당 운행이 끝날때보다 늦게 도착
    late_cnt += 1
  elif st_drive < T:  # 운행시간내에 도착하는데 버스 얼마나 기다려야하는지 계산
    find_remain = remain_AI(st_drive, itv, lst - 1, T)
    if find_remain < result:
      result = find_remain

  
  if early_cnt == len(interval):  # 모든 운행시간이 T보다 클 경우
    # ( 모든 버스가 도착이후에 운행 시작함)
    print(min - T)
    exit(0)
  elif late_cnt == len(interval):  # 탈 수 있는 버스가 없음
    print(-1)
    exit(0)

print(result)
