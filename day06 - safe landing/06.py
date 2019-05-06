def check_infinite(coord, sides, coordinates):
    """Has an infinite area if at least one of its spots is a border one
        without a pinned coordinate to its left or right (wall orientation)"""
    return is_border(coord, sides)\
           and coord not in coordinates\
           and (\
               (coord[0]+1, coord[1]) not in coordinates and (coord[0]-1, coord[1]) not in coordinates\
               or (coord[0], coord[1]+1) not in coordinates and (coord[0], coord[1]-1) not in coordinates)


def is_border(coord, sides):
    """Border spot - alongside a wall of the matrix"""
    return coord[0] <= 0 or coord[0] >= sides["bottom"]\
       or coord[1] <= 0 or coord[1] >= sides["right"]


def calc_distance(coor1, coor2):
    """Calculates the Manhattan distance between two coordinates"""
    y = abs(coor1[0] - coor2[0])
    x = abs(coor1[1] - coor2[1])
    return x + y


coordinates = set()
coordinate_areas = dict()
sides = {
    "top" : 500,
    "bottom" : 0,
    "left" : 500,
    "right" : 0,
}

while True:
    line = input()
    if line == "":
        break
    line = line.split(", ")  # x, y
    line[1] = int(line[1])
    line[0] = int(line[0])
    coord = (line[1], line[0])
    coordinates |= set({coord})
    coordinate_areas[coord] = set({coord})

    if coord[0] < sides["top"]:  # row, so top or bottom
        sides["top"] = coord[0]
    if coord[0] > sides["bottom"]:
        sides["bottom"] = coord[0]
    if coord[1] < sides["left"]:
        sides["left"] = coord[1]
    if coord[1] > sides["right"]:
        sides["right"] = coord[1]

print("Wait for a little bit...")
finite_area_c = set()
iterations = 4
for c in coordinates:
    infinite = False
    if is_border(c, sides):
        continue  # it is a border dot and has an infinite area
    radius = 1
    while not infinite:
        previous = (c[0] - radius, c[1])  # top of the circle
        area_len = len(coordinate_areas[c])
        for i in range(iterations):
            for j in range(radius):
                if i == 0:  # y+ x+
                    current = (previous[0]+1, previous[1]+1)
                elif i == 1:  # y+ x-
                    current = (previous[0]+1, previous[1]-1)
                elif i == 2:  # y- x-
                    current = (previous[0]-1, previous[1]-1)
                else:  # y- x+
                    current = (previous[0]-1, previous[1]+1)
                distances = [calc_distance(current, coord) for coord in coordinates if coord != c]
                if radius < min(distances):
                    if check_infinite(current, sides, coordinates):
                        infinite = True
                        break
                    else:
                        coordinate_areas[c] |= {current}
                previous = current
            if infinite:
                break
        if len(coordinate_areas[c]) == area_len:  # nothing changed
            break
        radius += 1
    if not infinite:
        finite_area_c |= set({c})

area_sizes = [len(coordinate_areas[c]) for c in finite_area_c]

largest_area_size = max(area_sizes)
print("Done 1/2!")
print("Largest area: " + str(largest_area_size))

print("\nNow just wait a little bit longer...")
# pad matrix - turned out unnecessary, as expected
pad = 0
    
distance_10000 = []
for i in range(pad, sides["bottom"]-pad+1):
    for j in range(pad, sides["right"]-pad+1):
        distance = sum([calc_distance((i, j), c) for c in coordinates])
        if distance < 10000:
            distance_10000.append(distance)

region_10000 = len(distance_10000)
print("Finished completely!")
print("Region 10000: " + str(region_10000))


