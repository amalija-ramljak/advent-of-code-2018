from opcode import *
from helpers19 import *


instruction_register = int(input().split(" ")[1])
registers = [0 for i in range(6)]

program = []
while True:
    line = input()
    if line == "":
        break
    line = line.split(" ")
    # function call, a, b, c
    instruction = calculate_values(line)
    program.append(instruction)

max_pointer = len(program)
while registers[instruction_register] < max_pointer:
    pointer = registers[instruction_register]
    instr = program[pointer]  # f, a, b, c
    func = instr[0]
    a = instr[1]
    b = instr[2]
    c = instr[-1]  # c

    if a[1]:  # a is a register
        a = registers[a[0]]
    else:
        a = a[0]

    if b[1]:
        b = registers[b[0]]
    else:
        b = b[0]

    # fill c
    registers[c] = func(a, b)
    registers[instruction_register] += 1

# print(registers[instruction_register])
print("Part 1", registers[0])

the_eq = 10551296   # found through checking the register state for part two, but the loop is gone
divs = find_divisors(the_eq)


print("Part 2", sum(divs))
