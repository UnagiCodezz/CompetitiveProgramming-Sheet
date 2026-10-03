t = int(input())
cases = []
def solve(data):
    size = data[0]
    string = data[1]
    l, r = 0, size-1
    while l<r+1:
        if set([chr(ord(string[l])+1)] if string[l]=='a' else [chr(ord(string[l])+1), chr(ord(string[l])-1)]) & set([chr(ord(string[r])-1)] if string[r]=='z' else [chr(ord(string[r])+1), chr(ord(string[r])-1)]):
            l+=1
            r-=1
        else:
            return 'NO'
    return 'YES'


for i in range(t):
    x = int(input())
    y = input()
    cases.append((x, y))


for i in range(t):
    print(solve(cases[i]), end='\n')
