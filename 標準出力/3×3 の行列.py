N=input().split()
for i in N:
    print(i,end=" ")
    if i%3==2:
        print("",end="\n")
print()


#解答
N=input().split()
for i in range(len(N)): #lenはlistの要素数
    if i%3==2:
        print()#改行
    else:
        print(" ",end="")
    print(N[i],end="")
