class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("moves along")


my_car = Vehicle('IVM', "Ikenga")
print(my_car.make)
print(my_car.model)
my_car.move()