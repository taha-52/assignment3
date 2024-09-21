my_dict = {'a': 10, 'b': 20, 'c': 15, 'd': 30, 'e': 25}

values = list(my_dict.values())

sorted_values = sorted(values, reverse=True)

top_3_values = sorted_values[:3]

print("The highest 3 values are:", top_3_values)
