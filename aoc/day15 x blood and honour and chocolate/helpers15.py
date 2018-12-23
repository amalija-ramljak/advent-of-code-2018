from collections import deque as dq

unit_types = {'G', 'E'}
occupied = set()
walls = set()
unit_locations = set()
size = 0


def set_data(wall_locs=None, occ_locs=None, unit_locs=None, size=0):
    set_walls(wall_locs)
    set_occupied(occ_locs)
    set_unit_locations(unit_locs)
    set_size(size)


def set_size(side):
    global size
    if side == 0:
        return
    size = side


def set_walls(wall_loc):
    global walls
    if wall_loc is None:
        return
    walls = wall_loc


def set_occupied(occ):
    global occupied
    if occ is None:
        return
    occupied = occ


def set_unit_locations(unit_locs):
    global unit_locations
    if unit_locs is None:
        return
    unit_locations = unit_locs


def get_targets(species, units):
    return [unit for unit in units if unit.spec != species]


def is_in_range(unit, units):
    target_adjacent = set()
    targets = get_targets(unit.spec, units)
    for t in targets:
        target_adjacent |= get_all_adjacent(t.loc)
    return unit.loc in target_adjacent


def move(unit, units):
    targets = get_targets(unit.spec, units)
    #print("  I got my targets", targets)
    reachable = get_reachable_targets(unit, targets)  # locations adjacent to targets!
    if len(reachable) == 0:
        return
    #print("  Looking for the nearest reachable t.adj", reachable)
    nearest = get_nearest(unit.loc, reachable)  # closest reachable to unit.loc
    #print("  Got my nearest adjacent", nearest)
    if nearest == (-1, -1):
        return
    # move 1 step to the nearest
    unit_open_adjacent = get_open_adjacent(unit.loc)
    #print("  Got my open spots", unit_open_adjacent)
    if len(unit_open_adjacent) == 0:
        return
    if nearest not in set(unit_open_adjacent):
        nearest = get_nearest(nearest, unit_open_adjacent)  # from unit adjacent to target location
        #print("  This open spot is where I go", nearest)
    unit.loc = nearest
    #print("  My new loc!", unit.loc)


def attack(unit, target):
    target.hp -= unit.atk
    if target.hp <= 0:
        target.die()


def pick_target(unit, units):
    targets = get_targets(unit.spec, units)
    unit_all_adjacent = get_all_adjacent(unit.loc)
    viable = [t for t in targets if t.loc in unit_all_adjacent]
    return min_health_sorted(viable)


def min_health_sorted(units):
    min_hp = units[0].hp
    min_hp_unit = [units[0]]
    for unit in units:
        if unit.hp < min_hp:
            min_hp_unit = [unit]
            min_hp = unit.hp
        elif unit.hp == min_hp:
            min_hp_unit.append(unit)
    min_hp_unit.sort()
    return min_hp_unit[0]


def get_nearest(location, locations):
    # location that is nearest and located at the most top leftmost position of them
    #print("  Let's find the closest from the list", location, locations)
    locations = list(locations)
    locations.sort()
    distances = []
    for loc in locations:
        #print("    Checking", loc)
        distance = get_obstacled_distance(loc, location)
        #print("      Distance is", distance)
        if distance > 0:
            distances.append([distance, loc])
    if len(distances) == 0:
        return -1, -1
    distances.sort()
    #distances = np.array(distances)
    #min_distance = distances[np.argmin(distances[:, 0], axis=0)]
    return distances[0][1]


def get_difference(coordinate_1, coordinate_2):
    return abs(coordinate_1 - coordinate_2)


# not sure if necessary
def get_manhattan_distance(location_1, location_2):
    return abs(location_1[0]-location_2[0]) + abs(location_1[1]-location_2[1])


def get_obstacled_distance(location_1, location_2):
    visited = set()
    #print("      So, check", location_1)
    # the numbers are not important, only order matters
    queue = dq([(0, location_1)])
    while len(queue) > 0:
        #print("      Queue", queue)
        part = queue.popleft()
        #print("        Next to check:", part[1])
        if part[1] in visited:
            continue
        visited |= {part[1]}
        if part[1] == location_2:
            return part[0]  # first appearance is smallest distance
        adjacent = get_all_adjacent(part[1])
        for location in adjacent:
            if location not in walls:
                queue.append((part[0]+1, location))
    return -1


def get_reachable_targets(unit, targets):
    # returns their open adjacent reachable locations, actually
    reachable_area = get_reachable_area(unit)
    #print("  Reachable area", reachable_area)
    target_open_adjacent = set()
    for t in targets:
        target_open_adjacent |= set(get_open_adjacent(t.loc))
    viable = set([location for location in target_open_adjacent if location in reachable_area])
    return viable


def get_reachable_area(unit):
    # everything that is not a wall or unit
    #print("  Reachable area calculation")
    reachable_area = {unit.loc}
    visited = set()
    queue = dq([unit.loc])
    while len(queue) > 0:
        #print(queue)
        location = queue.popleft()
        if location in visited:
            continue
        visited |= {location}
        reachable_area |= {location}
        queue.extend(get_open_adjacent(location))
    return reachable_area


def get_open_adjacent(location):
    # the positions around a location that is not occupied
    adjacent = get_all_adjacent(location)
    return [a for a in adjacent if a not in walls and a not in unit_locations]


def get_all_adjacent(location):
    adjacent = set()
    if location[0] > 0:
        adjacent |= {(location[0]-1, location[1])}
    if location[1] > 0:
        adjacent |= {(location[0], location[1]-1)}
    if location[0] < size - 1:
        adjacent |= {(location[0]+1, location[1])}
    if location[1] < size - 1:
        adjacent |= {(location[0], location[1]+1)}
    return adjacent
