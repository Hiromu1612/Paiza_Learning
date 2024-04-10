N,Q=map(int,input().split())
A=[int(i) for i in input().split()]
for _ in range(Q):
    s=input().split()
    if s[0]==0:
        A.append(s[1])
        print(A)
    elif s[0]==1:
        A.pop()
        print(A)
    elif s[0]==2:
        print()
        
# 解答
N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

for _ in range(Q):#_ は各要素の値を受け取る変数ですが、その値を使用しないことを示しています
    query = [int(x) for x in input().split()]

    cmd = query[0]
    if cmd == 0:
        # push_back
        A.append(query[1]) 
    elif cmd == 1:
        # pop_back
        A.pop() #pop()はリストの末尾の要素を削除します 先頭を削除する場合はpop(0) 2番目を削除する場合はpop(1)
    else:
        # print
        print(" ".join(map(str, A))) #ここで出力 Aはリストなので、文字列に変換