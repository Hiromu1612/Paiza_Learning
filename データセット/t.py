N=int(input())
A=[int(i) for i in range(1,N+1)]
count=[0]*10
for j in A:
    count[j]+=1
print(" ".join(map(str,count)))