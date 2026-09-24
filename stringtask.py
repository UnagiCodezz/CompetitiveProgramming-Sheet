#for input like "pneumonoultramicroscopicsilicovolcanoconiosis"
#print output: ".p.n.m.n.l.t.r.m.c.r.s.c.p.c.s.l.c.v.l.c.n.c.n.s.s"
inp_string = [x for x in input()]
res = ""
for x in range(len(inp_string)):
    if inp_string[x].upper() not in [ "A", "O", "Y", "E", "U", "I"]:
       res+="."+inp_string[x].lower() 


print(res)
