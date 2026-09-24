n = int(input())
soln = n
for i in range(1, n+1):
    soln += i*(n-i)
print(soln)
