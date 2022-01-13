'''
Created on 2021/11/26

@author: kentoo
'''
N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

ans = []

for i in range(N):
    
    ans.append(abs(A-(T-(H[i]*0.006))))

A = ans.index(min(ans))
print(A+1)
