#'factors.py'
#to be used in computing eigan values of matricies

def primefact(n): #gives prime factorization of n
    pf = list()
    if n<0:
        n = -n
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                pf.append(i)
                n = n/i
                break   
    return pf


def factorization(n):
    f = list()
    if n<0: n = -n
    f.append(1)
    f.append(n)
    for i in primefact(n):
        if not(i in f):
            f.append(i)
        for j in f:
            if n%(i*j)==0 and not(i*j in f):
                f.append(i*j)
    for m in f:
        if m>0:
            f.append(-m)
    f.sort()
    return f
