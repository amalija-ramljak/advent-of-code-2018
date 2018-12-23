# header - two numbers
#    - child nodes
#    - metadata entries
# child_node*
# metadata_entry+

import sys
from collections import deque

tree = None

def node():
    c = tree.popleft()
    m = tree.popleft()
    ms = 0
    children = []
    for i in range(c):
        children.append(node())
    meta = [tree.popleft() for i in range(m)]
    if c == 0:
        ms = sum(meta)
    else:
        for num in meta:
            if num <= len(children):
                ms += children[num-1]
    return ms


sys.setrecursionlimit(1000)
tree = input().split(" ")
head = deque()
for num in tree:
    head.append(int(num))
tree = head

meta_sum = node()
print(meta_sum)
