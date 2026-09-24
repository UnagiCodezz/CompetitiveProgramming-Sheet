n, l, u = map(int, input().split())
days = list(map(int, input().split()))
candidates = []

for i in range(n):
    left = days[max(0, i - l):i]
    right = days[i + 1:min(n, i + u + 1)]
    if all(days[i] < x for x in left) and all(days[i] < x for x in right):
        candidates.append(i + 1)

print(min(candidates))


'''
if i-l < 0 and i+u > 0 and i+u < n
    if a[i] < all(a[i+1 : i+u])
        cand[a[i]] = i 



'''