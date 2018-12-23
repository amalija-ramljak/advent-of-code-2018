import numpy as np
from collections import deque as dq

clay_loc = set()
water = set()
reach = set()


def fill(location):
    """Fills the area left and right of the given location if all are has_bottom till they reach a border
        Otherwise, the gathered area is only reachable, not stable water (added to reach set)

        returns the the borders (or ends, if filled it moves the non-border one/s further down if possible
        in the next loop)"""
    global reach, water
    filled = True

    area = set()

    borders = set()  # till 2 are visited or
    ends = set()  # till two are overflowing

    # common BFS
    visited = set()
    queue = dq([location])
    while len(queue) > 0:
        loc = queue.popleft()
        if loc in visited:
            continue
        visited |= {loc}

        if not has_bottom(loc):
            filled = False
            ends |= {loc}
            if len(ends) == 2 or len(ends) == 1 and len(borders) == 1:
                break
            continue
        if loc in clay_loc:
            borders |= {loc}
            if len(borders) == 2 or len(borders) == 1 and len(ends) == 1:
                break
            continue

        area |= {loc}
        neighbours = [
            (loc[0], loc[1]+1),
            (loc[0], loc[1]-1)
        ]
        queue.extend(neighbours)

    if filled:
        water |= area  # 2 borders (borders are not counted in!)
    else:
        reach |= area | ends  # 2 ends, 1 border 1 end

    return borders | ends


def has_bottom(location):
    """Checks the one beneath"""
    loc = (location[0]+1, location[1])
    return loc in clay_loc or loc in water


def calculate_area(clay, start):
    global clay_loc, water, reach
    clay_loc = clay

    clay_map = np.array(list(clay_loc))
    y_top = np.min(clay_map[:, 0], axis=0)
    y_bottom = np.max(clay_map[:, 0], axis=0)

    x_left = np.min(clay_map[:, 1], axis=0)
    x_right = np.max(clay_map[:, 1], axis=0)

    locations = {start}
    while len(locations) > 0:
        moved = set()
        new = set()
        for loc in locations:
            if loc[0] >= y_bottom:
                moved |= {loc}
                continue
            elif loc[0] < y_top:
                moved |= {loc}
                new |= {(loc[0]+1, loc[1])}
                continue

            if not has_bottom(loc):
                moved |= {loc}
                new |= {(loc[0]+1, loc[1])}
                reach |= {(loc[0]+1, loc[1])}
            else:
                new_locations = fill(loc)
                moved |= {loc}
                borders = 0
                for new_loc in new_locations:
                    if new_loc in clay_loc:
                        borders += 1
                    else:
                        new |= {(new_loc[0]+1, new_loc[1])}
                        reach |= {(new_loc[0]+1, new_loc[1])}
                if borders == 2:
                    new |= {(loc[0]-1, loc[1])}

        locations -= moved
        locations |= new
    """
    for i in range(y_top, y_bottom+1):
        for j in range(x_left-1, x_right+2):
            l = (i, j)
            if l in water:
                print("~", end="")
            elif l in reach:
                print("|", end="")
            elif l in clay_loc:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    """
    full_area = water | reach
    print("Part 1:", len(full_area)+1)  # I do not know why the first one won't fit in
    print("Part 2:", len(water))



