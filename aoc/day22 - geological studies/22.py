from helpers22 import find_path_time

cave = []

depth = int(input().split(" ")[1])

target = input().split(" ")[1].split(",")
target = (int(target[1]), int(target[0]))  # y, x

# this is the minimal rectangle
risk_level = 0
for i in range(target[0] + 11):
    row = []
    for j in range(target[1] + 11):
        if i == 0 and j == 0 or i == target[0] and j == target[1]:
            geo_index = 0
        elif i == 0:
            geo_index = j * 16807
        elif j == 0:
            geo_index = i * 48271
        else:
            geo_index = cave[i-1][j][1] * row[j-1][1]

        erosion = (geo_index + depth) % 20183
        erosion = (erosion % 3, erosion)
        if i <= target[0] and j <= target[1]:
            risk_level += erosion[0]
        row.append(erosion)
    cave.append(row)

print("Part 1", risk_level)

location = (0, 0)  # y, x, torch, rocky area
bounds = target[0] + 10, target[1] + 10
shortest_path = find_path_time(location, target, cave, bounds)
print(shortest_path)
