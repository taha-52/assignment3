my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 4}

sorted_ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by values (ascending):", sorted_ascending)
print("Dictionary sorted by values (descending):", sorted_descending)
