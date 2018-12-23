from helpers19 import *
from time import sleep

viable = {
    4921107,
    4921111,
    4921112,
    4921126,
    4921137,
    4921139,
    4921149,
    4921157,
    4921170,
    4921181, # nope
    4921183, # nope
    4921192,
    4921196,
    4921203,
    4921208,
    4921214,
    4921216,
    4921220,
    4921221,
    4921227,
    4921236,
    4921237,
    4921241,
    4921242,
    4921244,
    4921254,
    4921257,
    4921260,
    4921263,
    4921266,
    4921270,
    4921272,
    4921286,
    4921287,
    4921293,
    4921313,
    4921316,
    4921319,
    4921330,
    4921331,
    4921335,
    4921341,
    4946833,
    5201505,
    5201566,
    5541865,
    6020107,
    6020141,
    6217804,
    6218010,
    6218981,
    6219228,
    6415501,
    6415519,
    6530666,
    6684356,
    7025999,
    7026100,
    7073524,
    7140390,
    7140533,
    7206289,
    7206499,
    7220597,
    7220742,
    7222223,
    7222442,
    7469885,
    7469922,
    7479919,
    7532696,
    7532951,
    7567264,
    7760479,
    7865279,
    7865517,
    7953808,
    8039101,
}

instruction_register = int(input().split(" ")[1])

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

#for v in viable:
registers = [1 if i == 0 else 0 for i in range(6)]
repetition_count = 0
first = True

threes = []
while registers[instruction_register] < max_pointer:
    prev_3 = registers[3]
    repetition_count += 1
    # print(repetition_count)
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
    if registers[3] in threes and registers[3] != prev_3:
        print(threes[-1])
        break
    if registers[3] in range(4921098, 8563139):
        threes.append(registers[3])
    if repetition_count == 10**6:
        break
