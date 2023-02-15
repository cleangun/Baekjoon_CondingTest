N = int(input())

data = list(map(int, input().split()))
op = list(map(int,input().split()))

max_value = -1e9
min_value = 1e9

# print(max_value)
# print(min_value)

def solution(num, idx, add, sub, mul, div):

  global max_value, min_value
  
  if idx == N:
    max_value = max(max_value, num)
    min_value = min(min_value, num)
    return

  if add > 0:
    solution(num + data[idx], idx + 1, add - 1, sub, mul, div)
  if sub > 0:
    solution(num - data[idx], idx + 1, add, sub - 1, mul, div)
  if mul > 0:
    solution(num * data[idx], idx + 1, add, sub, mul - 1, div)
  if div > 0:
    # print(f"num // data[{idx}] = {num // data[idx]}")
    # print(f"int(num // data[{idx}]) = {int(num / data[idx])}")
    solution(int(num / data[idx]), idx + 1, add, sub, mul, div - 1)
    


solution(data[0], 1, op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)