# baekjoon 1316 - 그룹 단어 체크
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
  nogroup = set()
  isNo = 0
  word = input().rstrip()

  if len(word) == 1:  # 단어 한 개
    cnt += 1
    continue
    
  before = word[0]
  for ch in word[1:]:
    if ch not in nogroup:
      nogroup.add(before)
    elif ch != before:
      isNo = 1
      break
    before = ch
  if isNo != 1:
    cnt += 1
print(cnt)