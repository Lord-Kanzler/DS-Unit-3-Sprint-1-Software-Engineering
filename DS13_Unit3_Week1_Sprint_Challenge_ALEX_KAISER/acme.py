'''
Product class to record stats for individual players
'''
import random

# Part 1 - Keeping it Classy


class Product():
    def __init__(self, name=None, price=10, weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # Part 2 - Objects that Go!

    def stealability(self):
        '''
        - calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return
        "Not so stealable...", if it is greater or equal to 0.5 but less than
        1.0 return "Kinda stealable.", and otherwise return "Very stealable!"
        '''
        steal = self.price / self.weight
        if steal < 0.5:
            print("Not so stealable...")

        if (steal >= 0.5) and (steal < 1.0):
            print("Kinda stealable.")

        else:
            print("Very stealable!")

    def explode(self):
        '''
        - calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.",
        if it is greater or equal to 10 but less than 50 return "...boom!",
        and otherwise return "...BABOOM!!"
        '''
        boom_factor = self.flammability * self.weight
        if boom_factor < 10:
            print("...fizzle.")

        if (boom_factor >= 10) and (boom_factor < 50):
            print("...boom!")

        else:
            print("...BABOOM!!")
    

# Part 3 - A Proper Inheritance


class BoxingGlove(Product):
    def __init__(self, name=None, price=10, weight=10,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(
            name=name,
            price=price,
            weight=weight,
            flammability=flammability,
            identifier=identifier)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        weight = self.weight

        if (weight < 5):
            print("That tickles.")

        if (weight >= 5) and (self.weight < 15):
            print("Hey that hurt!")

        else:
            print("OUCH!")
