current_frequency = 0
reached_frequencies = set()
reached_frequencies |= {current_frequency}
puzzle_input = []

while True:
    freq = input()
    if freq == "":
        break
    freq = int(freq)
    puzzle_input.append(freq)
    current_frequency += freq
    reached_frequencies |= {current_frequency}

print("Part 1:", current_frequency)

done = False
while not done:
    for freq in puzzle_input:
        current_frequency += freq
        if current_frequency not in reached_frequencies:
            reached_frequencies |= {current_frequency}
            # print("New frequency added!")
        else:
            done = True
            # print("Found it!")
            break
    if done:
        break

print("Part 2:", current_frequency)
