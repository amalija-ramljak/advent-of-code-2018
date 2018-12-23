from opcode import *

instruction_numbers = [set() for i in range(16)]
instructions = instructions()

vague_3 = 0

before = []
after = []
instr = []
while True:
    line = input()
    if line == "done":
        break
    if line == "":
        pass
    elif line[0] == "B":
        before = line[9:len(line)-1].split(", ")
        for i, el in enumerate(before):
            before[i] = int(el)
        # print(before)
    elif line[0] == "A":
        after = line[9:len(line)-1].split(", ")
        for i, el in enumerate(after):
            after[i] = int(el)
        # print(after)
    else:
        instr = line.split(" ")

    if line == "":
        instrs = []
        numbers_index = int(instr[0])  # in which place the info will be saved
        for main in instructions:
            if main in {"gt", "eq"}:
                types = ["ir", "ri", "rr"]
            else:
                types = ["r", "i"]
            func = instructions[main]
            c_reg = int(instr[3])
            for t in types:
                f = t[0]   # r or i
                if main in {"set", "gt", "eq"} and f == "i":
                    # a_reg = None
                    a_val = int(instr[1])
                else:
                    a_reg = int(instr[1])
                    a_val = before[a_reg]

                f = t if len(t) == 1 else t[1]
                if f == 'r':
                    b_reg = int(instr[2])
                    b_val = before[b_reg]
                else:
                    # b_reg = None
                    b_val = int(instr[2])

                outcome = func(a_val, b_val)  # value of c
                new_regs = before[:]
                new_regs[c_reg] = outcome
                if new_regs == after:
                    instrs.append(main+t)
        if len(instrs) >= 3:
            vague_3 += 1
        if len(instrs) == 1:
            instruction_numbers[numbers_index] = set(instrs)
        else:
            if len(instruction_numbers[numbers_index]) != 1:
                instruction_numbers[numbers_index] |= set(instrs)

print("Part 1: ", vague_3, end="\n\n")

single_meaning = set()
for inst in instruction_numbers:
    if len(inst) == 1:
        #print(inst)
        single_meaning |= inst
#print("Single:", single_meaning)

done = False
while not done:
    for num, insts in enumerate(instruction_numbers):
        if len(insts) == 1:
            continue
        #print(num, insts)
        #print("single", single_meaning)
        insts -= single_meaning
        instruction_numbers[num] = insts
        #print(num, insts, end="\n\n")

    for inst in instruction_numbers:
        if len(inst) == 1:
            single_meaning |= inst
    #print("Single:", single_meaning, end="\n\n\n")

    if len(single_meaning) == 16:
        done = True

for num, i in enumerate(instruction_numbers):
    ins = i.pop()
    f = ins[0:len(ins)-2] if ins[0:len(ins)-2] in {'gt', 'eq'} else ins[0:len(ins)-1]
    instruction_numbers[num] = (ins, instructions[f])
    print(num, ins)

print("Part 2 input: ")
registers = [0, 0, 0, 0]
while True:
    line = input()
    if line == "":
        break
    line = line.split(" ")
    for i, el in enumerate(line):
        line[i] = int(el)

    instruction = instruction_numbers[line[0]]  # type, function
    func = instruction[1]

    main = instruction[0]
    #print(main, end=" ")
    typ = main[2:] if main[0:2] in {'gt', 'eq'} else main[3:]  # subtype
    main = main[0:len(main)-len(typ)]  # main part, key for instructions
    #print(main, end=" ")

    c_reg = int(line[3])
    #print(c_reg, end=" ")

    f = typ[0]
    if main in {"set", "gt", "eq"} and f == "i":
        a_reg = None
        a_val = int(line[1])
    else:
        a_reg = int(line[1])
        a_val = registers[a_reg]

    f = typ if len(typ) == 1 else typ[1]
    if f == 'r':
        b_reg = int(line[2])
        b_val = registers[b_reg]
    else:
        b_reg = None
        b_val = int(line[2])

    """
    if a_reg is None:
        print("Val", a_val, end=" ")
    else:
        print("Reg", a_reg, end=" ")
    if b_reg is None:
        print("Val", b_val)
    else:
        print("Reg", b_reg)
    """
    outcome = func(a_val, b_val)  # value of c
    registers[c_reg] = outcome
    #print(registers)

print("\n\nPart 2:", registers[0])
