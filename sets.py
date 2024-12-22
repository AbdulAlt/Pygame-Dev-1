# initialize set a and b
a = {1, 2, 3, 4, 5}
b = set([6, 7, 8, 9])
# print set a and b
print(a)
print(b)
# initialize set c (blank set)
c = set()
# print set c
print(c)
# add 10 to c
c.add(10)
# print c
print(c)
# remove 5 from set a
a.remove(5)
# print set a
print(a)
# remove 10 from set c
c.discard(10)
# print c
print(c)
# remove entire set c
c.clear()
# print b
print(b)
# remove 5 again from set a
#   a.remove(5)
#   print set a
#   print(a)
# remove 5 again with discard
c.discard(10)
# print c
print(c)
# union of a and b (both together)
ab = a|b
# print ab
print(ab)
# union of a and b with .union()
ab_two = a.union(b)
# print ab two
print(ab_two)
# setting up for intersections (common elements)
a.add(12)
b.add(12)
print( a, b)
# intersecting a and b
inter = a&b
print(inter)
# intersecting and b with .intersect()
alt_inter = a.intersection(b)
# print alt_inter
print(alt_inter)
# using difference (shows only elements of the first set)
dif = a-b
# print dif
print(dif)
# using differece with the function
alt_dif = a.difference(b)
# print alt_dif
print(alt_dif)
# symmetric difference (shows the elements but without the common elements)
sym = a^b
# print sym
print(sym)
# symmetric difference with the function
alt_sym = a.symmetric_difference(b)
# print alt_sim
print(alt_sym)
for i in b:
    print(i)

# adding another 12 to b
b.add(12)
b.add(12)
# print b
print(b)