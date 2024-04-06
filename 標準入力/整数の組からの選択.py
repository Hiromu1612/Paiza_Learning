n=int(input())
for i in range(n):
    for j in range(n):
        print()
        
#解答
N = int(input())
a = []
b = []
for i in range(N):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

print(a[7], b[7])

# n=int(input())
# for i in range(n):
#     a,b=list(map(int,input().split()))
#     print(a[7],b[7])