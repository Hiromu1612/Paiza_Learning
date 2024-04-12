N=int(input())
S=[input() for  i in range(N)]


#解答
N = int(input())
S = input()

count = {chr(x): 0 for x in range(ord("a"), ord("z")+1)} #ord()で文字をASCIIコードに変換 order(順序) char()でASCIIコードを文字列に変換 {key:value}
print(count) #{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for char in S:
    count[char] += 1

print(" ".join(map(str, count.values()))) #values()で辞書の値だけを取り出す