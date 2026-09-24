#k => cost of first banana;  w => amount we have;  n => number of bananas we want
#(made mistake in this code, w was supposed to be number of bananas, and n-amount we have
# but thats fine...)
k,w,n = input().split()
k, w, n = int(k), int(w), int(n)
prices_per_banana = [k*i for i in range(1, n+1)]

if sum(prices_per_banana) > w:
    print(sum(prices_per_banana)-w)
else:
    print('0')