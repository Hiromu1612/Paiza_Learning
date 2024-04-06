N,A,B=map(int,input().split())
for i in range(N):
    if i==N-1:
        print("({}, {})".format(A,B)) #空白を入れる
    else:
        print("({}, {})".format(A,B),end=", ")

#解答
values = input().split()
N = int(values[0])
A = int(values[1])
B = int(values[2])

for i in range(N):
    if i < N - 1:
        print("({}, {})".format(A, B), end=", ")
    else:
        print("({}, {})".format(A, B))