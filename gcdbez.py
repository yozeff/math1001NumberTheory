#Joseph Harrison 2020
#gcd and gcd with Bezout coefficients
import timeit

#used by the other programs so it's here for convenience
def get_int_input(prompt, cond=lambda x: True, err=None):
	while True:
		try:
			x = int(input(prompt))
			if cond(x):
				return x
			else:
				print(err)
		except ValueError:
			print('must be an integer')

#Euclid's algorithm for gcd
def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)

#uses Euclid's algorithm to find gcd and coefficients for Bezout's identity
def gcd_bez(a, b):
	#find the quotient and remainder
	q, r = a // b, a % b
	if r == 0:
		return b, 0, 1
	else:
		d, u, v = gcd_bez(b, a % b)
		#Bezout's identity uses this observation
		#bu + vr = d
		#bu + v(a - qb) = d
		#av + (u - qv)b = d
		return d, v, u - q * v

if __name__ == '__main__':
	print("find greatest common divisor and find integers satisfying Bezout's identity:\n")
	print('                 au + bv = gcd(a, b)\n')
	a = get_int_input('a: ')
	b = get_int_input('b: ')
	start = timeit.default_timer()
	d = gcd(a, b)
	end = timeit.default_timer()
	print('\nalgorithm for just gcd:')
	print(f'\n                 gcd({a}, {b}) = {d}')
	print(f'\nfinished in {round(end - start, 4)}s (4d.p)')
	start = timeit.default_timer()
	d, u, v = gcd_bez(a, b)
	end = timeit.default_timer()
	print("algorithm for gcd and Bezout's coefficients")
	print(f'\n                 gcd({a}, {b}) = {d}')
	print(f'\n                 {a} * {u} + {b} * {v} = {d}')
	print(f'\nfinished in {round(end - start, 4)}s (4d.p)')
