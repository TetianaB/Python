#Sets

set1 = {1,2,3,4}
set2= {1,2,3,4,'war', 'NY'}

print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.difference(set1))
print(set1.intersection(set2))
print(id(set1))
print(set1.remove(4))
print(set1.add(8))
print(set1)
print(set2.symmetric_difference(set1))

fs=frozenset({1,2,3,4})
print(fs)
