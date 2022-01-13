'''
Created on 2021/06/18

@author: kentoo
'''
S=str(input())

flag=True

for i in range(len(S)):
    if i%2==0:
        if S[i]==S[i].upper():
            flag=False
            break
            
        
    else:
        if S[i]==S[i].lower():
            flag=False
            break
if flag:
    print("Yes")
else:
    print("No")