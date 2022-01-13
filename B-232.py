'''
Created on 2021/12/19

@author: kentoo
'''
S = str(input())
T = str(input())

A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
     "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

ans = []
'''
for i in range(len(S)):
    N = A.index(S[i])
    cnt = 0
    for j in range(N,60):
        #print(T[i],A[j])
        
        if T[i] == A[j]:
            
            break
        cnt += 1
    ans.append(cnt)
#print(ans)
ans = len(sorted(set(ans)))

    
if ans == 1:
    print("Yes")
else:
    print("No")
'''
for i in range(len(S)):
    K = (ord(T[i]) - ord(S[i])+26)%26
    ans.append(K)
ans = len(sorted(set(ans)))
if ans == 1:
    print("Yes")
else:
    print("No")