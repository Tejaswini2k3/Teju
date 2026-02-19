def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

nums = [1, 2, 3, 4, 5, 3, 2, 6]
print("Duplicates:", find_duplicates(nums))
