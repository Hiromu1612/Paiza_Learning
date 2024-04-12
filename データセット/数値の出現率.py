N=int(input())
A=map(int,input().split())
count=[0]*10
for i in A:
    count[i]+=1
print(*count) #OK

#解答
N = int(input())
A = [int(x) for x in input().split()]
A=map(int,input().split())#これの方が分かりやすい

count = [0] * 10
for num in A: #リストAの要素を取り出す
    count[num] += 1
print(" ".join(map(str, count)))