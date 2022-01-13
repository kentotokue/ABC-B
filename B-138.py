'''
Created on 2021/08/14

@author: kentoo
'''

N=int(input())
A=list(map(int,input().split()))
sum=0

for i in A:
    sum+=1/i 
print(1/sum)