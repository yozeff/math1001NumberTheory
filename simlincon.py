#Joseph Harrison 2020
import lincon
import gcdbez
import timeit

#use our current solution of the form x = x_1 + (n_1)t to find a solution that also satisifes the next 
#congruence
def solve(cur_soln, next_con):
	b_2, n_2 = next_con
	x_1, n_1 = cur_soln
	#find a general solution to the next congruence that uses the current solution
	#x_1 + (n_1)t := b_2 mod (n_2)
	#(n_1)t := b_2 - x_1 mod (n_2)
	x_2, n_2 = lincon.four_pnt(n_1, b_2 - x_1, n_2)
	return x_1 + n_1 * x_2, n_1 * n_2

def main():
	print('solve a system of linear congruences of the form:\n')
	print('                 (a_1)x := b_1 mod (n_1)')
	print('                              ...')
	print('                 (a_k)x := b_k mod (n_k)\n')
	print('where k is a positive integer\n')

	#how many congruences are there?
	k = gcdbez.get_int_input('k: ', lambda x: x > 0, 'k must be positive')

	print('enter the constants in each congruence:\n')

	#store our moduli so we can check new moduli are coprime to all of them
	N = []

	#how long did the program take (not including waiting for user input or outputting)
	total_time = 0

	i = 0
	flag = True
	while i < k and flag:
		a = gcdbez.get_int_input('a: ')
		b = gcdbez.get_int_input('b: ')
		n = gcdbez.get_int_input('n: ', lambda x: x > 0, 'n must be positive')

		print(f'{a}x := {b} mod ({n})\n')

		start = timeit.default_timer()

		#need to solve/simplify each congruence so its in the form x := b mod (n) otherwise we can't use
		#the chinese remainder theorem
		b, n = lincon.four_pnt(a, b, n)

		if i != 0:
			#check that the new modulus is coprime to all the ones we've already been given
			for n_j in N:
				if gcdbez.gcd(n, n_j) != 1:
					print(f'no solutions as {n} and {n_j} not mutually coprime')
					flag = False

			N.append(n)

			#amend our current solution so that it satisfies the new congruence
			if flag:
				cur_soln = solve(cur_soln, (b, n))

		else:
			N.append(n)
			#on the first iteration produce the current solution by just solving the first congruence
			cur_soln = (b, n)
			if b == None:
				print(f'this congruence has no solutions')
				flag = False	

		i += 1

		end = timeit.default_timer()
		total_time += end - start

	if flag:
		print(f'x = {cur_soln[0]} + {cur_soln[1]}t for any integer t')

	print(f'finished in {round(total_time, 4)}s (4d.p)')

if __name__ == '__main__':
	main()