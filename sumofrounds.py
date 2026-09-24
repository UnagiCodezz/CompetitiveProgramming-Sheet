#a round number is: 5000, 6000, 7, etc.
#non round: 550, 101, etc.
#objective: convert number like 5865 to rounds number parts: 5000, 800, 60, 5.
#skip 0's: eg: 5058=>5000, 50, 8

tc = int(input())
nums = []
results = dict()
for i in range(tc):
    nums.append(int(input()))
for i in range(len(nums)):
    x = str(nums[i])
    res_per_tc = []
    for j in range(len(x)):
        if(x[j] != '0'):
            roundnum = x[j]+''.join(['0' for y in range(len(x)-j-1)])
            res_per_tc.append(roundnum)
    results[i+1]=res_per_tc

# print(results)
for _, val in results.items():
    print(len(val))
    for j in val:
        print(j, end=" ")
    print()
    