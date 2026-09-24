#we want to arrange heights of 'n' soldiers in a "mock" descending order
#eg: 1,2,3,4 => 4,2,3,1; that is, it only matters if max and min height is in right position
#we want to print number of swaps needed to achieve such an arrangement
#we move max towards idx 0, which will require max_idx-0 swaps
#we move min towards soldier_count-1 idx, which will require, soldier_count-1-min_idx swaps
#additionally, if min_idx occurs before max_idx, they will eventually swap with each other
#therefore, we will subtract 1, so that the swap is not counted twice
soldier_count = int(input())
heights = list(map(int, input().split()))
max_idx, min_idx = 0,0
for i in range(soldier_count):
    if heights[min_idx] >= heights[i]:
       min_idx = i
    elif heights[max_idx] < heights[i]:
       max_idx = i
#print(max_idx, min_idx)
if max_idx > min_idx:
    print(max_idx-0 + soldier_count-min_idx-2)
else:
    print(max_idx-0 + soldier_count-min_idx-1)