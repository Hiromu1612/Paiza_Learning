N,M=map(int,input().split())
total_distance=0
for _ in range(N-1):
    distance=int(input())
    if distance <=M:
        total_distance+=distance
print(total_distance)

#解答
# 車の数 N と渋滞と定義する車間距離 M を入力として受け取る
N, M = map(int, input().split())

# 渋滞の区間の合計を初期化する
total_jam_length = 0

# 各車の車間距離を入力として受け取る
for _ in range(N-1):
    distance = int(input())
    # 車間距離が M 以下の場合、渋滞の区間の合計に加える
    if distance <= M:
        total_jam_length += distance

# 渋滞の区間の合計を出力する
print(total_jam_length)