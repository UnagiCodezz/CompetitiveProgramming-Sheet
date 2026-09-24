tc = int(input())
res =[]
for i in range(tc):
    n = int(input())
    students = list(map(int, input().split()))
    students.sort()
    res.append(abs(students[n] - students[n-1]))

for x in res:
    print(x, end="\n")