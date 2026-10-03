#objective: find minimum number of toasts for all members of party
#input: n, k, l, c, d, p, nl, np
#n->number of people
#k->number of bottles; l->millilitres per bottle
#c-> number of limes; d->slices per lime
#p->grams of salt available
#nl->litres of drinks NEEDED
#np->grams of salt NEEDED
#to calculate: (k*l)/nl=>total litres/needed litres
#              (c*d)=>total SLICES of limes
#              (p/np)=>total salt/needed salt
#since everyone has to make toast, find MINIMUM OF ABOVE RESULTS AND DIVIDE BY n
# therefore, min((k*l//nl), (c*d), (p//np))//n
party = input()
party =list(map(int, party.split()))
drinks = (party[1]*party[2])//party[-2]
lime=party[3]*party[4]
salt = party[-3]//party[-1]
 
minimum = min(drinks, lime, salt)
toasts = minimum//party[0]
print(toasts)