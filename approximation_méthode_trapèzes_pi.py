def g(x):
    return 1/(1+x**2)

somme = 0
n = int(input("Découpage : "))
a = 0
b = 1

for k in range (n):
    somme += g(a+k*(b-a)/n) + g(a+(k+1)*(b-a)/n)
print (((b-a)*somme/n/2)*4)

# Prendre un n assez grand pour une meilleure approximation de pi