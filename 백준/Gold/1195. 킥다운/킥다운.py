import sys
input = sys.stdin.readline

gear1 = [ int(digit) for digit in input().rstrip() ]
gear2 = [ int(digit) for digit in input().rstrip() ]

def find_short_row(short_arr, long_arr):
    fit_length = set()
    max_gear_len = len(long_arr)
    min_gear_len = len(short_arr)
    ground = [0] * (max_gear_len * 3)
    ground[max_gear_len:max_gear_len*2] = long_arr.copy()
    
    for start_idx in range(max_gear_len, (max_gear_len*2) - min_gear_len + 1):
        out = [x+y for x,y in zip(ground[start_idx:],short_arr)]    # start_idx+min_gear_len
        # check is it fit
        if out.count(4) == 0:
            fit_length.add(max_gear_len)
    # if not fit with above
    if len(fit_length) <= 0:
        for distance in range(min_gear_len, 0,-1):
            out1 = [x+y for x,y in zip(ground[(max_gear_len-distance):], short_arr)]
            out2 = [x+y for x,y in zip(ground[(max_gear_len*2 - (min_gear_len-distance)):],short_arr )]
            if (out1.count(4) == 0) or (out2.count(4) == 0):
                fit_length.add(max_gear_len+distance)
    return min(fit_length)

res = 0
if len(gear1) >= len(gear2):    # gear1이 더 긴 기어인 경우
    res = find_short_row(gear2, gear1)
else:                           # gear2가 더 긴 깅인 경우
    res = find_short_row(gear1,gear2)
print(res)