
x = 0
y = 0
result = 0
while True:
    print('''List of available options:
    1. Add
    2. Multiply
    3. Divide
    4. Subtract
    5. Exit
    
    Please enter your choice (numeric value): ''')
    choice = int(input())
    if choice == 5:
        break
    elif choice == 1:
        # Add
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        result = x + y
        print(f'Sum of {x} and {y} is {result}')
    elif choice == 2:
        # Multiply
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        result = x * y
        print(f'Product of {x} and {y} is {result}')
    elif choice == 3:
        # Divide
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        result = x // y
        print(f'Division of {x} and {y} is {result}')
    elif choice == 4:
        # Subtract
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        result = x - y
        print(f'Difference of {x} and {y} is {result}')