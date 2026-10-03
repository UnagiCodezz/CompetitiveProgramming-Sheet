# the objective is, that given input like: 5 4 100 => (a, b, n); we need to perform either operation a+=b or b+=a in such a way that either a or b exceeds n and the number of iterations is minimum
# i used the following approach:
# 5>4: 4+5 = 9
# 9>5: 5+9 = 14
# 14>9: 9+14 = 23
# 23>14: 14+23 = 37
# 37>23: 23+37 = 60
# 60>37: 37+60 = 97
# 97>60: 60+97 = 157

# we stop at after iteration 7 because 157 > 100(threshold, n). therefore the output is 7
n=int(input())
res = []
all_inps = []
def solve():
    global n, all_inps, res
    for i in range(len(all_inps)):
        nums = [all_inps[i][0], all_inps[i][1]]
        thresh = all_inps[i][-1]
        # nmax = nums.index(max(nums))
        # nmin = nums.index(min(nums))
        c=0
        while(nums[0]<=thresh and nums[1] <= thresh):
            if(nums[0] >= nums[1]):
                nums[1] += nums[0]
            else:
                nums[0] += nums[1]
            c+=1
        res.append(c)


for i in range(n):
    inp = input().split()
    inp = [int(x) for x in inp]
    all_inps.append(inp)
solve()

for i in range(len(res)):
    print(res[i], end="\n")


