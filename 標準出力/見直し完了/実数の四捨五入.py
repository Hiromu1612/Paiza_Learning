N=float(input())
N=round(N,3) #小数点第3位まで表示
print("{:.3f}".format(N)) #小数点が3桁までない場合は0で埋める

#解答
N = float(input())
print("{:.3f}".format(N))#小数点以下の桁数の指定は、{:.桁数f} 