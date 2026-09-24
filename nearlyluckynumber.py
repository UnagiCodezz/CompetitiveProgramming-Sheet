#lucky numbers are 7 and 4
#any number made up of these is called nearly lucky if the counts of 7 + counts of 4 is also
#a lucky number.
#eg: 74 is not a nearly lucky number because one 7 and one 4, so total 2 != 4 or 7
n = input()
n = [i for i in n]
if n.count('7') + n.count('4') in [7, 4]:
   print("YES")
else:
   print("NO")