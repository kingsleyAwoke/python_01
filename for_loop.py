# Basic for loop
names = ["Kingsley", "Ada", "Victor", "ThankGod"]
for name in names:
    print(name)

# Print each letter
for letter in "Mississippi":
    print(letter)

# Break keyword stops the loop once it meets the name "Victor"
for name in names:
    if name == "Victor":
        break
    print(name)

# continue keyword stops the loop once it meets the name "Victor"
for name in names:
    if name == "Victor":
        break
    print(name)

# Using range in for loop
for x in range(10):
    print(x)

# specifying where to start counting
for x in range(3, 10):
    print(x)

# increament by 5
for x in range(5, 101, 5):
    print(x)
else:
    print("Glad tha\'s over!")

# Nested loops
names = ["Kingsley", "Ada", "Victor", "ThankGod"]
actions = ["code", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + ' ' + action + ".")