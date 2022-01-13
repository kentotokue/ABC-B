'''
Created on 2021/11/28

@author: kentoo
'''
N = int(input())

flag = True 
W = str(input())

WE = W[-1]
WC = {W:1}
for i in range(1,N):
    W = str(input())
    if WE != W[0] :
        flag = False
    if W in WC:
        WC[W] += 1
    else:
        WC[W] = 1 
    WE = W[-1]

#print(WC)
for i in WC.values():
    if i >= 2:
        print("No")
        exit()
if flag:
    print("Yes")
else:
    print("No")
        