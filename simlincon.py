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
	#k = gcdbez.get_int_input('k: ', lambda x: x > 0, 'k must be positive')

	print('enter the constants in each congruence:')

	#how long did the program take (not including waiting for user input or outputting)
	total_time = 0

	i = 0
	cont_flag = True
	while cont_flag:
		a = gcdbez.get_int_input('\na: ')
		b = gcdbez.get_int_input('b: ')
		n = gcdbez.get_int_input('n: ', lambda x: x > 0, 'n must be positive')

		print(f'{a}x := {b} mod ({n})\n')

		start = timeit.default_timer()

		#need to solve/simplify each congruence so its in the form x := b mod (n) otherwise we can't use
		#the chinese remainder theorem
		b, n = lincon.four_pnt(a, b, n)

		#its possible that the given congruence has no solutions
		if b == None:
			print(f'the last congruence has no solutions')
		elif i != 0:
			#amend our current solution so that it satisfies the new congruence
			cur_soln = solve(cur_soln, (b, n))
			print(f'x = {cur_soln[0]} + {cur_soln[1]}t for any integer t')
		else:
			#on the first iteration produce the current solution by just solving the first congruence
			cur_soln = (b, n)
			print(f'x = {cur_soln[0]} + {cur_soln[1]}t for any integer t')

		i += 1

		end = timeit.default_timer()
		total_time += end - start

		cont_flag = False if input("'quit' to quit: ") == 'quit' else True

	print(f'finished in {round(total_time, 4)}s (4d.p)')

if __name__ == '__main__':
	main()