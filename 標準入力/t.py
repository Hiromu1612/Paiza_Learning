N,M=map(int,input().split()) 
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
for i in range(N):
    print(*a[i])