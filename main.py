p_sum = 0
max = 0
for _ in range(10):
  ppout, ppin = map(int, input().split())
  p_sum += ppin - ppout
  if p_sum > max:
    max = p_sum
print(max)