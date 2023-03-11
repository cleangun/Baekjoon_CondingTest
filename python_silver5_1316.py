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
    if ch == before:
      continue
    elif ch in nogroup:
      isNo = 1
      break
    else:  # 현재 단어가 전의 단어와 다르지만 나온적 없는 단어일때
      nogroup.add(before)
    before = ch
  cnt += 0 if isNo == 1 else 1
  
print(cnt)