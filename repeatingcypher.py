# the input will be a string like "baabbb"
# where the first character will appear once, second will appear twice and so on
# we need to print the "decrypted string"
# that is, print each character just once
# so output is: "bab"
n = int(input())
enc_msg = input()
enc_msg = [x for x in enc_msg]
res = []
c=1
i=0
while i<n:
    x = enc_msg[i]
    res.append(x)
    i = i+c
    c+=1
for i in res:
    print(i, end="")