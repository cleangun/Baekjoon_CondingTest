import sys
input = sys.stdin.readline


N, K = map(int,input().rstrip().split())

lis = [ [i] for i in range(1,K+1) ]
print(lis)