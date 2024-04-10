a,b,c=map(int,input().split())
max=max(a,b,c)
min=min(a,b,c)
print(max-min) #OK

s=list(map(int,input().split()))
s.sort()
print(s[-1]-s[0])#OK

#解答
li = [int(i) for i in input().split()]
li.sort() #昇順にソートした後のリストでは、先頭の要素が最小値、末尾の要素が最大値 降順にしたいときは、sort(reverse=True)とする
print(li[2] - li[0])

#解答2
li = [int(x) for x in input().split()]
print(max(li) - min(li))
