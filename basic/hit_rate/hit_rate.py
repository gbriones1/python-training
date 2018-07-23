from random import random

tries = 0
chance = .5
hit = False

while not hit:
    tries += 1
    n = random()
    print("Got {}".format(n*100))
    if n*100 <= chance:
        hit = True

print("Chance of {}% hit in {} tries".format(chance, tries))
