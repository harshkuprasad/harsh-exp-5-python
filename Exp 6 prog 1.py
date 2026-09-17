from collections import Counter

test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2, 1]
print("The original list: " + str(test_list))
temp = Counter(test_list)
res = [[key] * val for key, val in temp.items()]
print("Matrix after grouping: " + str(res))
