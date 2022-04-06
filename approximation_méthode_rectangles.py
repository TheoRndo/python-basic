def f(x):
    return 1/(1+x**2)

somme = 0
n = int(input("Nombre de rectangles : "))
a = int(input("Borne inf : "))
b = int(input("Borne sup : "))

if a < b:
    for k in range (n):
        somme += f(a+k*(b-a)/n)
print((b-a)*somme/n)