N=input()[::-1]
for i in range(len(N)):
    if i % 3 == 0 and i != 0:
        print(",", end="")
    print(N[-i-1], end="")