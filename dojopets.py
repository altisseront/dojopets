class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def eat(self):
        print(self.name, "eats")
    
    def bathe(self):
        print(self.name, "bathes")

    def play(self):
        print(self.name, "plays")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.bathe()
        return self



Rat = Pet("remy", "rat", "dance")
gilbert = Ninja("gilbert", "tisseront", "carrots", "chicken", Rat)
gilbert.feed()
gilbert.walk()
gilbert.bathe()