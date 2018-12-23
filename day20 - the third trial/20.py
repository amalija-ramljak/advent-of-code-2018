from helpers20 import find_paren_pair


def count_loop_length(line):
    pairs = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    location = []  # stack
    for el in line:
        if len(location) == 0:
            location.append(el)
            continue
        if el != pairs[location[-1]]:
            location.append(el)
        else:
            location.pop()
    return len(location)


def max_len(regex_part, depth=0):
    if '(' not in regex_part:
        if '|' not in regex_part:
            return len(regex_part), len(regex_part)
        else:
            reg = regex_part.split("|")
            length = 0
            for el in reg:
                l = count_loop_length(el) if len(el) > 1 else len(el)
                if l > length:
                    length = l
            return length

    length = []
    part_length = 0
    part_start = 0
    i = 0
    while i < len(regex_part):
        el = regex_part[i]
        if el == "(":
            # print("")
            # pad = ["." for i in range(depth)]
            # print("".join(pad) + "Part begins", part_start)
            # print("".join(pad) + "Part ends", i)
            part_length += count_loop_length(regex_part[part_start:i])
            # print("".join(pad) + "Part length", part_length)
            paren_end = find_paren_pair(regex_part[i:])
            info = max_len(regex_part[i+1:i+paren_end], depth+3)
            part_length += info[0]
            # print("".join(pad) + "New part length", part_length)
            i = paren_end + i + 1
            part_start = i
            continue
        if el == "|":
            length.append(part_length)
            part_length = 0
            i += 1
            part_start = i
            continue
        i += 1
        # print(el, end="")
        if i == len(regex_part) - 1 and regex_part[i] != ")":
            part_length += count_loop_length(regex_part[part_start:])
    length.append(part_length)

    return max(length)  # , min(length)


directions = input()[1:-1]
aoc = max_len(directions)
print("\n\nPart 1", aoc[0])
print("Part 2", aoc[1])
