N=int(input())
A=[input() for i in range(1,N+1)]

#解答
N = int(input())
A = [int(x) for x in input().split()]

count = [0] * 10
for num in A:
    count[num] += 1
print(" ".join(map(str, count)))