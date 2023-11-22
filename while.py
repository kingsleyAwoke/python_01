value = 1
# while loop syntax
while value <= 10:
    print(value)
    value += 1


# break keyword terminates the loop once it reaches 5
while value < 10:
    print(value)

    if value == 5:
        break
    value += 1

# continue keyword skips to the next iteration once it reaches 5
while value < 10:
    value += 1

    if value == 5:
        continue
    print(value)