n=int(input())
a_list=list(map(int,input().split()))
q=int(input())
b_list=list(map(int,input().split()))

for i in b_list:
    print(*i)
    
#解答
N = int(input())
A = [int(x) for x in input().split()] #[10,20,30]
Q = int(input())
B = [int(x) for x in input().split()]
for i in range(Q):
    print(A[B[i]-1])