#!/usr/bin/python

class ApplesOverflow(Exception):

    def __init__(self, apples):
        self.apples = apples

    def __repr__(self):
        return "Te pasaste de manzanas. Por {}".format(self.apples)

class Basket(object):

    def __init__(self):
        self.apples = {
            'Gabriel': 5,
            'Obed': 16
        }

    def get_apples(self, name):
        apples = 0
        try:
            apples = self.apples[name]
        except KeyError as e:
            self.apples[name] = apples
        return apples

    def add_apples(self, name, amount):
        try:
            self.apples[name] += amount
            acc = 0
            for member in self.apples:
                acc += self.apples[member]
            if acc > 25:
                raise ApplesOverflow(acc-25)
        except KeyError as e:
            self.apples[name] = amount
        except ApplesOverflow as e:
            print("No pasa nada")

b = Basket()
n = b.get_apples('Jaime')
b.add_apples("Gabriel", 10)
print(b.apples)