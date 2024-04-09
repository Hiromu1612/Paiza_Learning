H,W,r,c=int(input().split())
for h in range(1,H+1):
    for w in range(1,W+1):
        if h==r and w==c:
            a=a

# 解答
H, W, r, c = map(int, input().split())
maze=[input() for _ in range(H)]

#for文使うと
maze = []
for _ in range(H):
    maze.append(input())

if maze[r-1][c-1] == "#": #maze[r-1][c-1]は、r行目のc列目の要素を表しています 行と列の指定ができる
    print("Yes")
else:
    print("No")