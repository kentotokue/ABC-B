'''
Created on 2021/08/14

@author: kentoo
'''
S=str(input())

for i in range(len(S)):
    if i%2==0:
        if S[i]=="R" or S[i]=="U" or S[i]=="D":
            continue
        else:
            print("No")
            exit()
    else:
        if S[i]=="L" or S[i]=="U" or S[i]=="D":
            continue
        else:
            print("No")
            exit()
print("Yes")