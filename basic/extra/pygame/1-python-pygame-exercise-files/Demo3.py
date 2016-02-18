class Person:

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

p = Person("Filip")
print(p.getName())