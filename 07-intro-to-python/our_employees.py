from Employees import Employees

e1 = Employees("John", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Jane", "Executive", "CIO", 150000, 10)

print(e1.name) # John
print(e2.role) # CIO

print(e1.eligible_for_retirement()) # True