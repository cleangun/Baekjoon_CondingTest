import sys


# 함수 - visited에는 인덱스 번호를 담는다
def dfs(Aarr, Barr, A_visit, B_visit, lv, sum, min):
  if sum > min:
    return min

  if lv == len(Aarr):
    if sum <= min:
      min = sum
    return min

  for bidx in range(len(Barr)):
    if bidx in B_visit:  # B 인덱스 방문 했대요
      continue

    B_visit.append(bidx)
    for aidx in range(len(Aarr)):
      if aidx in A_visit:  # B인덱스는 해당 A인덱스를 접근 불가(이미 접근됨)
        continue

      A_visit.append(aidx)
      tmp = sum + (Barr[bidx] * Aarr[aidx])
      min = dfs(Aarr, Barr, A_visit, B_visit, lv + 1, tmp, min)
      A_visit.pop()
    B_visit.pop()

  return min


N = int(sys.stdin.readline())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(f"A = {A}")
print(f"B = {B}")

print(dfs(A, B, [], [], 0, 0, 1e9))
