'''
Created on 2021/08/14

@author: kentoo
'''
S,T=map(int,input().split())
cnt=0

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j+k<=S and i*j*k<=T:
                cnt+=1

print(cnt)       
    