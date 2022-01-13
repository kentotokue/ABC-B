'''
Created on 2021/07/26

@author: kentoo
'''
S=str(input())
N=len(S)

S1=S[0:N//2]
S2=S[N-1:-(N//2+1):-1]



S3=S1[0:len(S1)//2]
S4=S1[len(S1)-1:-(len(S1)//2+1):-1]



if S1==S2 and S3==S4:
    print("Yes")
else:
    print("No")
