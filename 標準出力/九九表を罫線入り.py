for i in range(1,10):
    for j in range(1,10):
        if j==9:
            print(" {: >2} ".format(i*j))
        else:
            print("{: >2}".format(i*j),end=" | ")
    if i!=9:
        print("==========================================")

#解答
for i in range(1, 10):
    for j in range(1, 10):
        print("{: >2}".format(i * j), end="") #最初に数字を出力して、改行するか|を出力するかを判断する
        if j == 9:
            print()
        else:
            print(end=" | ")

    if i < 9:
        print("=" * (2 * 9 + 3 * (9 - 1))) #各行で 2 けたの数値を 9 個と 3 文字の区切り文字 | を 9 - 1 = 8 個出力するので、2 * 9 + 3 * 8 = 42 個出力します。