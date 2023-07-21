from collections import Counter
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
unique = Counter(duplicate)
print(list(unique.keys()))