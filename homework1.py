cost = {'physics': 2, 'maths': 500, 'english': 200, 'science': 300, 'art': 500}
print(cost)
cost['physics'] = 200
print(cost)
a = input('write a book name\n').lower()
if a in cost:
    print(f'The cost of {a} is {cost[a]}')
else:
    print('The book is not available')
print(cost)