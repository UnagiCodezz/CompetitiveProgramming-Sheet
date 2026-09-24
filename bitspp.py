n = int(input())
x=0
op=""
for i in range(n):
    op = input()
    if(op in ["++X", "X++"]): x= x+1
    else: x=x-1
print(x)