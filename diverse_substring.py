n = int(input())
s = input()

def has_majority(t):
    counts = {}
    for ch in t:
        counts[ch] = counts.get(ch, 0) + 1
    return any(v > len(t) // 2 for v in counts.values())

if not has_majority(s):
    print("YES")
    print(s)
else:
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            print("YES")
            print(s[i:i+2])
            break
    else:
        print("NO")