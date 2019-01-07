# 1. Using OOP in Python, we can restrict access to methods and variables.
# 2. This prevent data from direct modification which is called encapsulation.
# 3. In Python, we denote private attribute using underscore as prefix i.e single "_" or double "__".

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1500)
c.sell()
