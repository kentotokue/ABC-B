'''
Created on 2021/12/25

@author: kentoo
'''
A,B = map(int,input().split())
S = str(input())

if len(S) != (A+B+1):
    print("No")
    exit()
for i in range(len(S)):
    
    if i == A:
        if S[A] != "-":
            print("No")
            exit()
    elif  S[i] == "0" or S[i] == "1" or S[i] == "2" or S[i] == "3" or S[i] == "4" or S[i] == "5" or S[i] == "6" or S[i] == "7" or S[i] == "8" or S[i] == "9":
        continue
    else:
        print("No")
        exit()
print("Yes")

        