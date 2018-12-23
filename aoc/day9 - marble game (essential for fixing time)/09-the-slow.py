players = int(input("Players: "))
marbles = int(input("Marble count: "))  # starts with 0!

marble_count = 1  # number 0 is default
circle = [0]  # clockwise/counterclockwise - mod length
scores = [0 for i in range(players)]

current_marble = (0, 0)  # index, number
while marble_count <= marbles:
    for i in range(players):
        #print(circle, end="\n\n")
        #print("New marble: " + str(marble_count))
        if marble_count == 1:
            circle.append(1)
            current_marble = (1, 1)
        elif marble_count % 23 != 0:
            placement = (current_marble[0] + 2) % len(circle)
            #print("Placement: " + str(placement))
            if placement == 0:
                placement = len(circle)
            circle.insert(placement, marble_count)
            current_marble = (placement, marble_count)
        else:
            removed_index = (current_marble[0]-7)%len(circle)
            scores[i] += marble_count + circle[removed_index]
            circle.pop(removed_index)
            new_current_index = removed_index
            current_marble = (new_current_index, circle[new_current_index])
        marble_count += 1
        #print("Player " + str(i) + " - marble at " + str(current_marble[0]))
        if marble_count > marbles:
            #print(circle)
            break

print("Max score: " + str(max(scores)))
