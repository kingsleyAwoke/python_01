# Syntax for creating Tuple
my_tuple = ("Benz", "Lambo", "Felarri")
print(my_tuple)

# How to modify tuble
newlist = list(my_tuple)
newlist.append("Bugatti")
newtuple = tuple(newlist)
print(newtuple)

# Unpack tuple
nums = (1,2,4,5,65,4,22,2,2)
(one, two, *others) = nums
print(one)
print(two)
print(others)

# Check a specific item occurence in a tuple
print(nums.count(2))
