def solve(n, m):
    ans = (n+1)//2
    while ans%m != 0:
        ans+=1
        if ans > n:
            return -1
    return ans

n, m = list(map(int, input().split()))
print(solve(n, m))