N=input()
for i in range(1,len(N)+1):
    for j in range(len(N)):
        if j==len(N):
            print(i*j,end="\n")
        else:
            print(i*j,end=" ")

#解答
N = int(input()) #input()はstr型なのでint型に変換

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == N:
            print(i * j)
        else:
            print(i * j, end=" ")