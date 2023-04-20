N, K = map(int, input().split())

purchased_water_bottle_cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    print(f"bin(N)[::-1] = {bin(N)[::-1]}")
    print(f"idx = {idx}")
    print(f"purchased_water_bottle_cnt : {purchased_water_bottle_cnt}")
    purchased_water_bottle_cnt += 2**idx
    print(f"purchased_water_bottle_cnt : {purchased_water_bottle_cnt}")
    N += 2**idx

print(purchased_water_bottle_cnt)
