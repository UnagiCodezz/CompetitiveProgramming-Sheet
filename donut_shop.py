t = int(input())
while t > 0:
    a,b,c = map(int, input().split())
    if a< c:
        print("1 ")
    else:
        print("-1 ")
    if c < a * b:
        print(b)
    else:
        print("-1")
    t=t-1