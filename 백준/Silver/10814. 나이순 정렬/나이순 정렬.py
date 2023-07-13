import sys
input = sys.stdin.readline

n = int(input())

userlst = []
for i in range(n):
    age,name = map(str,input().rstrip().split())
    userlst.append([age,i,name])

sorted_userlst = sorted(userlst, key=lambda x: (int(x[0]), x[1]))

for element in sorted_userlst:
    print(element[0],end=" "); print(element[2])