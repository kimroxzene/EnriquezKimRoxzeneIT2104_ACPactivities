set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

first_set_difference = set1.difference(set2)
second_set_difference = set2.difference(set1)
print("Set difference: ", first_set_difference,",", second_set_difference)

set_union = set1.union(set2)
print("Union of sets: ", set_union)

first_symmetric_diff= set2.symmetric_difference(set1)
second_symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference: ", first_symmetric_diff, ",", second_symmetric_diff)

set_intersection = set1.intersection(set2)
print("Set Intersection: ", set_intersection)