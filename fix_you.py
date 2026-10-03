# a conveyor belt matrix is input like this:
# RDDDDDRRR
# RRDDRRDDD
# RRDRDRRDR
# DDDDRDDRR
# DRRDRDDDR
# DDRDRRDDC
# we want to transport luggage from top left to bottom right
#conveyor belt is "functional" if the last row is all R's and last column is all D's
#therefore, we need to print number of R's to D's and D's to R's that we will have to change
#to make the conveyor belt "functional"
tc = int(input())
test_cases = []
for _ in range(tc):
    n, m = input().split()
    n,m = int(n), int(m)
    grid = []
    for i in range (n):
        row = [x for x in input()]
        grid.append(row)
    test_cases.append(grid)

for i in range(len(test_cases)):
    n, m, grid = len(test_cases[i]), len(test_cases[i][0]), test_cases[i]
    changes=0
    for x in range(n-1):
        if grid[x][m-1] == 'R':
            changes+=1
    for y in range(m-1):
        if grid[n-1][y] == 'D':
            changes+=1
    print(changes)
