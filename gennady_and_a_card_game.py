#input like:
#AS
#2H 4C TH JH AD
#we need to check the second row for a pair in which either first character matches first character
#of first row OR second character matches second character of first row
#if either is true for any of the second row pairs, print YES else print NO
in_play = input()
in_play = [x for x in in_play]
in_hand = input().split()
in_hand = [x for x in in_hand]
flag=0
for i in range(len(in_hand)):
    if in_hand[i][0] == in_play[0] or in_hand[i][1] == in_play[1]:
        flag=0
        break
    else:
        flag=1
if flag==1:
    print("NO")
else:
    print("YES")