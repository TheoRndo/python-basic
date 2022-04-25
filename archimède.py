from math import sin,tan,pi

n=int(input("Donner n : "))
# Il faut que n soit plus grand ou égal à 3

def archimedeSimple(n):
    return n*sin(pi/n),n*tan(pi/n)
print(archimedeSimple(n))


N = 3*(2**n)
def archimedeSimple(N):
    return N*sin(pi/N),N*tan(pi/N)
print(archimedeSimple(N))

from math import sqrt
def archimede(n):
    a = 2*sqrt(2)
    b = 4
    for i in range(n):
        b = (2*a*b)/(a+b)
        a = sqrt(b*a)
    return a,b
print(archimede(n))

from math import sqrt
def archimede(n):
    a = (3*sqrt(3))/2
    b = 3*sqrt(3)
    for i in range(n):
        b = (2*a*b)/(a+b)
        a = sqrt(b*a)
    return a,b
print(archimede(n))