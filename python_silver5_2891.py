import sys

input = sys.stdin.readline

n, s, r = map(int, input().rstrip().split())

teams = [1 for i in range(n)]

# brute Force ? 그리디가 맞나;;;
for lost_idx in list(map(int, input().rstrip().split())):
  teams[lost_idx - 1] -= 1
for more_idx in list(map(int, input().rstrip().split())):
  teams[more_idx - 1] += 1
for idx in range(len(teams)):
  if teams[idx] == 0:
    if (idx != 0) and (teams[idx - 1] == 2):
      teams[idx - 1] -= 1
      teams[idx] += 1
    elif (idx != len(teams) - 1) and (teams[idx + 1] == 2):
      teams[idx] += 1
      teams[idx + 1] -= 1
print(teams.count(0))