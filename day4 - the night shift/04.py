from datetime import timedelta, datetime

datetime_format = "%Y-%m-%d %H:%M"
F = "falls asleep"
W = "wakes up"

sleep_times = dict()
guards = set()
puzzle_input = []
while True:
    line = input()
    if line == "":
        break
    d = line[6:11]
    t = line[12:17].split(":") # [hour, minute]
    t = t[1]
    message = line[19:]
    if message[0:5] == "Guard":
        message = message.split(" ")[1][1:]  # only guard ID
        guards |= {message}
    puzzle_input.append((d, t, message))

puzzle_input.sort()

for guard in guards:
    sleep_times[guard] = [0 for i in range(60)]

guard = ""
asleep = 0
for stamp in puzzle_input:
    if stamp[2] != F and stamp[2] != W:  # means it is an ID
        guard = stamp[2]
    elif stamp[2] == F:
        asleep = int(stamp[1])
    elif stamp[2] == W:
        awake = int(stamp[1])
        for i in range(asleep, awake):  # [asleep, awake>
            sleep_times[guard][i] += 1

most_asleep = 0  # minutes count
guard_id = ""
for guard in guards:
    asleep = sum(sleep_times[guard])
    if asleep > most_asleep:
        most_asleep = asleep
        guard_id = guard

minute = max(sleep_times[guard_id])
minute_most_asleep = sleep_times[guard_id].index(minute)
guard_id = int(guard_id)

print("Result 1: ", end="")
print(guard_id*minute_most_asleep)

most_freq_min_c = 0
guard_id = 0
for guard in guards:
    max_min_c = max(sleep_times[guard])
    if max_min_c > most_freq_min_c:
        most_freq_min_c = max_min_c
        guard_id = guard

most_freq_min = sleep_times[guard_id].index(most_freq_min_c)

print("Result 2: ", end="")
print(int(guard_id)*most_freq_min)
        
