#Joseph Harrison 2020
#find prime-power factorisations
import gcdbez

def prime_pow_fact(n):
	ppf = {}
	#divide n by 2 until it 2 doesn't divide it anymore
	while n % 2 == 0:
		if 2 not in ppf:
			ppf[2] = 1
		else:
			ppf[2] += 1
		n //= 2
	#now try all odd integers
	k = 3
	while n != 1 and k <= n:
		if n % k == 0 and k not in ppf:
			ppf[k] = 0
		#divide n by k until k doesn't divide it anymore
		while n % k == 0:
			ppf[k] += 1
			n //= k
		k += 2
	return ppf

#format the ppf in a neat table
def table(ppf):
	key_len = max([len(str(p)) for p in ppf.keys()] + [5])
	print(f"\nprime{' ' * (key_len - 5)} : exponent")
	for p in ppf:
		print(f"{p}{' ' * (key_len - len(str(p)))}   {ppf[p]}")

def main():
	print('find the prime-power factorisation of n > 1\n')
	n = gcdbez.get_int_input('n: ', lambda x: x > 1, 'n must be greater than 1')
	ppf = prime_pow_fact(n)
	table(ppf)

if __name__ == '__main__':
	main()