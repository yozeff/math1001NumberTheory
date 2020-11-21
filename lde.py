#Joseph Harrison 2020
#solve linear diophantine equations in 2 variables
import gcdbez
import timeit

def main():
	print('solve linear diophantine equations of the form:\n')
	print('                 ax + by = c\n')
	print('by finding an integer solution (x, y)\n')

	#get a, b and c
	a = gcdbez.get_int_input('a: ')
	b = gcdbez.get_int_input('b: ')
	c = gcdbez.get_int_input('c: ')

	start = timeit.default_timer()

	#find the gcd of a and b and a u and v satisfying au + bv = d using Bezout's identity
	d, u, v = gcdbez.gcd_bez(a, b)

	#find a particular solution by multiplying each Bezout coefficient by c / d s.t ax0 + by0 = c
	x0 = c // d * u
	y0 = c // d * v

	end = timeit.default_timer()

	#output the solutions (if they exist)
	print('\nequation and solutions:\n')
	print(f'                 {a}x + {b}y = {c}\n')
	if c % d != 0:
		print(f"no integer solutions, because {d} doesn't divide {c}")
	else:
		print(f'x = {x0} - {b // d}n and y = {y0} + {a // d}n for any integer n')
	print(f'finished in {round(end - start, 4)}s (4d.p)')

if __name__ == '__main__':
	main()