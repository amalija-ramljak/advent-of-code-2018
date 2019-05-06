def get_manhattan(loc1, loc2):
    return sum([abs(a-b) for a, b in zip(loc1, loc2)])


stars = []

while True:
    line = input()
    if line == "":
        break
    line = line.split(",")
    for i, el in enumerate(line):
        line[i] = int(el)
    line = tuple(line)
    stars.append(line)

constellations = dict()
count = 0
for star in stars:
    cons = []
    for con in constellations:
        for con_star in constellations[con]:
            if get_manhattan(star, con_star) <= 3:
                cons.append(con)
                break
    if len(cons) == 1:
        constellations[cons[0]] |= {star}
    elif len(cons) == 0:
        constellations[count] = {star}
        count += 1
    elif len(cons) > 1:
        new_const = {star}
        for con in cons:
            for con_star in constellations[con]:
                new_const |= {con_star}
            constellations.pop(con)
        constellations[count] = new_const
        count += 1

print(len(constellations))
                
