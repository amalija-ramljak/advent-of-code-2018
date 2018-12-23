# alphabetically if more than one
from collections import deque
from string import ascii_uppercase


class Step:
    def __init__(self, current, length):
        self.current = current
        self.length = length
        self.previous = list()
        self.next = list()
        self.first = True

    def __repr__(self):
        return self.current

    def __lt__(self, other):
        return self.current < other.current

class Worker:
    def __init__(self, idn):
        self.idn = idn
        self.current = ""
        self.remaining_time = 0

    def __repr__(self):
        return str(self.idn)+" -> ["+str(self.current)+"] "+str(self.remaining_time)

base_time = input("Base time: ")
workers = input("Number of workers: ")

step_count = 0
steps = dict()
while True:
    req = input()
    if req == "":
        break
    req = req.split(" ")
    current = req[7]
    previous = req[1]
    
    if current not in steps:
        length = base_time + 1 + ascii_uppercase.index(current)
        steps[current] = Step(current, length)
        step_count += 1
    if previous not in steps:
        length = base_time + 1 + ascii_uppercase.index(previous)
        steps[previous] = Step(previous, length)
        step_count += 1

    steps[current].previous.append(steps[previous])
    steps[current].first = False
    
    steps[previous].next.append(steps[current])

first = []    
for step in steps:
    if steps[step].first:
        first.append(steps[step])
first.sort()

visited = set()
next_steps = first[:]
order = []
while len(next_steps) > 0:
    step = next_steps.pop(0)
    if step in visited:
        continue
    visited |= {step}
    order.append(step)
    print(str(step) + " <- " + str(step.previous))
    for s in step.next:
        ready = True
        for p in s.previous:
            if p not in visited:
                ready = False
                break
        if ready:
            next_steps.append(s)
    next_steps.sort()

order = deque(order)
idle = deque()
working = list()
for i in range(workers):
    idle.append(Worker(i))
time = 0
done = False

finished_steps = set()
previous_step_len = len(finished_steps)
while len(finished_steps) < step_count:
    # print(end="\n\n")
    not_ready = deque()
    # print(time, end=":\n")
    # print(len(order), end=" ")
    # print(len(idle))
    while len(idle) > 0 and len(order) > 0:
        step = order.popleft()
        for p in step.previous:
            if p not in finished_steps:
                not_ready.append(step)
                break
        if step not in not_ready:
            worker = idle.popleft()
            worker.current = step
            worker.remaining_time = step.length
            working.append(worker)
    if len(not_ready) > 0:
        not_ready.reverse()
        order.extendleft(not_ready)
    # print(idle)
    # print(working)
    for worker in working:
        worker.remaining_time -= 1
        if worker.remaining_time == 0:
            idle.append(worker)
            finished_steps |= {worker.current}
    for worker in idle:
        if worker in working:
            working.pop(working.index(worker))
    # print(idle)
    # print(working)
    # print(finished_steps)
    time += 1

print(end="\n\n")
print("Base time for step: " + str(base_time))
print("Number of workers: " + str(workers))
print("Time for them all, in order: " + str(time))
