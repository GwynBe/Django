class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles'


blue = Car('blue', 20000)
red = Car('red', 30000)
print(blue)
print(red)
        
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return f'{self.name} says {sound}'


dog = GoldenRetriever('Mic', 4)
print(dog.speak)


