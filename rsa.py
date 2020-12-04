#Joseph Harrison 2020
#rsa
import random
import gcdbez
import lincon

#reduce a^e mod (n) by squaring as much as we can
def fast_mod_exp(a, e, n):
	if e % 2 == 1:
		return (a * fast_mod_exp(a, e - 1, n)) % n
	elif e == 0:
		return 1
	else:
		return fast_mod_exp(a ** 2 % n, e // 2, n)

#tests if n is prime or composite using Fermat primality test k is the number of trials. 
#this test is not completely correct
def is_prime(n, k):
	if n > 1:
		for _ in range(k):
			a = random.randint(1, n - 1)
			#from Fermat's little theorem, if n doesn't divide a then a^(n-1) := 1 mod (n) if
			#n is prime, so if this ever doesn't happen then n is composite
			if fast_mod_exp(a, n - 1, n) != 1:
				return False
		return True
	else:
		return False

def main():
	#this is the number of trials that the fermat primality test will use on p and q
	k = 10
	print('rsa implementation')
	#get our two primes p and q. we can use 'is_prime' as the condition function
	print('\nenter primes p and q')
	p = gcdbez.get_int_input('p: ', lambda p: is_prime(p, k), 'p must be prime')
	q = gcdbez.get_int_input('q: ', lambda q: is_prime(q, k), 'q must be prime')
	#this will be the 'public modulus'
	n = p * q
	#this is Euler's phi (totient) function for n
	phi_n = (p - 1) * (q - 1)
	print(f'\nn = {n}, phi(n) = {phi_n}')

	print('\nenter public exponent e')
	e = gcdbez.get_int_input('e: ', lambda e: gcdbez.gcd(e, phi_n) == 1, 
							 'e must be coprime to phi(n)')

	#find f, the multiplicative inverse of e mod (phi(n))
	#since gcd(e, phi(n)) = 1, e is a unit and so has a multiplicative inverse
	f, _ = lincon.four_pnt(e, 1, phi_n)

	print()
	x = gcdbez.get_int_input('number to encode: ')
	print(f'encoded: {fast_mod_exp(x, e, n)}')

	x = gcdbez.get_int_input('number to decode: ')
	print(f'decoded: {fast_mod_exp(x, f, n)}')

if __name__ == '__main__':
	main()