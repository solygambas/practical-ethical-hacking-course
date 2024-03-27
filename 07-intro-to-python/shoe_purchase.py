from Shoes import Shoes

low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s', 120)
high = Shoes('Off Whites', 400)

try:
    shoe_budget = float(input('Enter your budget: '))
except ValueError:
    exit('Budget must be a number.')
for shoe in [high, medium, low]:
    shoe.buy(shoe_budget)