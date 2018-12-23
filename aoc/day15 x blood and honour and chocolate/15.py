from classes import Unit
from helpers20 import *

empty = '.'
wall = '#'
unit_types = {'G', 'E'}

occupied = set()
unit_locations = set()
elves = set()
goblins = set()
walls = set()
units = []
size = 0

i = 0
while True:
    line = input()
    if line == "":
        break
    for j, el in enumerate(line):
        #print(i, j)
        if el == empty:
            continue
        location = (i, j)
        if el in unit_types:
            unit = Unit(el, location)
            units.append(unit)
            unit_locations |= {location}
            if el == 'G':
                goblins |= {location}
            else:
                elves |= {location}
        else:
            walls |= {location}
        occupied |= {location}
    i += 1

size = i
set_data(walls, occupied, unit_locations, i)
"""walls2 = list(walls)
walls2.sort()
for wall in walls2:
    print(wall)

print((occupied - unit_locations) == walls)"""

rounds = 0
done = False
while not done:
    units.sort()
    print("\n\nRound", rounds+1)
    for i in range(size):
        for j in range(size):
            loc = (i, j)
            if loc in walls:
                print("#", end="")
            elif loc in elves:
                print("E", end="")
            elif loc in goblins:
                print("G", end="")
            else:
                print('.', end="")
        print("")
    print("\n")
    dead = set()
    for unit in units:
        if not unit.alive:
            continue
        #print(unit)
        targets = get_targets(unit.spec, units)
        if len(targets) == 0:
            done = True
            break
        if not is_in_range(unit, units):
            unit_locations -= {unit.loc}
            if target.spec == 'G':
                goblins -= {unit.loc}
            else:
                elves -= {unit.loc}
            #print("  Moving")
            move(unit, units)
            unit_locations |= {unit.loc}
            if target.spec == 'G':
                goblins |= {unit.loc}
            else:
                elves |= {unit.loc}
        if is_in_range(unit, units):
            #print("  Attack!")
            target = pick_target(unit, units)
            attack(unit, target)
            if not target.alive:
                dead |= {target}
                unit_locations -= {target.loc}
                occupied -= {target.loc}
                if target.spec == 'G':
                    goblins -= {target.loc}
                else:
                    elves -= {target.loc}
    units = list(set(units) - dead)
    set_data(occ_locs=occupied, unit_locs=unit_locations)
    if not done:
        rounds += 1

total_hp = sum([u.hp for u in units])
print(rounds, total_hp)
print("Part 1:", total_hp*rounds)
