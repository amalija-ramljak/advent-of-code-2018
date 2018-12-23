import numpy as np
from matplotlib import pyplot as plt

def calc_sides(light_x, light_y, sides):
    if light_x < sides["left"]:
        sides["left"] = light_x
    elif light_x > sides["right"]:
        sides["right"] = light_x
    if light_y < sides["top"]:
        sides["top"] = light_y
    elif light_y > sides["bottom"]:
        sides["bottom"] = light_y

sides = {
    "top" : 0,
    "bottom": 0,
    "left" : 0,
    "right": 0,
}
lights = []
velocities = []
print("Let's read the input!")
while True:
    line = input()
    if line == "":
        break
    # x, y pairs (column, row)
    light_pos = line[10:24].split(",")
    light_vel = line[36:len(line)-1].split(",")
    for i in range(2):
        light_pos[i] = int(light_pos[i].strip())
        light_vel[i] = int(light_vel[i].strip())

    lights.append(light_pos)
    velocities.append(light_vel)
    # side calculation
    if len(lights) == 1:
        # y
        sides["top"] = light_pos[1]
        sides["bottom"] = light_pos[1]
        # x
        sides["left"] = light_pos[0]
        sides["right"] = light_pos[0]
    else:
        calc_sides(light_pos[0], light_pos[1], sides)
        
print("Input saved! Starting check...")
lights = np.array(lights, dtype=np.float64)
velocities = np.array(velocities, dtype=np.float64)
second = 0
area = (sides["bottom"]-sides["top"])*(sides["right"]-sides["left"])
seen = False
while not seen:
    second += 1
    new_lights = lights + velocities
    min_vals = np.amin(new_lights, axis=0)
    max_vals = np.amax(new_lights, axis=0)
    new_area = (max_vals[0]-min_vals[0])*(max_vals[1]-min_vals[1])
    if new_area < area:
        area = new_area
        lights = new_lights
    else:
        second -= 1
        seen = True

x = lights[:, 0]
y = lights[:, 1]

print("Appeared on second: " + str(second))
plt.scatter(x, y)
plt.show()
