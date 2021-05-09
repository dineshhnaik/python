#################################
# P8 Math functions
import math

# Modules
from pathlib import Path
path = Path()
for p in path.glob('*.py'):
    print(p)

# from Dice import Dice
#
# dice1 = Dice()
# numbers = dice1.roll_on()
# print(numbers)

# import random
# colors = ["red", "blue", "yellow", "green", "orange"]
# print(random.choice(colors))

# for i in range(3):
#     print(random.randint(1, 25))


# from ecommerce import shipping
# from ecommerce.shipping import calc_shipping
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# shipping.calc_shipping()
# calc_shipping()

# import Utils
# from Utils import find_largest
#
# numbers = [10, 5, 3, 81, 20, 18]
# print(f'Max. number is {find_largest(numbers)}')

# import Converters
# from Converters import kgs_to_lbs
# print(kgs_to_lbs(100))

# print(Converters.kgs_to_lbs(100))
# print(Converters.lbs_to_kgs(68))


# Class

# Inheritence

# class Mammal:
#     def walk(self):
#         print('walk')
#         # print(self.__class__)
#
# class Dog(Mammal):
#     def bark(self):
#         print('Dog barks')
#
# class Cat(Mammal):
#     def annoying(self):
#         print('Cat is annoying')


# dog = Dog()
# cat = Cat()
# dog.bark()
# dog.walk()
# cat.walk()
# cat.annoying()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'{self.name} talks!')
#
#
# person = Person('Dinesh')
# person.talk()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('Move')
#
#     def draw(self):
#         print('Draw')
#
#
# point1 = Point(12, 14)
# point1.draw()
# point1.move()
#
# print(point1.x)
# print(point1.y)

# Functions

# try:
#     age = int(input('Enter age: '))
#     income = 2000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be zero!')
# except ValueError:
#     print('Invalid value!')

# def get_emoji(message):
#     emojis = {
#         ":)" : "😀",
#         ":(" : "🙁"
#     }
#     words = message.split(' ')
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + ' '
#
#     return output
#
#
# message = input('Enter the string: ')
#
# print(get_emoji(message))

# By default functions return None.
# def square(num1):
#     return num1 ** 2
#
#
# num = int(input('Enter the number: '))
# print(f'Value is: {square(num)}')

# def greet_user(first_name, last_name):
#     print(f'Hello {first_name} {last_name}')
#     print('How are you?')
#
#
# print('Start')
# greet_user( 'John', last_name='Smith')
# print('end')

# message = input("Enter the string: ")
# words = message.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "☹"
# }
#
# output = ""
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)

# numbers = {
#     "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
#     "9": "Nine", "0": "Zero"
# }
#
# input_number = input('Enter the number: ')
# output = ""
# for num in input_number:
#     output += numbers.get(num, "") + " "
#
# print(output)

# Dictionary
# customer = {
#     "name": "Dinesh",
#     "age": 37,
#     "city": "Bangalore",
#     "is_valid": True
# }
#
# print(customer.get("Name", "Dinesh"))

# Tuple - cannot be modified
# numbers = (1,2,3)

# Unpacking
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(f'{x},{y},{z}')

# numbers = [12, 4, 15, 7, 9]
# # numbers.insert(3, 16)
# # numbers.pop()
# # numbers.sort()
# # numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(23)
# print(numbers2)
# print(numbers)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for m in matrix:
#     for n in m:
#         print(n)

# numbers = [10, 2, 8, 11, 12, 9]
# count = int(len(numbers))
# largest = 0
# for x in numbers:
#     if x > largest:
#         largest = x
# print(f'Largest: {largest}')

# Largest number
# for x in numbers[0:(count//2)+1]:
#     if x > largest:
#         largest = x
#     for y in numbers[(count//2)+1:]:
#         if y > largest:
#             largest = y
# print(f'Largest number is: {largest}')

# name = "Grammar book for High school"
# print(name[1:-5])

# names = ["John", "Bob","Mosh","Mary","Sarah"]
# print(names[-4])

# numbers_for_l = [2,2,2,2,5]
#
# for x in numbers_for_l:
#     output = ""
#     for y in range(x):
#         output += "x"
#     print(output)

# numbers = [5,2,5,2,2]
#
# for x in numbers:
#     output = ""
#     for y in range(x):
#         output += "x"
#     print(output)
#
# for x in numbers:
#     print('x' * (x))

# xx
# xx
# xx
# xx
# xxxxx

# xxxxx
# xx
# xxxxx
# xx
# xx

# for x in range(5):
#     for y in range(4):
#         print(f'({x}, {y})')

# prices = [10, 20, 30]
# sum_of_prices = 0
# for price in prices:
#     sum_of_prices += price
# print(f'Sum from loop: {sum_of_prices}')
#
# print(f'Total = {sum(prices)}')

# for item in range(1, 10, 1):
#     print("*" * item)

