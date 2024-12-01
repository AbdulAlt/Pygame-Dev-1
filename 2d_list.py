list_1d = [1, 2, 3, 4, 5]
list_2d = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
print(list_2d)
print(list_1d[2])
print(list_2d[1][1])
print(list_2d[2][2])
list_1d.append(6)
print(list_1d)
list_2d.append([10, 11, 12])
print(list_2d)
list_2d[1].append('here')
print(list_2d)
list_1d[4] = 44
print(list_1d)
list_2d[2][1] = 88
print(list_2d)
del list_2d[3]
print(list_2d)
del list_2d[1][3]
print(list_2d)
print(len(list_1d))
print(len(list_2d))
for row in list_2d:
    for item in row:
        print(item, end = ' ')
    print()