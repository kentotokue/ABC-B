'''
Created on 2021/12/25

@author: kentoo
'''
L,R = map(int,input().split())
S = str(input())

S1 = S[:L-1]
S2 = S[R:]
S3 = S[L-1:R]
S4 = S3[::-1]
print(S1+S4+S2)