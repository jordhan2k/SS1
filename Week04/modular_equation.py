

# def modular_arithmetic_solver(a: int, b: int, n: int):
#
#     # Step 1: Get greatest common divisor
#     if (a > n):
#         a = a % n
#     d , s, r = euclidean_algo(n, a)
#     ddqr_table = greatest_common_divisor_table(a, n)
#     display_ddqr_table(ddqr_table)
#     print(euclidean_algo(n, a))
#
#     # Step 2:
#     if b % d == 0:
#         root_num = d
#         d, s, r = euclidean_algo(n, a)
#
#         print('No. of roots: ', root_num)
#         x0 = (r * (b // d)) % (n // d)
#         print('x0', x0)
#         root_list = []
#         for i in range(0, d):
#             root_list.append(x0 + (i*n)//d)
#         print(root_list)
#     else:
#         root_num = 0
#
#     # Step 3
#     # Identify d = n.(s) + a.(r)




#đi chép
def euclidean_algo(n, a):
    # Base Case
    if a == 0:
        return n, 1, 0
    else:
        d, s, r = euclidean_algo(a, n % a)
        # if s != 0 and r != 0:
            # print(d, s, r)
        return (d, r, s-(n // a) * r)

def gcd(a: int, n: int):
    if a == 1 or n == 1:
        return 1
    else:
        while a != 0:
            c = n
            n = a
            q = c // a
            a = c % a
    return n
# Function to get a table for dividend, divisor, quotient, remainder
def greatest_common_divisor_table(a: int, n: int):
    ddqr_table = []
    if a == 1 or n == 1:
        return 1
    else:
        while a != 0:
            c = n
            n = a
            q = c // a
            a = c % a
            ddqr_table.append(c)
            ddqr_table.append(n)
            ddqr_table.append(q)
            ddqr_table.append(a)
    return ddqr_table

# Identify d = n.(s) + a.(r)
def identify_s_and_r(ddqr_table: list, gcd: int):
    s_r_report = ''
    dividend = []
    divisor = []
    for i in range(0 , len(ddqr_table)):
        if (i % 4 == 0):
            dividend.append(ddqr_table[i])
        if (i % 4 == 1):
            divisor.append(ddqr_table[i])
    dividend.reverse()
    divisor.reverse()
    r = 1
    s_list = []
    r_list = []
    for i in range(1, len(dividend)):
        s = r
        s_list.append(s)
        r = (gcd - dividend[i]* s) // divisor[i]
        r_list.append(r)
    for j in range(1, len(dividend)):
        s_r_report += ('Step {}: {} = {}.({}) + {}.({}) \n'.format(j - 1, gcd, dividend[j], s_list[j-1], divisor[j], r_list[j-1]))

    return s_r_report, s_list[len(s_list)-1], r_list[len(r_list)-1]














# Function to display a table of dividend, divisor, quotient, remainder
def display_ddqr_table(ddqr_table):
    dividend = []
    divisor = []
    quotient = []
    remainder = []
    print('{0:^10s}|{1:^10s}|{2:^10s}|{3:^10s}'.format('Dividend', 'Divisor', 'Quotient', 'Remainder'))
    for i in range(0 , len(ddqr_table)):
        if (i % 4 == 0):
            dividend.append(ddqr_table[i])
        if (i % 4 == 1):
            divisor.append(ddqr_table[i])
        if (i % 4 == 2):
            quotient.append(ddqr_table[i])
        if (i % 4 == 3):
            remainder.append(ddqr_table[i])
    for i in range(0, len(dividend)):
        print('{0:^10d}|{1:^10d}|{2:^10d}|{3:^10d}'.format(dividend[i], divisor[i], quotient[i], remainder[i]))




# modular_arithmetic_solver()

#
# modular_arithmetic_solver(2323, 8, 5544)



def display_solution(a, b, n):
    print('<<<< SOLUTION >>>>')
    print('The equation: {} x X = {} (mod {})       (1)'.format(a, b, n))

    af = a % n
    if a > n:
        print('We can see: ')
        print('      {} x X (mod {}) = {} x X'.format(a, n, af))
        print('then the equation (1) is changed to: ')
        print('      {} x X = {} (mod {})                (2)'.format(af, b, n))
        print('Solve the equation (2): ')
    else:
        print('Solve the equation (1): ')
    d = gcd(a, n)
    gcd_table = greatest_common_divisor_table(af, n)
    display_ddqr_table(gcd_table)
    print('{:^40}'.format('Table 1. GCD Algorithm'))
    s_r_report, s, r = identify_s_and_r(gcd_table, d)
    print('We have d = gcd({}, {}) = {} => {} roots'.format(af, n, d, d))
    print(s_r_report)
    x0 = (r * (b // d)) % (n // d)
    print('x0 = (r x b)/d mod (n/d) = ({}x{}/{}) mod ({}/{}) = {}'.format(r, b, d, n, d, x0))
    root_list = []
    for i in range(0, d):
        root_list.append(x0 + (i*n)//d)
    print('=> x = {}'.format(root_list))




def modular_arithmetic_solver():
    while True:
        try:
            a = int(input('Enter a: '))
            if a < 0:
                print('Invalid input, please re-input!')
                continue
            else:
                break
        except ValueError:
            print('Invalid input, please re-input!')
            continue
    while True:
        try:
            b = int(input('Enter b: '))
            if b < 0:
                print('Invalid input, please re-input!')
                continue
            else:
                break
        except ValueError:
            print('Invalid input, please re-input!')
            continue
    while True:
        try:
            n = int(input('Enter n: '))
            if n < 0:
                print('Invalid input, please re-input!')
                continue
            else:
                break
        except ValueError:
            print('Invalid input, please re-input!')
            continue

    display_solution(a, b, n)


modular_arithmetic_solver()
