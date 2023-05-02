import sys
input = sys.stdin.readline

h, w = map(int,input().split()) # h = height(세로크기) / w = width(가로크기)
castle = []
result = 0
width = [0]*w
for _ in range(h):
    line = [ ch for ch in input().rstrip()]
    if 'X' in line:
        for idx in range(w):
            if (line[idx] == 'X') and (width[idx] == 0):
                width[idx] = 1
    castle.append(line)

for line in castle:
    if not ('X' in line):
        result += 1
        if width.count(1) == w:
            continue
        if 0 in width:
            idx = width.index(0)
            width[idx] = 1
            line[idx] = 'X'
result += width.count(0)
print(result)