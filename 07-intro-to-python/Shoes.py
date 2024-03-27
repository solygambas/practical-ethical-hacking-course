class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def budget_check(self, budget):
        if not isinstance(budget, (int, float)):
            print("Budget must be a number.")
            exit()
    
    def change(self, budget):
        return budget - self.price

    def buy(self, budget):
        self.budget_check(budget)
        if budget >= self.price:
            print(f'You can buy the {self.name} shoes.')
            if budget == self.price:
                print('You have exactly enough money for these shoes.')
            else:
                print(f'You will have ${self.change(budget)} left after buying the shoes.')
            exit("Thank you for shopping with us.")
