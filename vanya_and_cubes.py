#input: number of cubes available
#objective stack the cubes in this way:
#top row: 1 cube
#row below: 1+2
#row below: 1+2+3
#and so on until maximum possible levels of the pyramid are achieved
#output: number of levels in the pyramid

n = int(input())
cubes_per_level = [1]
i=2
def sum_of_cubes(i):
    res=0
    for x in range(1, i+1):
        res += x
    return res
while sum(cubes_per_level) < n:
    x=sum_of_cubes(i)
    if sum(cubes_per_level) + x > n:
        break
    cubes_per_level.append(x)
    i+=1
 
# print(cubes_per_level)
print(len(cubes_per_level))