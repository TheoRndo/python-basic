# Approximation de pi par la série de Gregory-Leibniz

k = 1
s = 0
n=int(input("Donner n : "))

for i in range(n):
	if i % 2 == 0:
		s += 4/k
	else:
		s -= 4/k
	k += 2	
print(s)

