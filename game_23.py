#given numbers like 100(n) and 600(m), we need to find the number of operations to perform
#to convert 100 into 600
#operations: either do n*=2 or n*=3
#in this case we can do 100*2 = 200*3 = 600 so, print 2 (2 operations)
#approach:
#first reduce the given numbers, so in this case instead of multiplying in 100 to get 600
#we can multiply in 1 to get 6 (600 divided by 100)
#then we can employ a backward approach wherein we divide 6 by 3 repeatedly until we can't
# anymore and then divide by 2 repeatedly until we reach 2/2 = 1
#if 1 is reached print number of operations (which is maintained/incremented throughout)
#if 1 is not reached print -1 (that is, m cant be reached from n using the given operations)
#also, initially we check if m is divisible by n, if not we can just print(-1) there itself
n, m = map(int, input().split())
ans = 0
if m%n != 0:
    ans = -1
else:
    reduced_numerator = m//n
    while reduced_numerator % 3 == 0:
        reduced_numerator = reduced_numerator // 3
        ans+=1
    while reduced_numerator % 2 == 0:
        reduced_numerator = reduced_numerator // 2
        ans+=1
    if reduced_numerator != 1:
        ans = -1
print(ans)