# syntax for creating a function
def greet():
    print("Hello")

greet()

# Passing parameters to the function
def sum(num1, num2):
    print(num1 + num2)

sum(2, 3)

# Using return keyword, and check if the value type in int, also setting the default value
def addition(num1=0, num2=0):
    if (type(num1) is  not int or type(num2) is not int):
        return
    return num1 + num2

total = addition(10, 20)
print(total)

# multiple parameters
def people(*args):
    print(*args)

people("Kingsley", "Ada", "Victor", "ThankGod")

# kwargs in function
def auto(**cars):
    print(cars)

auto(Toyota="Camery", Lamborgini="Urus")