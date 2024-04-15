N=input()
for i in range(len(N)):
    print(N[i],end="")
    if i%3==2 and i!=len(N)-1:
        print(end=",")
    else:
        print(end="")