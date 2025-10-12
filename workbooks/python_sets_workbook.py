
# 📘 Python Sets Workbook with Solutions

# 1. Creating Sets
print("Exercise 1: Creating Sets")
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# 2. Iterating Through a Set
print("\nExercise 2: Iteration")
for item in my_set:
    print(item)

# 3. Add and Update Elements
print("\nExercise 3: Add and Update")
my_set.add(5)
print("After add:", my_set)
my_set.update([6, 7])
print("After update:", my_set)

# 4. Remove and Discard
print("\nExercise 4: Remove and Discard")
my_set.remove(1)
print("After remove:", my_set)
my_set.discard(100)  # No error if not found
print("After discard:", my_set)

# 5. Set Union
print("\nExercise 5: Union")
a = {1, 2, 3}
b = {3, 4, 5}
union_set = a.union(b)
print("Union:", union_set)

# 6. Set Intersection
print("\nExercise 6: Intersection")
print("Intersection:", a.intersection(b))

# 7. Set Difference
print("\nExercise 7: Difference")
print("a - b:", a.difference(b))
print("b - a:", b.difference(a))

# 8. Set Symmetric Difference
print("\nExercise 8: Symmetric Difference")
print("Symmetric Difference:", a.symmetric_difference(b))

# 9. Frozen Set
print("\nExercise 9: Frozen Set")
frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)

# 10. Set Membership
print("\nExercise 10: Membership")
print("2 in a?", 2 in a)
print("10 in a?", 10 in a)
