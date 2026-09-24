# l and b starting weights are input
#every year l weight triples, and b weight doubles
#we need to print number of years at and after which l weight will always be more than b weight

l, b = input().split()
l, b = int(l), int(b)
weight_increase = {"l":3, "b":2}

years = 0
while(l<=b):
    l = l*weight_increase["l"]
    b = b*weight_increase["b"]
    years = years+1
print(years)