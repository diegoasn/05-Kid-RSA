#Kid RSA

import fileinput

"""setup_kid_RSA(a, b, A, B)
   Calcula los elementos M, e, d y n, necesarios para el cifrado y descifrado de kid RSA.
   a - número entero random
   b - número entero random
   A - número entero random
   B - número entero random""" 
def setup_kid_RSA(a, b, A, B):
	M = (a * b) - 1
	e, d = (A * M) + a, (B * M) + b
	n = (e * d - 1) // M
	return [M, e, d, n]

"""kid_RSA(mode, a, b, A, B)
   mode - 'E' para cifrar y 'D' para descifrar
   a - número entero random
   b - número entero random
   A - número entero random
   B - número entero random
   m - mensaje a cifrar/descifrar"""
def kid_RSA(mode, a, b, A, B, m):
	s = setup_kid_RSA(int(a), int(b), int(A), int(B))
	if mode == 'E':
		return (int(m) * s[1]) % s[3]
	else:
		return (int(m) * s[2]) % s[3]

l = list()
for line in fileinput.input():
	line = line.replace('\n','')
	l.append(line)

print(kid_RSA(l[0], l[1], l[2], l[3], l[4], l[5]))