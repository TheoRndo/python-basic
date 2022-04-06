k = int(input("Nombre à tester : "))

if k > 1:
    for i in range(2, int(k/2)+1):
         if (k % i) == 0:
            print(k,"n'est pas un nombre premier")
            break
    else:
        print(k,"est un nombre premier")
else:
    print(k,"n'est pas un nombre premier")