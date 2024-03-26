# no need to be a dev to be successful, being able to read code

# STRINGS

# linux
##!/bin/python3

# # Print Hello, World! to the console
# print("Hello, World!")

# # Triple quote for multi-line strings
# print("""Hello, 
# World!""")

# # Concatenation
# print("Hello, " + "World!")

# # Print a new line
# print("Hello, \nWorld!")

# MATH

# # Addition
# print(5 + 5)
# # Subtraction
# print(5 - 5)
# # Multiplication
# print(5 * 5)
# # Division
# print(5 / 5) # 1.0 float
# # Exponent
# print(5 ** 5)
# # Modulus
# print(50 % 6) # 2 (remainder)
# # Floor division
# print(50 // 6) # 8 (quotient)

# VARIABLES & METHODS

# # Variables
# quote = "All is fair in love and war."
# print(quote)
# # Methods
# print(quote.upper()) # ALL IS FAIR IN LOVE AND WAR.
# print(quote.lower()) # all is fair in love and war.
# print(quote.title()) # All Is Fair In Love And War.
# print(len(quote)) # 28
# name = "Heath"
# age = 30
# gpas = 3.7 # float
# print(int(age)) # 30
# print(int(gpas)) # 3

# print("My name is " + name + " and I am " + str(age) + " years old.")

# age += 1
# print(age) # 31

# birthday = 1
# age += birthday
# print(age) # 32

# FUNCTIONS

# def who_am_i(name, age):
#     return "My name is " + name + " and I am " + str(age) + " years old."

# print(who_am_i("Heath", 30))

# def square_root(num):
#     return num ** 0.5

# print(square_root(64)) # 8.0

# BOOLEAN

# bool1 = True
# bool2 = 3 * 3 == 9
# bool3 = False
# bool4 = 3 * 3 != 9

# print(bool1, bool2, bool3, bool4) # True True False False
# print(type(bool1)) # <class 'bool'>

# RELATIONAL OPERATORS

# greater = 3 > 2
# less = 3 < 2
# greater_equal = 3 >= 2
# less_equal = 3 <= 2

# test_and = (3 > 2) and (4 > 3)
# test_or = (3 > 2) or (3 < 2)
# test_not = not True

# CONDITIONALS

# def drink(money):
#     if money >= 2:
#         return "You've got yourself a drink!"
#     else:
#         return "No drink for you!"

# print(drink(3)) # You've got yourself a drink!
# print(drink(1)) # No drink for you!

# def alcohol(age, money):
#     if (age >= 21) and (money >= 5):
#         return "We're getting a drink!"
#     elif (age >= 21) and (money < 5):
#         return "Come back with more money."
#     elif (age < 21) and (money >= 5):
#         return "Nice try, kid!"
#     else:
#         return "You're too poor and too young."

# print(alcohol(21, 5)) # We're getting a drink!
# print(alcohol(21, 4)) # Come back with more money.
# print(alcohol(20, 5)) # Nice try, kid!
# print(alcohol(20, 4)) # You're too poor and too young!

# LISTS

# movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life", "The Holy Grail"]
# print(movies[0]) # The Holy Grail
# print(movies[1]) # The Life of Brian
# print(movies[1:3]) # ['The Life of Brian', 'The Meaning of Life']
# print(movies[1:]) # ['The Life of Brian', 'The Meaning of Life', 'The Holy Grail']
# print(movies[:2]) # ['The Holy Grail', 'The Life of Brian']
# print(movies[-1]) # The Holy Grail
# print(len(movies)) # 4

# movies.append("JAWS")
# print(movies) # ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life', 'The Holy Grail', 'JAWS']
# movies.insert(2, "The Dark Knight")
# print(movies) # ['The Holy Grail', 'The Life of Brian', 'The Dark Knight', 'The Meaning of Life', 'The Holy Grail', 'JAWS']
# movies.pop()
# print(movies) # ['The Holy Grail', 'The Life of Brian', 'The Dark Knight', 'The Meaning of Life', 'The Holy Grail']
# movies.pop(2)
# print(movies) # ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life', 'The Holy Grail']

# amber_movies = ["Just Go With It", "The Wedding Singer", "50 First Dates"]
# our_movies = movies + amber_movies
# print(our_movies) # ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life', 'The Holy Grail', 'Just Go With It', 'The Wedding Singer', '50 First Dates']

# grades = [["Bob", 3.7], ["Heath", 3.8], ["Amber", 3.9]]
# bobs_grade = grades[0][1]
# print(bobs_grade) # 3.7


