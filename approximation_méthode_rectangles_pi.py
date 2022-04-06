def f(x):
    return 1/(1+x**2)

somme = 0
n = int(input("Nombre de rectangles : "))
a = 0
b = 1

if a < b:
    for k in range (n):
        somme += f(a+k*(b-a)/n)
print(((b-a)*somme/n)*4)

# Prendre un n assez grand pour une meilleure approximation de pi