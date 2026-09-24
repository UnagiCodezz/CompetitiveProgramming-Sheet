#given a string like 3+2+1, we have to arrange the numeric terms in ascending order and print:-
#1+2+3 => <answer>

expr = input()
terms = [int(x) for x in expr if x not in ['+']]
terms.sort()
output = ""
for i in terms:
    output = output + str(i) + "+"
print(output[0:len(output)-1])

