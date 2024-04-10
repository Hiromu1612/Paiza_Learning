a=[]
N=int(input())
for i in range(1,N+1):
    a.append(i)
    print(*a) #*をつけるとリストの中身をそのまま出力できる(アンパック)

#解答
N = int(input())

for i in range(1, N + 1):
    for j in range(1, i + 1): #1 行目の出力する個数は 1 つ、2 行目の出力する個数は 2 つですね。さらに、i 行目の出力する個数は i 個
        if j == i:
            print(j)
        else:
            print(j, end=" ")