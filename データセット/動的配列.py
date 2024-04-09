N,Q=map(int,input().split())
A=[int(i) for i in input().split()]
for i in range(Q):
    query=[int(i) for i in input().split()]
    if query[0]==0:
        result=A.append(query[1])
    elif query[0]==1:
        result=A.pop()
    else:
        print(" ".join(map(str,A)))

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
        A.pop() #pop()はリストの末尾の要素を削除します
    else:
        # print
        print(" ".join(map(str, A)))