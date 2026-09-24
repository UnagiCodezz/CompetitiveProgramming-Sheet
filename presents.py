#suppose there are 4 friends, 2 3 4 1
#2 gifts 3, 3 gifts 4, 4 gifts 1, 1 gifts 2
#so if we have 2 3 4 1, we can see that 2 gifts 3, so the 3rd position number that is 4, should come first, and so on
n = int(input())
friends = list(map(int, input().split()))
result = [0 for i in range(n)]
for i in range(n):
   position = friends[i]
   result[position-1]= i+1
ans = ""
for i in result:
    ans = ans+" "+str(i)
print(ans.strip())