# for item in 'Python':
#     print(item)

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1

# weight = int(input("Enter the weight: "))
# weight_unit = input("(K)gs or (L)bs?: ")
# is_weight_in_pounds = False
#
# if weight_unit.lower() == "l":
#     is_weight_in_pounds = True
#
# if is_weight_in_pounds:
#     print(f'Your weight in Kgs is: {weight * 0.45} Kgs')
# else:
#     print(f'Your wieght in pounds is: {weight / 0.45} lbs')

# name = input("Please enter your name: ")
#
# if len(name) < 3:
#     print("Name should be at least 3 characters.")
# elif len(name) > 50:
#     print("Name cannot be more than 50 characters")
# else:
#     print("Name looks good!")

# temperature = int(input("What is the temperature today? "))
#
# if temperature > 30:
#     print("It's a hot day today")
# elif temperature < 10:
#     print("It's a cold day today")
# else:
#     print("It's neither hot or cold today")

# current_day = input("What is the day today? ")
#
# if not (current_day.lower().__eq__("saturday") or current_day.lower().__eq__("sunday")):
#     print("Today is a weekday!")
# else:
#     print("Today is a weekend!")

# has_high_income = True
# has_good_credit = False
#
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan.")

# house_price = 1000000
# credit_value = input("Does the buyer has good credit? ")
# has_good_credit = False
# if credit_value.__eq__("Yes"):
#     has_good_credit = True
# else:
#     has_good_credit = False
#
# down_payment = 0
# if has_good_credit:
#     down_payment = house_price * 0.1
# else:
#     down_payment = house_price * 0.2
#
# print(f'Your downpayment amount is ${down_payment}')

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day.")
#     print("Drink plenty of fluids.")
# elif is_cold:
#     print("It's a cold day.")
#     print("Wear warm clothes.")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
#################################
# P7 Arithmetic operators
# print(10 + 5)  # Add
# print(8 - 5)  # Subtract
# print(6 * 3)  # Multiply
# print(10 / 3)  # Divide, Quotient with decimal values.
# print(10 % 3)  # Remainder
# print(8 // 3)  # Quotient
# print(7 ** 5)  # Exponentiation
# x = (3 + 6) - 9 * 2
# print(x)
#################################
# P6 String formatting
# course = 'Python for beginners'
# # check string is present in a variable
# print('Python' in course)
# print(course.upper())
# print(course.lower())
# print(course.find('beginners'))
# print(course.replace('beginners', 'expert'))
# name = 'John'
# lastname = 'Smith'
# message = name + ' [' +lastname+ '] is a coder'
# print(message)
# formattedString = f'{name} [{lastname}] is a coder'
# print(formattedString)
# age = 10
# formattedString2 = f'I am {name}. My age is {age}'
# print(formattedString2)

#################################
# P5 strings

# name = 'Jennifer'
# print(name[1:-1])
#
# course = 'Python course for beginners'
# another_course = course[:]
# course = 'New course'
# print('Course is: '+course)
# print('Another course is: '+another_course)
# print('Character at first index: ' + course[1])
# print('Character at last index (reads from reverse) :' + course[-3])
# print('Characters from beginning till index: ' + course[0:3])
# print('Return entire string: '+course[:])

# long string data
# email = '''
# Hi John,
#
# This is our first email!
#
# Thank you,
# The support team
# '''
# print(email)
# course = 'Python course for "beginners"'
# print(course)

#################################
# P4 Type conversion
# weight_in_pounds = input('Enter weight in pounds: ')
# print('You entered '+str(weight_in_pounds) + ' lbs')
# weight_in_kilograms = int(weight_in_pounds) * 0.45
# print('The entered weight is equivalent to ' + str(weight_in_kilograms) + ' Kgs')

# birth_year = input('What is your year of birth? ')
# print(type(birth_year))
# age = 2020-int(birth_year)
# print(type(age))
# print('You are '+str(age) + ' old!')
#################################
# P3 Read I/O

# name = input('What is your name? ')
# colour = input('What is your favourite color? ')
# age = input('What is your age? ')
# print(name + ' is ' + str(age) + ' years old.')
# print(name +' likes '+ colour)
#################################
# P2 variables
# price = 10
# rating = 4.3
# name = 'Dinesh'
# is_Published = True
# print(price)
# print(name)

# patientName = "John Smith"
# Age = 20
# isNewPatient = True
# print("Patient name is: " + patientName)
# print(Age)

# print("Rating" &rating)

#################################
# P1 Hello world!
# print("Hello world")
# print("Dinesh H Naik")

# print('0----')
# print(" ||||")
# print("*" * 10)
#
# print('  *  ')
# print(' *'*2)
# print('* '*3)
# print('*'*4)
# print('*'*5)
# print('*'*4)
# print('*'*3)
# print('*'*2)
# print('*')
#################################
