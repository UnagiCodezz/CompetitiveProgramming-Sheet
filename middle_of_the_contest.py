h1, m1 = input().split(':')
h2, m2 = input().split(':')
h1, m1 = int(h1), int(m1)
h2, m2 = int(h2), int(m2)

minutes = h1*60 + h2*60 + m1 + m2
midpoint = int(minutes / 2)

h = midpoint // 60
m = midpoint - h*60

print(f"{'0'+str(h) if h<10 else h}:{'0'+str(m) if m<10 else m}")