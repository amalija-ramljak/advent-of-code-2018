from classes24 import Group
from fight import fight
from copy import deepcopy

groups = set()

"""
    To not lose your mind, prepare the input beforehand in a txt, each group in one line,
    values separated by spaces in this order:
    [string] group type - inf for infection, imm for immune system
    [int] group size - the amount of units in the group
    [int] hit/health points - per unit, how much damage can they handle?
    [int] damage - per unit, how much damage does one deal?
    [string] damage type - the type of attack of the group
    [int] initiative - how much initiative do they have? higher - act sooner
    [int] immunity count - how many types of damage are they immune to? (such damage turns to 0 on them)
    [strings] immunities - names of damage types they are immune to, is count is 0 skip to next element
    [int] weakness count - how many types of damage are they weak to? (such damage doubles on them)
    [strings] weaknesses - same for immunities...
"""

while True:
    line = input()
    if line == "":
        break
    line = line.split(" ")
    spec = line[0]
    n = int(line[1])
    health = int(line[2])
    damage = int(line[3])
    dmg_type = line[4]
    initiative = int(line[5])

    immune_to = int(line[6])
    i = 7
    if immune_to == 0:
        immune_set = set()
    else:
        immune_set = set()
        for j in range(immune_to):
            immune_set |= {line[i+j]}
        i += immune_to

    weak_to = int(line[i])
    i += 1
    if weak_to == 0:
        weak_set = set()
    else:
        weak_set = set()
        for j in range(weak_to):
            weak_set |= {line[i+j]}

    group = Group(spec, n, health, initiative, damage, dmg_type, immune_set, weak_set)
    groups |= {group}

groups = list(groups)
groups.sort()
fight(deepcopy(groups), 1)
# will run a bit more slowly if a large number of simulations is needed, or if the input is large, perhaps
# worst if both
fight(groups, 2)
