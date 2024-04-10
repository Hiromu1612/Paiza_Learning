N,M=map(int,input().split())   
A=input().split()
print(A[M-1]) #OK

#解答
N, M = map(int, input().split())
A = [int(x) for x in input().split()]

print(A[M-1]) #データの位置がわかっているときに、そのデータに直接アクセスすることをランダムアクセスといいます。配列はランダムアクセスをサポートするデータ型です。