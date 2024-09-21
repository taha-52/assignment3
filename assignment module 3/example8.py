original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

unique_list = []

seen = set()

for item in original_list:

    if item not in seen:
        unique_list.append(item)
        seen.add(item)

print("Unique elements:", unique_list)
