N=input().split()
print(",".join(N))

#解答
nums = input().split()

for num in nums:
    print(num, end=",")#print関数はデフォルトで改行するのでend=","で改行しないようにする

print() #最後に改行する