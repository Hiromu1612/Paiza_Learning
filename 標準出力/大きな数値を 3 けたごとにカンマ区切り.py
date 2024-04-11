N=input().split()
for i in int(N):
    if i%3==2:
        print(i,end=",")
    else:
        print(i,end="")
print()

#解答
N = input()
for i in range(len(N)):
    if i % 3 == 0 and i != 0: #i=3 : カンマを改行無しで出力してから 3 を改行無しで出力 (122,3)
        print(",", end="")

    print(N[i], end="")
print()

#3つの数字後にカンマ
N=list(input())
for i in range(len(N)):
    if i%3==2 and i!=0 and i!=len(N)-1:
        print(N[i],end=",")
    else:
        print(N[i],end="")