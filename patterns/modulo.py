def modulo(n , d):
	q = int(n/d);
	remainder = (n-(q*d))
	return remainder

n = int(input("Enter n : "))
d = int(input("Enter d : "))
print(modulo(n,d))
