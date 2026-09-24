t = int(input())
r = []
for i in range(t):
    x = int(input())
    y = list(map(int, str((input()))))
    r.append((x,y))

counts = []
for j in r:
    if 1 not in j[1]:
        counts.append(j[0])
        continue
    cnt = []
    i=0
    while i<j[0]:
        if j[1][i] == 1:
            cnt.append(2*max(len(j[1][0 : i+1]), len(j[1][i:j[0]])))
        i+=1
    counts.append(max(cnt))

for k in counts:
    print(k, end='\n')