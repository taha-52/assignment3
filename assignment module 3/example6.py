list1 = [1, 2, 3, 4]
list2 = [3, 5, 6]
list3 = [7, 8, 9]
for item in list1:
        if item in list2:
            print("common ")
        else:
              print("uncommon")
print(list1, list2)  
print(list1, list3)  
