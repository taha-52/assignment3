list_of_tuples = [(1, 2, 3), (), (4, 5), (), (6, 7, 8), (), (9,)]

filtered_list_of_tuples = []

for t in list_of_tuples:
    
    if t:
        filtered_list_of_tuples.append(t)

print("Original list of tuples:", list_of_tuples)
print("Filtered list of tuples (without empty tuples):", filtered_list_of_tuples)
