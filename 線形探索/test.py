n=int(input())
a=[int(i) for i in input().split()]
k=int(input())
sum=0
for s in a:
    if s==k:
        sum+=1
print(sum)

print(a.count(k))