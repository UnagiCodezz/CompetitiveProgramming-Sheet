'''
00000     00000
00001     00000
00000  => 00100 |<= Beautiful Matrix
00000     00000
00000     00000
'''
def findIdxOfOne(matrix):
    for i, row in enumerate(matrix):
        if 1 in row:
            return [i, row.index(1)] 
matrix= []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
 
oneidxs = findIdxOfOne(matrix)
print(f"{abs(oneidxs[0]-2) + abs(oneidxs[1]-2)}")