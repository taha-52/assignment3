my_tuple = (1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 1, 2)

seen = set()

repeated = set()

for item in my_tuple:
    if item in seen:
        repeated.add(item)
    else:
        seen.add(item)

repeated_items_list = list(repeated)
print("Repeated items in the tuple:", repeated_items_list)
