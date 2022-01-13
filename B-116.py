S = int(input())

A = [S]
ans = {S:1}

for i in range(1,10**6):
    if A[i-1] % 2 == 0:
        A.append(A[i-1]//2)
        if A[i-1]//2 in ans:
            print(i+1)

            exit()
        else:
            ans[A[i-1]//2] = 1
    else:
        A.append(A[i-1]*3+1)
        if A[i-1]*3+1 in ans:
            print(i+1)

            exit()
        else:
            ans[A[i-1]*3+1] = 1
