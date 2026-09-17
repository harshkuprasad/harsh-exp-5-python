list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = lambda x, y: list(filter(lambda n: n in y, x))

print("Intersection:", intersection(list1, list2))
