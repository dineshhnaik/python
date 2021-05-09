def find_largest(numbers):
    maximum = 0
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
