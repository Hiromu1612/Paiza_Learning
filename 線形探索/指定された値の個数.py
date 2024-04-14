n=int(input())
for i in range(n):
    a=map(int,input().split())
k=int(input())
if k in a:
    print('Yes')

#解答
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

num_of_k = 0
for val in a:
    if val == k:
        num_of_k += 1

print(num_of_k)

#別解
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

print(a.count(k)) #count()でリスト内の要素の数を数える