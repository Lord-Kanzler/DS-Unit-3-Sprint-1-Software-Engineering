# !/usr/bin/env python

from random import randint, sample, uniform
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for _ in list(range(num_products)):
        name = (sample(ADJECTIVES, k=1) + " " + sample(NOUNS, k=1))

    products.append(name)
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())


# #The last lines let you test by running `python acme_report.py`.
# You should see output like:

# ```
# $ python acme_report.py
# ACME CORPORATION OFFICIAL INVENTORY REPORT
# Unique product names: 19
# Average price: 56.8
# Average weight: 54.166666666666664
# Average flammability: 1.258097155966675
# ```
