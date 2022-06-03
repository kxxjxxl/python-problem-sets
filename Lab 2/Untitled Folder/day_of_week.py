y = int(input("Enter the 4-digit year: "))
m = int(input("Enter the month as an integer: "))
d = int(input("Enter the day as an integer: "))

if m == 1 or m == 2:
    y = y - 1

y = str(y)

p = y[2] + y[3]
q = y[0] + y[1]

r = ((m + 9) % 12) + 1
s = ((13 * r) - 1) // 5
t = int(p) // 4
u = int(q) // 4
v = d + int(p) + s + t + u + (5 * int(q))
w = int(v % 7)

if w == 0:
    day = "Sunday"
elif w == 1:
    day = "Monday"
elif w == 2:
    day = "Tuesday"
elif w == 3:
    day = "Wednesday"
elif w == 4:
    day = "Thursday"
elif w == 5:
    day = "Friday"
elif w == 6:
    day = "Saturday"

if m == 1:
    month = "January"
elif m == 2:
    month = "Feburary"
elif m == 3:
    month = "March"
elif m == 4:
    month = "April"
elif m == 5:
    month = "May"
elif m == 6:
    month = "June"
elif m == 7:
    month = "July"
elif m == 8:
    month = "August"
elif m == 9:
    month = "September"
elif m == 10:
    month = "October"
elif m == 11:
    month = "November"
elif m == 12:
    month = "December"

y = int(y)
if m == 1 or m == 2:
    year = y + 1
else:
    year = y

print("{} {}, {} is a {}".format(month, d, year, day))