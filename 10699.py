hour, minute = map(int,input().split())
ovendelay = int(input())

totaltime = minute + ovendelay
print(totaltime / 60 , totaltime%60)
