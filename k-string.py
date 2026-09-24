# given value of k like 3
# and string like "aaabbbcccccc"
# we need to divide it into 3 same parts like abcc abcc abcc and print them out as a single string like abccabccabcc

# on the other hand if such an arrangement is not possible for the given input k, then print -1, like for eg: the string aabbccc, cannot be divided into 3 same parts, or even 2 same parts if k=2

# approach: 
# 1) first check if length of the string is divisible by k, if not then print -1
# 2) if it is divisible, create a list of all distinct characters in the string, and also a dictionary which maintains count of each character in the string
# 3) then check if count of each character is divisible by k (for eg: aaabbbcccccc, and k= 3, we can see that there are 3 a's and b's and 6 c's, all of which are divisible by k=3, therefore, can be distributed into 3 different groups as required).
k = int(input())
string = input()
ans = ""
counts = dict()
flag = 0
if len(string)%k != 0:
    ans = "-1"
else:
    distinct = list(set(string))
    for i in range(len(distinct)):
        counts[distinct[i]] = string.count(distinct[i])
    for _, val in counts.items():
        if val % k !=0:
            ans = '-1'
            flag = 1
    if flag == 0:
        for i in range(k):
            ans += ''.join([x*(string.count(x)//k) for x in distinct])
print(ans)