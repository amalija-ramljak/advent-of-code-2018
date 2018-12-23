class LinkedNode:
    def __init__(self, value, previous=None, following=None):
        self.value = value
        self.previous = previous
        self.next = following


players = int(input("Players: "))
marbles = int(input("Marble count: "))  # starts with 0!

marble_count = 1  # number 0 is default
current = LinkedNode(value=0)  # clockwise/counterclockwise - mod length
current.next = current
current.previous = current
scores = [0 for i in range(players)]

while marble_count <= marbles:
    for i in range(players):
        #print(circle, end="\n\n")
        #print("New marble: " + str(marble_count))
        if marble_count % 23 != 0:
            new = LinkedNode(value=marble_count)
            pre_marble = current.next
            post_marble = current.next.next
            new.previous = pre_marble
            new.next = post_marble
            pre_marble.next = new
            post_marble.previous = new
            current = new
        else:
            scores[i] += marble_count
            removed = current
            for j in range(7):
                removed = removed.previous
            # print(removed.value)
            pre_marble = removed.previous
            post_marble = removed.next
            pre_marble.next = post_marble
            post_marble.previous = pre_marble
            scores[i] += removed.value
            current = post_marble
        marble_count += 1
        #print("Player " + str(i) + " - marble at " + str(current_marble[0]))
        if marble_count > marbles:
            #print(circle)
            break

print("Max score: " + str(max(scores)))
