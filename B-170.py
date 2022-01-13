'''
Created on 2021/07/17

@author: kentoo
'''
X,Y=map(int,input().split())

flag=False

for i in range(X+1):
    j=X-i 
    if i*4+j*2==Y:
        flag=True
if flag:
    print("Yes")
else:
    print("No")