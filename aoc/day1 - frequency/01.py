current_frequency = 0
reached_frequencies = [0]

puzzle_input = []

while True:
    try:
        freq = int(input())
        puzzle_input.append(freq)
    except ValueError:
        break

print("Starting...")
done = False
while not done:
    for freq in puzzle_input:
        current_frequency += freq
        if current_frequency not in reached_frequencies:
            reached_frequencies.append(current_frequency)
            print("New frequency added!")
        else:
            done = True
            print("Found it!")
            break
    if done:
        break
    

print("Result: ", end=" ")
print(current_frequency)
