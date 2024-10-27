l1 = [1, 2, 3, 4, 5]
d1 = {'first': 1, 'second': 2}
print(d1)
d1['third'] = 3
print(d1)
del d1['first']
print(d1)
print(d1)
d1['second'] = 2
print(d1)
d1['third'] = 3
d1['fourth'] = 4
d1['fifth'] = 5
print(d1.keys())
print(d1.values())
for i in d1.keys():
    print(i, d1[i])
print('third' in d1)
if 'third' in d1:
    print('key does exist')
else:
    print('key does not exist')

# Nested Dictionarys
classroom = {'student 1': {'age': 4, 'marks': 100}, 'student 2': {'age': 5, 'marks': 50}}
print(classroom)
print(classroom.keys())
print(classroom.values())
for i in classroom.keys():
    print(i, classroom[i])

print(classroom['student 1']['age'])
