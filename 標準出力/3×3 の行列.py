N = input().split()

for i in range(len(N)):
    print(N[i], end="")
    if i % 3 == 2:#iが3の倍数から1つ前の数である場合 0 1 2で改行
        print()
    else:
        print(" ", end="")
        
#2回目
N=input().split()
for i in range(len(N)):
    if i%3==2:
        print()
    else:
        print(" ",end="")
    print(N[i],end="")