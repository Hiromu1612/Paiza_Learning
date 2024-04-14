n=int(input())
a=[int(x) for x in input().split()]
k=int(input())
if k in a:
    print()

#解答
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k = -1
for i in range(n):
    if a[i] == k:
        index_of_k = i
        break

print(index_of_k + 1)

#別解
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

if k in a:
    print(a.index(k) + 1) #index()でリスト内の要素のインデックスを取得
else:
    print(0)