class Animal(object):

    def __init__(self, species, gender):
        self.species = species
        self.gender = gender
        self.foods = []
        self.sleep_hours = []

    def eat(self, food):
        print("Animal eats")
        self.foods.append(food)

    def sleep(self, num_hours):
        print("Animal sleeps")
        self.sleep_hours.append(num_hours)

# my_animal = Animal("pig", "male")
# my_animal.sleep(12)
# my_animal.eat("grass")

class Pig(Animal):
    def eat(self, food, amount):
        super(Pig, self).eat(food)
        for i in range(amount):
            self.foods.append(food)
        print("Pig eats")

pig = Pig("pig", "female")
pig.sleep(14)
pig.eat("acorn", 5)





