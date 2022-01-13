'''
Created on 2021/08/04

@author: kentoo
'''
N=int(input())
S=str(input())

if N%2==0:
    D=S[0:N//2]
    F=S[N//2:]
    if D==F:
        print("Yes")
    else:
        print("No")
else:
    print("No")