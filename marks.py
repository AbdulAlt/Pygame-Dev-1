# import libraries
import random

marks = []
for i in range(20):
    marks.append(random.randint(0, 100))

# lists
low = []
mid = []
high = []

# for loop
for i in marks:
    # if less than or = 30
    if i <= 30:
        low.append(i)
    # if 31 to 69
    elif i >=31 and i <=69:
        mid.append(i)
    # if 70+
    else:
        high.append(i)

# print lists
print(low)
print(mid)
print(high)