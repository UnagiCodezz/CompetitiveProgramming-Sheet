import math
from collections import deque
tc_cnt = int(input())
tc = []
res = []
choices = []
def solve(x):
    num_list = deque(range(1, x + 1))
    local_choices = []
    while len(num_list) > 1:
        a = num_list.pop() 
        b = num_list.pop()
        local_choices.append((a, b))
        num_list.append(math.ceil((a + b) / 2))
    res.append(num_list[0])
    choices.append(local_choices)


for _ in range(tc_cnt):
    tc.append(int(input()))

for x in tc:
    solve(x)

for i in range(tc_cnt):
    print(res[i])
    for pair in choices[i]:
        print(f"{pair[0]} {pair[1]}")
