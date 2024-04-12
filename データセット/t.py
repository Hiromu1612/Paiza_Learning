N,Q=map(int,input().split())
A=[int(i) for i in input().split()]
for _ in range(Q):
    s=[int(i) for i in input().split()]
    if s[0]==0:
        A.append(s[1])
        print(A)
    elif s[0]==1:
        A.pop()
        print(A)
    elif s[0]==2:
        print()
        