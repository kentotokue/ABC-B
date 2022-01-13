'''
Created on 2021/12/19

@author: kentoo
'''
N = int(input())

SD = {}
for i in range(N):
    S = str(input())

    if S in SD:
        SD[S] += 1
    else:
        SD[S] = 1
M = int(input())

TD = {}
for i in range(M):
    T = str(input())

    if T in TD:
        TD[T] += 1
    else:
        TD[T] = 1
cnt = 0
for i in SD.keys():
    if i in TD:
        sum = SD[i] - TD[i]
    else:
        sum = SD[i] 
    cnt = max(cnt,sum)
print(cnt)
