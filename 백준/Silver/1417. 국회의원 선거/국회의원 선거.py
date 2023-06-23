import sys
input = sys.stdin.readline

vote_list = []
n = int(input())

for _ in range(n):
    vote_list.append(int(input()))

dasom = vote_list.pop(0)
if len(vote_list) == 0:
    print(0)
    exit(0)
cnt = 0
while dasom <= max(vote_list):
    dasom += 1; cnt += 1
    vote_list[vote_list.index(max(vote_list))] -= 1
print(cnt)