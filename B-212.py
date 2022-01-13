'''
Created on 2021/07/31

@author: kentoo
'''

S=str(input())
'''
if S[0]==S[1] and S[1]==S[2] and S[2]==S[3] :
    print("Weak")
    exit()


if (int(S[0])+int(S[3]))%10==(int(S[1])+int(S[2]))%10 and (int(S[1])+1)%10==(int(S[2]))%10:
    print("Weak")
    exit()


print("Strong")
'''
cnt1=0  
cnt2=0      
for i in range(3):
    if S[i]==S[i+1]:
        cnt2+=1
    if (int(S[i])+1)%10==(int(S[i+1]))%10:
        
        cnt1+=1

if cnt2==3 or cnt1==3:
    print("Weak")
else:
    print("Strong")
        
    