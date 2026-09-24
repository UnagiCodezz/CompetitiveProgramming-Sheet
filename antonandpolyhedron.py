#print total number of slides of the particular shapes that are input

shapes = {"Tetrahedron":4,
    "Cube":6,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20
}
total_sides=0
shape_inputs = []
n = int(input())
for i in range(n):
    shape_inputs.append(input())
    total_sides=total_sides+shapes[shape_inputs[i]]
print(total_sides)