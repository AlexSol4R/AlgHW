import math
M,N=1000,10000
prime=[i for i in range(2,N+1)]
for p in range(2,math.floor(math.sqrt(N))+1):
    j=p**2
    while j<N+1:
        prime[j-2]=0
        j+=p
while 0 in prime: prime.remove(0)
i=0
while prime[i] < M: prime.remove(prime[i])
print(prime,len(prime))