'''
Created on 2021/08/29

@author: kentoo
'''

N=int(input())

NAME = []
for i in range(N):
    S,T=map(str,input().split())
    NAME.append([S,T])

flag = False

for i in range(N):
    for j in range(i,N):
        if i==j:
            continue
        
        if NAME[i][0]==NAME[j][0] and NAME[i][1]==NAME[j][1]:
            
            print("Yes")
            exit()
print("No")
    
