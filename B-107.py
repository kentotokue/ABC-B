'''
Created on 2021/11/29

@author: kentoo
'''
'''
H,W = map(int,input().split())
#A = [list(map(str,input().split()))for i in range(H)]
A = [input() for i in range(H)]
I = []
for i in range(H):
    if A[i] == "...." or A[i] == "####":
        I.append(i)
I2 = []
print("------")
for i in range(W):
    C = ""
    for j in range(H):
        C += A[j][i]
    if C == "...." or C == "####":

        I2.append(i)
ans = []
for i in range(H):
    K = ""
    for i in range(W):
        if 
'''
h, w = map(int, input().split())
a = [''] * h
for i in range(h):
    a[i] = input()
 
row = [False] * h
col = [False] * w
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            row[i] = True
            col[j] = True
print(row)
print(col) 
for i in range(h):
    if row[i]:
        for j in range(w):
            if col[j]:
                print(a[i][j], end = '')
        print()