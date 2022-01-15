'''
Created on 2022/01/15

@author: kentoo
'''
N = int(input())
S = [list(map(int,input().split())) for i in range(N)]

sum = 0

for i in range(N):
    sum += (S[i][1]+1)-S[i][0]

print(sum)
