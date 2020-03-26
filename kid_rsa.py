#Kid RSA

import fileinput

def setup_kid_RSA(a, b, A, B):
	M = (a * b) - 1
	e, d = (A * M) + a, (B * M) + b
	n = (e * d - 1) // M
	return [M, e, d, n]

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