'''
Created on 2022/01/23

@author: kentoo
'''

W,H,N = map(int,input().split())

R = [list(map(int,input().split()))for i in range(N)]

LX = 0
LY = 0
RX = W 
RY = H  

for i in range(N):
    if R[i][2] == 1 :
        if LX < R[i][0]:
            LX = R[i][0]

    elif R[i][2] == 2:
        if RX > R[i][0]:
            RX = R[i][0]
    elif R[i][2] == 4:
        if RY > R[i][1]:
            RY = R[i][1]

    else:
        if LY < R[i][1]:
            LY = R[i][1]



print(max(0,(RY-LY))*max(0,(RX-LX)))
'''
LU = [0,H]
LD = [0,0]
RU = [H,W]
RD = [W,0]

for i in range(N):
    if R[i][2] == 1:
        LU = [R[i][0],H]
        LD = [R[i][0],0]
    elif R[i][2] == 2:
        RU = [R[i][0],H]
        RD = [R[i][0],0]
    elif R[i][2] == 3:
        LU = [R[i][0],]
        LD = [R[i][0],0]
'''