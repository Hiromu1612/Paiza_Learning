N=int(input())
char =[input() for i in range(N)]

#解答
N = int(input())
count = {}

for _ in range(N):
    s = input()
    if s not in count: #countにkeyがない場合
        count[s] = 1 #valueを1にする
    else:
        count[s] += 1

for word, times in sorted(count.items()): #items()でキーと値を取り出す
    print(word, times)