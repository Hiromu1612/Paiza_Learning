n=int(input())
for i in range(n):
    values=list(map(int,input().split()))
    print(*values[1:]) #アンパック演算子*でリストの中身を展開して出力 [1,2,3]なら1 2 3を出力