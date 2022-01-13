'''
Created on 2021/10/02

@author: kentoo
'''
S = str(input())
T = str(input())

cnt = 0
if S == T :
    print("Yes")
    exit()

c = 0   
for i in range(len(S)-1):
    if S[i] == T[i]:
        c += 1
    else:
        if S[i] == T[i+1] and T[i] == S[i+1]:
            cnt += 1 
if len(S)==2 and cnt == 1:
    print("Yes")
    exit()
    
if cnt ==1 and c >=1:
    print("Yes")
else:
    print("No")