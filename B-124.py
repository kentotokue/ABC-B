'''
Created on 2021/09/06

@author: kentoo
'''

N = int(input())
H = list(map(int,input().split()))

cnt = 1
MH = H[0]
for i in range(1,N):
    if MH<=H[i]:
        MH = H[i]
        cnt+=1

print(cnt)