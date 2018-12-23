def get_manhattan(loc1, loc2):
    manhattan = 0
    for a, b in zip(loc1, loc2):
        manhattan += abs(a-b)
    return manhattan


def get_strongest(bots):
    op = None
    for bot in bots:
        if op is None:
            op = bot
            continue
        if bot[1] > op[1]:
            op = bot
    return op


def get_in_strongest_range(bots):
    op = get_strongest(bots)  # pos(x,y,z), radius
    in_range = []
    for bot in bots:
        d = get_manhattan(op[0], bot[0])
        if d <= op[1]:
            in_range.append(bot)
    return in_range


def calculate_max_bounds(bots):
    x = 0
    y = 0
    z = 0
    for bot in bots:
        pos = bot[0]
        x = pos[0] if pos[0] > x else x
        y = pos[1] if pos[1] > y else y
        z = pos[2] if pos[2] > z else z
    return x, y, z

def calculate_bounds(bots):
    maximum = calculate_max_bounds(bots)
    x, y, z = maximum
    for bot in bots:
        pos = bot[0]
        x = pos[0] if pos[0] < x else x
        y = pos[1] if pos[1] < y else y
        z = pos[2] if pos[2] < z else z
    return maximum, (x, y, z)


def get_in_most_bots_range(bots, self_loc=(0, 0, 0)):
    bounds = calculate_bounds(bots)
    min_b = bounds[1]
    max_b = bounds[0]
    most_surr = (0, 0, 0), 0
    for i in range(min_b[0], max_b[0]+1):
        for j in range(min_b[1], max_b[1]+1):
            for k in range(min_b[2], max_b[2]+1):
                surround = 0
                for bot in bots:
                    if get_manhattan(bot[0], (i, j, k)) <= bot[1]:
                        surround += 1
                if surround > most_surr[1]:
                    most_surr = (i, j, k), surround
                    #print("New most bots!")
                elif surround == most_surr[1]:
                    #print("Find the closer one!")
                    new_d = get_manhattan(self_loc, (i, j, k))
                    curr_d = get_manhattan(self_loc, most_surr[0])
                    if curr_d > new_d:
                        most_surr = (i, j, k), surround
    return most_surr


bots = []
while True:
    line = input()
    if line == "":
        break
    line = line[5:].split(">, r=")
    radius = int(line[1])
    pos = line[0].split(",")  # x, y, z
    for i, el in enumerate(pos):
        pos[i] = int(el)
    bots.append((pos, radius))

in_range = get_in_strongest_range(bots)
print("Part 1:", len(in_range))

most_surrounded = get_in_most_bots_range(bots)
distance = get_manhattan((0, 0, 0), most_surrounded[0])
print("Part 2:", distance)
