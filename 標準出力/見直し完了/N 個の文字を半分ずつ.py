N=int(input())
M=N/2
for i in range(1,N+1):
    if i==M:
        print(i)
    else:
        print(i,end=" ")

#解答
N = int(input())

for i in range(1, N + 1):
    if i % (N // 2) == 0: #2で割った商(整数部分)が出力される
        print(i)
    else:
        print(i, end=" ")
