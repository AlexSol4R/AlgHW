import math
n=int(input("n = "))
for i in range(1,n+1):
    lnn = n*math.log(i,2)
    power = 2**i
    fact = 1
    for j in range(2,i+1):
        fact*=j
    print("{:2} {:7.3f} {:2} {:2}".format(i, lnn, power, fact))