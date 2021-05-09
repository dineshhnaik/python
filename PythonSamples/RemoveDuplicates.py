# Remove duplicates in list
numbers = [2,6, 4, 5, 6, 5, 8]
duplicate_numbers = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicate_numbers:
        duplicate_numbers.append(num)
print(f'Numbers before removing duplicates: {numbers}')

for num in duplicate_numbers:
    numbers.remove(num)

print(f"Numbers after removing duplicates: {numbers}")
