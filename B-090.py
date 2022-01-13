'''
Created on 2021/12/19

@author: kentoo
'''
A,B = map(int,input().split())



#S = ''.join(list(reversed(S)))
cnt = 0
for i in range(A,B+1):
    N = str(i)
    if N == N[::-1]:
        cnt += 1
        #print(i)
print(cnt)
        