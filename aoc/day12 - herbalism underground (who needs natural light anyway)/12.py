import numpy as np
from collections import deque as dq

rules = dict()
initial = dq(input().split(" ")[2])
initial.extendleft(['.' for i in range(10)])
initial.extend(['.' for i in range(15)])
initial = list(initial)
input() # empty line

while True:
    rule = input()
    if rule == "":
        break
    rule = rule.split(" ")
    rules[rule[0]] = rule[2]  # '.#.##' : '.'

print("0:")
pot_sum = 0
for i in range(len(initial)):
    if initial[i] == '#':
        pot_sum += i-10
print("\tSum of pots in gen: " + str(pot_sum))
zero_index = 10
for gen in range(1, 171):  # stable at gen 170
    current = 2
    new_gen = initial[0:current]
    for i in range(current, len(initial)-2):
        key = "".join(initial[i-2:i+3])
        if key in rules:
            new_state = rules[key]
        else:
            new_state = '.'
        new_gen.append(new_state)
    new_gen.extend(initial[len(initial)-2:len(initial)])
    test = new_gen
    new_gen = dq(new_gen)
    if '#' in test[0:3]:
        new_gen.extendleft(['.' for i in range(2)])
        zero_index += 2
    if '#' in test[len(test)-3:len(test)]:
        new_gen.extend(['.' for i in range(2)])
    initial = list(new_gen)
    print(gen, end=":\n")
    pot_sum_new = 0
    for i in range(len(initial)):
        if initial[i] == '#':
            pot_sum_new += i-10
    print("\tSum of pots in gen: " + str(pot_sum_new))
    print("\tCompared to previous gen: " + str(pot_sum_new - pot_sum))
    if gen == 170:
        diff = pot_sum_new - pot_sum
    pot_sum = pot_sum_new

print("\nSum of pots in gen 50000000000: ", end="")
print(pot_sum_new + diff*(50000000000-gen))
