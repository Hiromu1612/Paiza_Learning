N,M=map(int,input().split())
a=map(int,input().split())
for i in a:
    print(i[M-1])

#解答
N, M = map(int, input().split())
A = [int(x) for x in input().split()]

print(A[M-1]) #データの位置がわかっているときに、そのデータに直接アクセスすることをランダムアクセスといいます。配列はランダムアクセスをサポートするデータ型です。