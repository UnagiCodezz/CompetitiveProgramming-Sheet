# the input is n: the number of stations; and the number of people who exit the train at a station and the number of people who board the train at that same station. this input is given for n number of stations.
# we need to find the maximum number of passengers that have been in the train throughout the journey
# approach: 1) calculated difference between number of boarding passengers 
#              and number of exiting passengers for each station and stored in a list
#           2) calculated the cumulative sum of all numbers in the above list and stored
#              in a separate list;eg: if list is [1, 2, 3], cumulative list is [1, 3, 6] {[1, 1+2, 1+2+3]}
#           3) the result is the maximum value from this cumulative list
n = int(input())
passenger_matrix = []
max_psngr = []
res = []
for i in range(n):
    passenger_row = input()
    passenger_row = passenger_row.split()
    passenger_row = list(map(int, passenger_row))
    passenger_matrix.append(passenger_row)

for i in range(n):
    max_psngr.append(passenger_matrix[i][1]-passenger_matrix[i][0])

cumulative_sum = max_psngr[0]
res.append(cumulative_sum)
for i in range(1, n):
    cumulative_sum = cumulative_sum + max_psngr[i]
    res.append(cumulative_sum)
print(max(res))