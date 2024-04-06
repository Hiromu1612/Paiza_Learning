N = int(input())

M = [0] * N #長さNのリストの要素を0で初期化
values = input().split()
for i in range(N):
    M[i] = int(values[i]) #Mの要素は2なら1,2 5なら1,2,3,4,5を出力

for i in range(N):
    for j in range(1, M[i] + 1):
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")