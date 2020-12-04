#Joseph Harrison 2020
#find a particular solution using the four-point algorithm to solve linear congruences
import gcdbez
import timeit

#find a particular solution for a congruence
def four_pnt(a, b, n):
    #reduce congruence
    a %= n
    b %= n
    #step 1: let d = gcd(a, n)
    d = gcdbez.gcd(a, n)
    #if d doesn't divide b, no solutions
    if b % d != 0:
        return None, n
    #step 2: 'divide' congruence by d
    a, b, n = a // d, b // d, n // d
    while True:
        #step 3: let m = gcd(a, b)
        #'divide' a and b by m but check that b isn't zero first
        if b != 0:
            m = gcdbez.gcd(a, b)
            a, b = a // m, b // m
        else:
            #if b is zero then the solution must also be zero
            return 0, n
        #if a is +- 1, we can 'read off' a solution
        if a == 1:
            return b % n, n
        elif a == -1:
            return -b % n, n
        #step 4: find a p s.t gcd(a, b + pn) > 1
        p, _ = four_pnt(n % a, -b % a, a)
        b += p * n

if __name__ == '__main__':
    print('solve linear congruences of the form:\n')
    print('                 ax := b mod (n)\n')
    print('by finding a particular solution using the four-point algorithm\n')
    a = gcdbez.get_int_input('a: ')
    b = gcdbez.get_int_input('b: ')
    n = gcdbez.get_int_input('n: ', lambda x: x > 0, 'n must be positive')
    start = timeit.default_timer()
    x0, n = four_pnt(a, b, n)
    end = timeit.default_timer()
    if x0 != None:
        print(f'\nx = {x0} + {n}t for any integer t')
    else:
        print("\nno solutions as gcd(a, n) doesn't divide b")
    print(f'finished in {round(end - start, 4)}s (4d.p)')
