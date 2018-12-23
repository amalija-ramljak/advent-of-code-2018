from day17.water_area_calc import calculate_area

x = 'x'
y = 'y'

# y, x notation
starting_spring = (0, 500)
clay = set()

while True:
    line = input()
    if line == "":
        break
    line = line.split(", ")
    first = line[0]
    second = line[1]

    coor1 = int(first[2:])
    coor1_type = first[0]
    if coor1_type == x:
        x_coor = coor1
    else:
        y_coor = coor1

    coor2_range = second[2:]  # end point included
    coor2_range = coor2_range.split("..")
    coor2_start = int(coor2_range[0])
    if len(coor2_range) == 2:
        coor2_end = int(coor2_range[1])
    else:
        coor2_end = coor2_start
    coor2_type = second[0]
    for i in range(coor2_start, coor2_end+1):
        if coor2_type == x:
            location = (y_coor, i)
        else:
            location = (i, x_coor)
        clay |= {location}

# calculation
calculate_area(clay, starting_spring)
