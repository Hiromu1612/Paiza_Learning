n=list(map(int,input().split()))
for i in n:
    if i % 3 == 2:
        print(n[i])
    else:
        print(n[i], end=" ")#OK


#解答
N=input().split()
for i in range(len(N)): #lenはlistの要素数
    if i%3==2:
        print()#改行
    else:
        print(" ",end="")
    print(N[i],end="")