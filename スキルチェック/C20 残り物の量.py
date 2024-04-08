values=list(map(int,input().split()))
m=values[0]
p=values[1]
q=values[2]

unsold=m*(1-p/100)*(1-q/100)
print("{:.2f}".format(unsold)) #OK