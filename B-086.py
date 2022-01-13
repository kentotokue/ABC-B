'''
Created on 2021/12/22

@author: kentoo
'''
A,B = map(str,input().split())
sum = int(A+B)

for i in range(1,100001):
    if i*i == sum:
        print("Yes")
        exit()
print("No")