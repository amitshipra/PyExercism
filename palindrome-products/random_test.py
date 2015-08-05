__author__ = 'dias'

import random
import collections

dq = collections.deque()

for x in range(1, 10):
    dq.append(random.randint(1, x))

print(dq)

left,right = dq.popleft(), dq.pop()

print(left, right)

print(dq)
