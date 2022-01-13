'''
Created on 2021/07/24

@author: kentoo
'''
N=int(input())

A=[0]*(N+1)
sum=0
for i in range(1,N+1):
    if i%3==0 and i%5==0:
        A[i]="FizzBuzz"
    elif i%3==0:
        A[i]="Fizz"
    elif i%5==0:
        A[i]="Buzz"
    else:
        A[i]=i

for i in A:
    if i=="FizzBuzz" or i=="Fizz" or i=="Buzz":
        continue 
    else:
        sum+=int(i) 

print(sum)