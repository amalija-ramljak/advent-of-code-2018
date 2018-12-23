count_2 = 0
count_3 = 0

puzzle_input = []
while True:
    pi = input()
    if pi == "":
        break
    puzzle_input.append(pi)
    pi_set = set(pi)
    twos = 0
    threes = 0
    for l in pi_set:
        if pi.count(l) == 2 and twos == 0:
            twos = 1
        elif pi.count(l) == 3 and threes == 0:
            threes = 1
        if twos == 1 and threes == 1:
            break
    if twos == 1:
        count_2 += 1
    if threes == 1:
        count_3 += 1

print("Checksum: " + str(count_2*count_3))

length = len(puzzle_input)
c = 0
match = []
done = False
for box in puzzle_input:
    for box2 in puzzle_input:
        if box == box2:
            pass
        else:
            difference = [i for i, j in zip(box, box2) if i != j]
            if len(difference) == 1:
                x = list(box)
                x.pop(box.index(difference[0]))
                match = x
                done = True  # found em
                break
    if done:
        break

print("Matching: ", end="")
print("".join(match))
print(len(puzzle_input[0]), end=" -> ")
print(len(match))
