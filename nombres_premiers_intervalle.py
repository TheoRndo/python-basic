min = int(input("Entrez le min : "))
max = int(input("Entrez le max : "))

print("Les nombres premiers entre", min, "et", max, "sont :")
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)