price, count, pay = map(int,input().split())
result = (price*count) - pay
print(result if result >= 0 else 0)