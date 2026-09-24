#print pattern like: 
#           0
#         0 1 0
#       0 1 2 1 0
#     0 1 2 3 2 1 0
#   0 1 2 3 4 3 2 1 0
# 0 1 2 3 4 5 4 3 2 1 0
#   0 1 2 3 4 3 2 1 0
#     0 1 2 3 2 1 0
#       0 1 2 1 0
#         0 1 0
#           0
#for n = 5
#where 2<=n<=9
n = int(input())
spaces = 2*n
for i in range(n+1):
    line = ""
    print(" "*spaces, end="")
    for j in range(i+1):
        line += str(j)+" "
    line = line.rstrip()
    if(i!=0):
        line += line[-2::-1]
    print(line)
    spaces-=2

spaces = 2
for i in range(n-1, -1, -1):
    line = ""
    print(" "*spaces, end="")
    for j in range(i+1):
        line += str(j)+" "
    line = line.rstrip()
    if(i!=0):
        line += line[-2::-1]
    print(line)
    spaces+=2