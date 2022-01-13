'''
Created on 2021/12/03

@author: kentoo
'''
S = str(input())
L = len(S)

if S[0] != "A":
    print("WA")
    exit()
#print("1")
cnt = 0 
if 2 == L-2 :
    if S[2] != "C":
        print("WA")
        exit()
    else:
        cnt = 1
else:
    for i in range(2,L-1):
        if S[i] == "C":
            cnt += 1
#print("2")
if cnt != 1:
    print("WA")
    exit()
#print("3")
for i in range(L):
    if S[i] == "A" or S[i] == "C":
        continue
    else:
        if S[i].isupper():
            print("WA")
            exit()
#print("4")
print("AC")
    