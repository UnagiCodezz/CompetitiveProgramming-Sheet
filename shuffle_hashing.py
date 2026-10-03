t = int(input())
cases = []

def solve(p, h):
    if len(p) > len(h):
        return 'NO'
    else:
        for i in range(len(h)-len(p)+1):
            if sorted(p) == sorted(h[i:i+len(p)]):
                return 'YES'
        return 'NO'

for i in range(t):
    p = list(input())
    h = list(input())
    cases.append((p, h))

for i in range(t):
    print(solve(cases[i][0], cases[i][1]), end='\n')
