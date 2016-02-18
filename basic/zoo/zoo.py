class Life(object):

	YEAR = 2010
	BEINGS = []

	@classmethod
	def time_passes(cls, years):
		for being in cls.BEINGS:
			being.grow_up(years)
		cls.YEAR += years

class Animal(object):

	def __init__(self, age):
		self.age = age
		Life.BEINGS.append(self)

	def recieve_name(self, name):
		self.name = name

	def grow_up(self, years):
		self.age += years
		print self.__class__.__name__+" now has "+str(self.age)+" years old"

	def is_pet(self):
		if 'Pet' in [c.__name__ for c in list(self.__class__.__bases__)]:
			return True
		return False

	def speak(self):
		print "I have been living for "+str(self.age)+" years"

class Mammal(Animal):

	def speak(self):
		print "I was born from my mom's belly"
		super(Mammal, self).speak()

class Fish(Animal):

	def speak(self):
		print "I have scales"
		super(Fish, self).speak()

class Bird(Animal):

	def speak(self):
		print "I have feathers"

class Pet(Animal):

	def be_adopted(self, name, master):
		super(Pet, self).recieve_name(name)
		self.master = master
		print name+" was adopted by "+self.master.name

	def speak(self):
		print self.master.name+" is my master"
		super(Pet, self).speak()

class Dog(Mammal, Pet):

	def speak(self):
		print "Woof!"
		super(Dog, self).speak()

class GoldenFish(Fish, Pet):

	def speak(self):
		print "My color is golden"
		super(GoldenFish, self).speak()

class Wild(Animal):

	def speak(self):
		print "I cannot be tamed"
		super(Wild, self).speak()

class Tiger(Mammal, Wild):

	def speak(self):
		print "I am a tiger"
		super(Tiger, self).speak()

class Person(Mammal):

	def __init__(self, name):
		super(Person, self).__init__(0)
		super(Person, self).recieve_name(name)
		self.pets = []
		print self.name+" was born."

	def adopt_pet(self, animal, name):
		if animal.is_pet():
			animal.be_adopted(name, self)
			self.pets.append(animal)
		else:
			print animal.__class__.__name__+" is wild and cannot be adopted"

	def play_with_pets(self):
		for pet in self.pets:
			print "Playing with "+pet.name
			pet.speak()

me = Person("Gabriel")
Life.time_passes(20)
me.adopt_pet(Dog(3), "Icy")
Life.time_passes(5)
me.adopt_pet(GoldenFish(2), "Juicy")
me.adopt_pet(Tiger(2), "Fury")
puppy = Dog(0)
me.play_with_pets()
Life.time_passes(2)



