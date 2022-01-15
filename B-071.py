'''
Created on 2022/01/15

@author: kentoo
'''
S = set(input())
S = list(set("abcdefghijklmnopqrstuvwxyz") - S)
if len(S) == 0:
    print(None)
    exit()
S.sort()
print(S[0])
'''
S = str(input())
#97 - 122

for i in range(97,123):
    cnt = 0
    for j in range(len(S)):
        
        if chr(i) == S[j]:
            
            break
        else:
            cnt += 1
    if cnt == len(S):
        print(chr(i))
        exit()
    



print("None")
'''