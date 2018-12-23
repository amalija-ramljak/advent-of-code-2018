from collections import deque as dq
from helpers15 import get_manhattan_distance

gears = {
    0: {'climb', 'torch'},
    1: {'climb', 'none'},
    2: {'torch', 'none'}
}
move_time = 1
switch_gear_time = 7


def find_path_time(start, target, cave, bounds, gear='torch'):
    current = start
    time = 0
    while True:
        curr_er_lvl = cave[current[0]][current[1]][0]
        adj = get_adjacent(current, bounds)

        if target in adj:
            er_lvl = cave[target[0]][target[1]][0]
            if gear not in gears[er_lvl]:
                time += switch_gear_time
                gear = gears[curr_er_lvl] - {gear}
                gear = gear.pop()
            if gear != 'torch':
                time += switch_gear_time
            return time

        switch = []
        new = None
        time += move_time
        for a in adj:
            er_lvl = cave[a[0]][a[1]][0]
            if gear in gears[er_lvl]:
                new = a
                break
            switch.append(a)
        if new != current:
            current = new
        else:
            # smallest manhattan
            distance = [-1, -1]
            for loc in switch:
                if distance[0] == -1:
                    distance[0] = get_manhattan_distance(loc, target)
                    distance[1] = loc
                else:
                    d = get_manhattan_distance(loc, target)
                    if d < distance:
                        distance[0] = d
                        distance[1] = loc
            current = distance[1]
            time += switch_gear_time


def get_adjacent(location, bounds):
    # bounds = the bottom right coordinate
    adjacent = {
        (location[0]+1, location[1]),
        (location[0]-1, location[1]),
        (location[0], location[1]+1),
        (location[0], location[1]-1)
    }
    oob = set()
    for a in adjacent:
        if out_of_bounds(a, bounds):
            oob |= {a}
    adjacent -= oob
    adjacent = list(adjacent)
    adjacent.sort()
    return adjacent


def out_of_bounds(location, bounds):
    return location[0] < 0 or location[0] > bounds[0]\
            or location[1] < 0 or location[1] > bounds[1]
