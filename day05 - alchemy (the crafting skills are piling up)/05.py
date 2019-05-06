from string import ascii_lowercase

def reduction(polymer):
    stack = []
    for unit in polymer:
        stack.append(unit)
        length = len(stack)
        current = stack[length-1]
        previous = stack[length-2]
        if current.lower() == previous.lower() and current != previous:
            for i in range(2):
                stack.pop()
    return stack
    

polymer = list(input())
print("Length 1: " + str(len(polymer)))

reduced_1 = reduction(polymer)
print("Length 2: " + str(len(reduced_1)))

cleaned_lengths = []
for letter in ascii_lowercase:
    cleaned_poly = list(filter(lambda l: l != letter and l != letter.upper(), polymer))
    cleaned_lengths.append(len(reduction(cleaned_poly)))

min_len = min(cleaned_lengths)
index = cleaned_lengths.index(min_len)
print("Minimum length: " + str(min_len) +\
      " for " + str(ascii_lowercase[index]))
