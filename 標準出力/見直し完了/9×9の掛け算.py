for i in range(1,10):
    for j in range(1,10):
        if j==9:
            print(i*j)
        else:
            print(i*j,end=" ") #OK

#解答
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print(i * j,end="\n")
        else:
            print(i * j, end=" ")