#objective: given 3 points X1, X2, X3, choose a middle ground point and find total distance
#that other two points have to move to reach the chosen point
#sample input: 7 1 4
#here, we choose 4 because its neither max nor min
#then 7 has to travel 3 points, and so does 1
#therefore, output=3+3=6

points = list(map(int, input().split()))
meetAt = 0
for i in points:
    if i==max(points) or i==min(points):
         continue
    else:
        meetAt = i
 
print(max(points)-meetAt + meetAt-min(points))