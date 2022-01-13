'''
Created on 2021/12/25

@author: kentoo
'''
import itertools
s = str(input())
t = str(input())

S = []
T = []

for i in range(len(s)):
    S.append(s[i])
for i in range(len(t)):
    T.append(t[i])
S.sort()
T.sort(reverse = True)
SA = ""
TA = ""
for i in S:
    SA += i
for i in T:
    TA += i 

if SA < TA :
    print("Yes")
else:
    print("No")
    

'''
SL = []
TL = []
for p  in itertools.permutations(s):
    L = len(p)
    sum = ""
    for i in range(L):
        sum += p[i]
    SL.append(sum)
for p  in itertools.permutations(t):
    L = len(p)
    sum = ""
    for i in range(L):
        sum += p[i]
    TL.append(sum)
SL.sort()
TL.sort()

for i in SL:
    for j in TL :
        if i < j:
            print("Yes")
            exit()
print("No")
'''