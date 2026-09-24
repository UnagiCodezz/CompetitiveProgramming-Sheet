n = int(input())
f=0
ans = []
while n > 0:
    if n%7 <= n%4:
        n-=7
        ans.append(7)
    elif n%7 > n%4:
        n-=4
        ans.append(4)
    if n < 0:
        f=1
        break
if f==1:
    print(-1)
else:
    print(int(''.join(map(str, sorted(ans)))))