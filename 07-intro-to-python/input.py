# name = input("Enter your name: ")
# drink = input("Enter your favorite drink: ")
# print(f"Hello, {name}! Have a {drink} on me!")

x = float(input("Enter a number: "))
o = input("Enter an operator: ")
y = float(input("Enter another number: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "**" or o == "^":
    print(x ** y)
else:
    print("Invalid operator.")

