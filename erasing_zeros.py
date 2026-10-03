#we need to get consecutive 1's without converting unnecessary 0's to 1's
#eg: in 00100010, we only need to flip middle 3 zeros to 1's, so we can strip 0's from the ends
#and just print number of zeros that are remaining
n = int(input())
tc = [input() for _ in range(n)]
for i in range(n):
    tc[i] = tc[i].strip('0')
    print(tc[i].count('0'))