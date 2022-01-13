'''
Created on 2021/12/02

@author: kentoo
'''
def Y (X):
    cnt = 0
    for i in range(1,X+1):
        if X % i == 0:
            cnt += 1
    return cnt
            
N = int(input())

ans = 0
for i in range(1,N+1,2):
    if Y(i) == 8:
        ans += 1
print(ans)
