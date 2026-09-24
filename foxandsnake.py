#n => number of rows
#m => number of columns
#after reaching end of row, like for first row:-
#at (0,m), we move down 2 rows then go backwards
#every point traversed will become a '#'

n, m = input().split()
n, m = int(n), int(m)
hash_position_decider = 0
snake_plane = []
def setSingleHash(i):
    global hash_position_decider
    if hash_position_decider == 0:
        snake_plane[i] = snake_plane[i][:m-1] + "#"
        hash_position_decider = 1
    else:
        snake_plane[i] = "#" + snake_plane[i][1:]
        hash_position_decider = 0
for i in range(n):
    snake_plane.append("."*m)
# print(snake_plane)
for i in range(n):
    if i % 2 == 0:
        snake_plane[i] = "#"*m
    else:
        setSingleHash(i)

for x in range(n):
    for y in range(m):
        print(snake_plane[x][y],end="")
    print()
