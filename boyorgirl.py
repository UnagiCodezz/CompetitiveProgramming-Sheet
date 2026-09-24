#if input string has odd number of distinct characters, print "IGNORE HIM!"
#else print "CHAT WITH HER!"
name = input()
name = [x for x in name]
 
char_count = dict()
distinct_sum = 0
 
for i in range(len(name)):
    if name[i] in char_count:
        char_count[name[i]] = char_count[name[i]]+1
    else:
        char_count[name[i]] = 1
 
distinct_count = len(char_count)
if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")