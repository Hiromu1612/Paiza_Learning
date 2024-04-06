N,M=map(float,input().split())  
N=round(N,M)
print(N)

#解答
values = input().split()
N = float(values[0])
M = int(values[1])

print("{:.{}f}".format(N, M)) #{}にNを、{}にMを代入している