# 300 x 300 dimension
# index + 1 -> x, y
# rack ID = x + 10
# power level = rack ID * y
# power level += grid serial
# power level *= rack ID
# power level = (power level % 1000) / 100
# power level -= 5
import numpy as np

def calc_power_level(x, y, grid):
    return int(((((x+10)*y + grid)*(x+10))%1000) / 100) - 5

dimension = 300
grid = int(input("Grid serial number: "))
part = input("Part of AoC11 (1, 2): ")
cells = [[calc_power_level(j, i, grid) for j in range(1, dimension+1)] for i in range(1, dimension+1)]
cells = np.array(cells)

# represents the top left cell
group_x = 0
group_y = 0
group_size = 3 if part == "1" else 1
size_range = (group_size, 4 if group_size == 3 else dimension+1)

total_power = cells[0, 0]

for size in range(size_range[0], size_range[1]):
    for i in range(dimension-size+1):
        for j in range(dimension-size+1):
            new_power = cells[i:i+size, j:j+size].sum()
            if new_power > total_power:
                total_power = new_power
                # plus one because counting starts at 1
                group_x = j + 1
                group_y = i + 1
                group_size = size


print(str(group_x) + "," + str(group_y) + "," + str(group_size))
print(total_power)
