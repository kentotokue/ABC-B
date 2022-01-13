'''
Created on 2021/12/03

@author: kentoo
'''
S = str(input())
T = str(input())
N = len(S)

A = S + S 
for i in range(N):
    if A[i:i+N] == T:
        print("Yes")
        exit()
print("No")

        