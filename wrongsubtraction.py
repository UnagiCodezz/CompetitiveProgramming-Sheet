#subtract like this, if last digit is 0, delete it, else subtract one from it
#eg: 512 4: 511, 510, 51, 50=>ans. (4 is number of subtractions to perform)
num, itn = input().split()
num, itn = [x for x in num], int(itn)

for i in range(itn):
    if num[-1] == '0':
        del num[-1]
    else:
        x = int(num[-1])
        del num[-1]
        num.append(str(x-1))
for i in num:
    print(i, end="")