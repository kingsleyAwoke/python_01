try:
    print(x)

except:
    print("There is an error")


try:
    print(x)

except NameError:
    print("There is a name error")

x = 2
try:
    print(x / 0)

except ZeroDivisionError:
    print("You cannot divide with zero")

try:
    print("x")

except ZeroDivisionError:
    print("You cannot divide with zero")

else:
    print("There is no error here")

finally:
    print("Always print with or without error")