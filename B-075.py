'''
Created on 2022/01/14

@author: kentoo
'''
H,W = map(int,input().split())
S = [str(input())for i in range(H)]

S.insert(0,"."*(W+2))
S.append("."*(W+2))
for i in range(1,H+1):
    S[i] = "."+S[i]+"."
    
ans = []
dx = [-1,0,1]
dy = [-1,0,1]
for i in range(1,H+1):
    A = ""
    
    for j in range(1,W+1):
        cnt = 0
        
        if S[i][j] == ".":
            for k in range(3):
                for l in range(3):
                    if dx[k] == 0 and dx[l]==0:
                        continue
                    if S[i+dx[k]][j+dx[l]] == "#":
                        cnt += 1
            A += str(cnt)
        else:
            A += "#"
    ans.append(A)
                

                
        
'''
        if S[i][j] ==".":
            if S[i-1][j-1] == "#":
                cnt += 1
            if S[i-1][j] == "#":
                cnt += 1
            if S[i-1][j+1] == "#":
                cnt += 1
            if S[i][j-1] == "#":
                cnt += 1
            if S[i][j+1] == "#":
                cnt += 1
            if S[i+1][j-1] == "#":
                cnt += 1
            if S[i+1][j] == "#":
                cnt += 1
            if S[i+1][j+1] == "#":
                cnt += 1
            A += str(cnt)
            
        else:
            A += "#"
'''
    #ans.append(A)
for i in range(H):
    print(ans[i])