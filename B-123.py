'''
Created on 2021/09/06

@author: kentoo
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

T = [A,B,C,D,E]
NT = [0]*5
for i in range(5):
    if T[i]%10==0:
        NT[i]=T[i]
    else:
        NT[i]=T[i]-T[i]%10+10

BS = 1001001001
for i in range(5):
    sum = 0
    for j in range(5):
        if i==j:
            sum +=T[j]
        else:
            sum +=NT[j]
    BS = min(BS,sum)
    

print(BS)