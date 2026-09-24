#9-t, only when the result is less than previous n
#skip if first digit is 9
#for the rest, perform step 1 till all elements
#have been visited
import sys
n = int(input())
n = [int(x) for x in str(n)]
records = []
records.extend(n)

for i in range(len(n)):
    if len(n)==1 and 9 in n:
        print("9")
        sys.exit(0)
    if n[i] == 9 and i ==0:
        continue
    else:
        if n[i] in [1, 2, 3, 4]:
            continue
        records[i] = 9-records[i]
        if int(''.join(map(str, records))) < int(''.join(map(str, n))):
            n[i] = 9-n[i]
        else:
            records[i] = 9-records[i]
print(''.join(map(str, n)))
