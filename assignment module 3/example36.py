def find_max_min(numbers):
    
    max_number = max(numbers)
    min_number = min(numbers)
    
    return max_number, min_number

decimal_numbers = [3.14, 2.71, 1.61, 4.67, 0.577] 

max_num, min_num = find_max_min(decimal_numbers)

print(f"The maximum number is {max_num}.")
print(f"The minimum number is {min_num}.")
