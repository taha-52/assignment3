strings = ["apple", "banana", "civic", "deed", "madam", "radar", "level", "noon", "refer", "world"]
count = 0
for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(f"Number of strings with length 2 or more and same first and last character: {count}")
