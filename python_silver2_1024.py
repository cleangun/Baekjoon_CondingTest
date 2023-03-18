# 수열의 합 - silver2 baekjoon
# => 시간을 빨리하기 위해, (투 포인터 알고리즘 사용)
import sys

input = sys.stdin.readline


#function
def get_sequence(start_num, target_num):
  li = [start_num]
  while sum(li) < target_num:
    most_num = li[-1]
    li.append(most_num + 1)
  return li


def binary_search(node, left, right, final_li):
  if (right < left) or (left > right):
    return final_li
  mid = (right + left) // 2

  func_result = get_sequence(mid, n)
  if (sum(func_result) == n) and (len(func_result) >= l):
    if len(final_li) == 0:
      final_li = func_result
    elif len(func_result) < len(final_li):
      final_li = func_result
  # 오른쪽 탐색
  temp = binary_search(node, mid + 1, right, final_li)
  if final_li != temp:
    final_li = temp
  # 왼쪽 탐색
  else:
    final_li = binary_search(node, left, mid - 1, final_li)

  return final_li


n, l = map(int, input().split())

node = list([i for i in range(0, n + 1)])
result = binary_search(node, 0, n // l, [])
if len(result) == 0:
  print(-1)
else:
  for i in result:
    print(i, end=" ")
