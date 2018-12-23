def find_paren_pair(regex):
    """Receives a string or list that comes after the ( whose pair is sought"""
    paren_count = 0  # the one missing from the str/lst
    for i, el in enumerate(regex):
        if el == "(":
            paren_count += 1
        elif el == ")":
            paren_count -= 1
        if paren_count == 0:
            return i
