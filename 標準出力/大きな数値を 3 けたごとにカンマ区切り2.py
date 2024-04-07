#解答
N=input()[::-1]
for i in range(len(N)):
    if i % 3 == 0 and i != 0:
        print(",", end="")
    print(N[-i-1], end="") #-i-1で逆順にする


N = input()
x = len(N) % 3
for i in range(len(N)):
    if (i - x) % 3 == 0 and i != 0:
        print(",", end="")

    print(N[i], end="")

print()