'''
Created on 2021/06/14

@author: kentoo
'''
N=int(input())
cnt=0
cnt2=0
for i in range(1,N+1):
    if (i%2==1):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==8:
            cnt2+=1

print(cnt2)
               