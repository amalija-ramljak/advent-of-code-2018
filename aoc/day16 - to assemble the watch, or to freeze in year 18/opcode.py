# types for add through assign => r, i
# types for gt and eq => ir, ri, rr


def add(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def bit_and(a, b):
    return a & b


def bit_or(a, b):
    return a | b


def assignment(a, b):
    # b is ignored
    return a


def gt(a, b):
    if a > b:
        return 1
    return 0


def eq(a, b):
    if a == b:
        return 1
    return 0


def instructions():
    instr = {
        "add": add,
        "mul": multiplication,
        "ban": bit_and,
        "bor": bit_or,
        "set": assignment,
        "gt": gt,
        "eq": eq
    }
    return instr
