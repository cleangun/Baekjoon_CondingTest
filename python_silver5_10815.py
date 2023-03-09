# silver5 숫자카드 - 10815

import sys
input = sys.stdin.readline

input()
slist = set(map(int,input().split()))

input()
chklist = map(int,input().split())
for i in chklist:
  if i in slist:
    print(1,end=" ")
    slist.remove(i)
  else:
    print(0,end=" ")

# set자료형을 사용했을 경우의 코드이다
# list를 사용했을 경우
# => 시간복잡도는 O(NM)의 시간복잡도를 가지지만
# set 자료형을 사용하면
# => O(1)의 시간복잡도를 가지게 된다 => 전체시간복잡도는 O(N+M)이 된다.