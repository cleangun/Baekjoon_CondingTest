num = int(input())
divisor = 2
while num > 1:
  if num % divisor == 0:
    print(divisor)
    num /= divisor
  else:
    divisor += 1