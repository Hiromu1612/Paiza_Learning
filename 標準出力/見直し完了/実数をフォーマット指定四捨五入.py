N=int(input())
for i in range(1,N+1):
    M=input().split()
    print("{:.{}f}".format(float(M[0]),int(M[1])))