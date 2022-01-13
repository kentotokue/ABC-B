'''
Created on 2021/08/02

@author: kentoo
'''

S=str(input())
D=S[::-1]


cnt=0


for i in range(len(S)//2):
    if S[i]==D[i]:
        continue
    else:
        cnt+=1 

print(cnt)
