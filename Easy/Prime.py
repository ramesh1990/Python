import math

def isPrime(n):
    if (n <= 1):
        return False
    max = math.floor(math.sqrt(n))
    for i in range(2,1+max):
        if(n%i==0):
            return False
    return True
    
    
def isPrime(n):
    m=n**0.5
    m=int(m)
    for i in range(2,m,1):
        if(n%i==0):
            return False
    return True
