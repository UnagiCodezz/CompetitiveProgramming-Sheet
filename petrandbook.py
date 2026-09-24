book_len = int(input())
pages_per_day = list(map(int, input().split()))

day = 0

while book_len > 0:
    book_len -= pages_per_day[day]
    day += 1
    if day == 7 and book_len > 0:
        day = 0
print(day)
