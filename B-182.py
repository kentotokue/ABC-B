'''
Created on 2021/06/24

@author: kentoo
'''
N = int(input())
A = list(map(int, input().split()))
 
ans = -1
mx = 0
 
for x in range(2, 1001):
    s=0
    for a in A:
        if a%x==0:
            s+=1
    if mx < s:
        mx = s
        ans = x
 
print(ans)