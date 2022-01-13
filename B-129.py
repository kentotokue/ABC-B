'''
Created on 2021/08/21

@author: kentoo
'''
N=int(input())
W=list(map(int,input().split()))

sum1=0
sum2=0
ans=1001001001
for i in range(N-1):
    sum1=sum(W[:i+1])
    sum2=sum(W[i+1:])
    #print(W[:i+1],W[i+1:])
    ans=min(abs(sum1-sum2),ans)
    
print(ans)
        
        