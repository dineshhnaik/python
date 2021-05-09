# Prints the 'n' Fibonacci numbers

total_num = int(input("Please enter a number:"))
print(f'Entered number is {total_num}')

prev_num1 = 1
prev_num0 = 0
current_num = 0
fibonacci_numbers = []
if total_num == 1:
    fibonacci_numbers.append(prev_num0)
elif total_num == 2:
    fibonacci_numbers.append(prev_num0)
    fibonacci_numbers.append(prev_num1)
else:
    fibonacci_numbers.append(prev_num0)
    fibonacci_numbers.append(prev_num1)

    for num in range(2, total_num, 1):
        current_num = prev_num0 + prev_num1
        fibonacci_numbers.append(current_num)
        prev_num0 = prev_num1
        prev_num1 = current_num
        # 0, 1, 1, 2, 3, 5, 8

print(f'The {total_num} Fibonacci numbers are: {fibonacci_numbers}')