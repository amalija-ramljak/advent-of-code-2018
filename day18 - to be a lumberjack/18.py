# symbols
tree_symbol = '|'
lumber_symbol = '#'
open_symbol = '.'
num_of_min = 1000000000


def get_adjacent(location, all_locations):
    adjacent = {
        (location[0]+1, location[1]),
        (location[0]-1, location[1]),
        (location[0], location[1]+1),
        (location[0], location[1]-1),
        (location[0]+1, location[1]+1),
        (location[0]+1, location[1]-1),
        (location[0]-1, location[1]+1),
        (location[0]-1, location[1]-1),
    }
    out_of_bounds = set()
    for a in adjacent:
        if a not in all_locations:
            out_of_bounds |= {a}
    adjacent -= out_of_bounds
    return adjacent


def print_area(trees, open, lumber, size):
    arena = [['.' for j in range(size[1])] for i in range(size[0])]
    for location in trees:
        arena[location[0]][location[1]] = tree_symbol
    for location in lumber:
        arena[location[0]][location[1]] = lumber_symbol
    for location in open:
        arena[location[0]][location[1]] = open_symbol

    print("\n".join(["".join(line) for line in arena]))
    print("\n")


trees = set()
lumber = set()
open = set()
size = 0

i = -1
j = -1
while True:
    line = input()
    if line == "":
        break
    i += 1
    j = -1
    for el in line:
        j += 1
        location = (i, j)
        if el == tree_symbol:
            trees |= {location}
        elif el == lumber_symbol:
            lumber |= {location}
        else:
            open |= {location}

size = (i+1, j+1)

resources = []
repeated = []
first_repeated = 0
for minute in range(num_of_min):
    new_trees = set()
    new_lumber = set()
    new_open = set()
    print_area(trees, open, lumber, size)
    combo = (trees, lumber)
    repetition = False
    if combo in resources:
        repetition = True
        #print("Ayy repetition", minute)
    else:
        resources.append(combo)
    found = False
    if repetition:
        if combo in repeated:
            found = True
            break
        else:
            repeated.append(combo)
            if len(repeated) == 1:
                first_repeated = minute

    #print_area(trees, open, lumber, size)
    #print("\n\n")
    #print(minute+1)
    for i in range(size[0]):
        for j in range(size[1]):
            current = (i, j)
            adjacent = get_adjacent(current, trees | lumber | open)
            if current in trees:
                lumber_c = 0
                for a in adjacent:
                    if a in lumber:
                        lumber_c += 1
                if lumber_c > 2:
                    new_lumber |= {current}
                else:
                    new_trees |= {current}
            elif current in lumber:
                lumber_c = 0
                tree_c = 0
                for a in adjacent:
                    if a in lumber:
                        lumber_c += 1
                    elif a in trees:
                        tree_c += 1
                if tree_c > 0 and lumber_c > 0:
                    new_lumber |= {current}
                else:
                    new_open |= {current}
            elif current in open:
                tree_c = 0
                for a in adjacent:
                    if a in trees:
                        tree_c += 1
                if tree_c > 2:
                    new_trees |= {current}
                else:
                    new_open |= {current}
    trees = new_trees
    lumber = new_lumber
    open = new_open
    if minute == 9:
        print("Part 1:", len(trees)*len(lumber))


print_area(trees, open, lumber, size)

comparison_mod = num_of_min % len(repeated)
res_1kkk = 0
rep_min = first_repeated
for rep in repeated:
    if rep_min % len(repeated) == comparison_mod:
        res_1kkk = len(rep[0])*len(rep[1])
        break
    rep_min += 1
print("Part 2:", res_1kkk)
