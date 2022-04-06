def g(x):
    return 1/(1+x**2)

somme = 0
n = int(input("Découpage : "))
a = int(input("Borne inf : "))
b = int(input("Borne sup : "))

for k in range (n):
    somme += g(a+k*(b-a)/n) + g(a+(k+1)*(b-a)/n)
print ((b-a)*somme/n/2)