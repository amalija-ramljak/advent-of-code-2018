from opcode import instructions
from math import sqrt


def calculate_values(instruction):
    main = instruction[0]

    typ = main[2:] if main[0:2] in {'gt', 'eq'} else main[3:]  # subtype for a, b, c values

    main = main[0:len(main)-len(typ)]  # main part, key for instructions
    func = instructions()[main]

    # always a register
    c = int(instruction[3])

    f = typ[0]
    if main in {"set", "gt", "eq"} and f == "i":
        a = int(instruction[1]), False
    else:
        a = int(instruction[1]), True

    f = typ if len(typ) == 1 else typ[1]
    if f == 'r':
        b = int(instruction[2]), True
    else:
        b = int(instruction[2]), False

    return func, a, b, c


def find_divisors(number):
    top = int(sqrt(number))
    divs = []
    for i in range(1, number+1):
        if number / i == number // i:
            divs.append(i)
    return divs


def calc_gauss_sum(n):
    return n*(n+1)/2
