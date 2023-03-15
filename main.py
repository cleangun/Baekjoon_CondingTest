# baekjoon silver4 1018 - 체스판 다시 칠하기
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ground = []
for _ in range(n):
  ground.append(input().rstrip())

result = []
for y in range(n - 7):
  for x in range(m - 7):
    draw1 = 0
    draw2 = 0
    for c in range(y, y + 8):
      for r in range(x, x + 8):
        if (c + r) % 2 == 0:  # 두 합이 짝수일때
          if ground[c][r] == 'B':
            draw1 += 1
          if ground[c][r] == 'W':
            draw2 += 1
        else:
          if ground[c][r] == 'W':
            draw1 += 1
          if ground[c][r] == 'B':
            draw2 += 1
    result.append(min(draw1, draw2))

print(min(result))
# 코드 설명
# 체스특징 : 2번째 마다 + 대각선마다 자기와 같은 색이 나와야함
# => 다시 칠해야 하는 인덱스인 경우, 옆 ( 좌 우 위 하 )의 색이 자기와 다르게 되면
# => 그 두개는 다른게 나오는게 맞으니까 -> 정사각형으로 같이 묶어서 수정할 수 없음
# => 즉 draw +1이 안되면 더 큰 정사각형으로 묶는 다는 말이됨
# => (c+r)%2 이라는 식을 사용한 이유 -> 다다음인덱스와 , 해당인덱스의 대각선방향의
# => 인덱스를 조회할 수 있게 됨
