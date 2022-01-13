'''
Created on 2021/08/21

@author: kentoo
'''
N=int(input())

cnt=0
sum=1

for i in range(100):
    sum*=2
    cnt+=1
    if sum>N:
        print(cnt-1)
        exit()
print(cnt)
    