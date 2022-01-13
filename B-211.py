'''
Created on 2021/07/24

@author: kentoo
'''

S=[str(input()) for i in range(4)]
'''
cnt1=False
cnt2=False
cnt3=False
cnt4=False

for i in S:
    if i=="H":
        cnt1=True 
    elif i=="2B":
        cnt2=True
    elif i=="3B":
        cnt3=True
    elif i=="HR":
        cnt4=True

if cnt1 and cnt2 and cnt3 and cnt4:
    print("Yes")
else:
    print("No")
'''

S=set(S)

if len(S)==4:
    print("Yes")
else:
    print("No")