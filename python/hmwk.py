# import libraries
from random import randint

# create the file
f = open('c:\\Users\\44794\\Music\\Jetlearn\\Game Dev 1\\python\\B.txt', 'w')
# create the numbers list
numbers = []
# for loop to add items to the numbers list
for i in range(10):
    numbers.append(randint(1, 100))
# string and format because otherwise you get an error
f.write('{}\n'.format(numbers))
# sum variable
sumNumbers = sum(numbers)
# create the sum
f.write('the sum is {}'.format(sumNumbers))
f = open('c:\\Users\\44794\\Music\\Jetlearn\\Game Dev 1\\python\\B.txt', 'r')
print(f.readlines())