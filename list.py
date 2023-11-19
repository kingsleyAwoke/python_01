# List syntax
users = ['kingsley', 'obi', 'ada']
print(users)

# Verify if an item exist
print("kingsley" in users)

# Get a specific item in a specific index position
print(users[0])
print(users[-1]) # print the last item in the list
print(users.index('ada')) # check the index position of the a specific value

# Slicing
print(users[0:2])
print(users[0:])

# Length of the list
print(len(users))

# Add an item to the list
users.append('Ndubueze')
print(users)

# Merge two lists
fruits = ['Apple', 'Orange','Pawpaw','Mango']
fruits.extend(users)
print(fruits)

# Add an item to a specific index position
users.insert(1, "ThankGod")
print(users)

# Using the bracket notion
users[2:2] = ["victor", "mmeso"]
print(users)

# Sort items
users.sort()
print(users)

users.sort(key=str.lower) # To start from the lowercase order
print(users)

nums = [2,3,2,4,5,65,24,13,]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

# Copy list
numscopy = nums.copy()
print(numscopy)
# -----OR-----
mynum = list(nums)
print(mynum)

# Remove an item
users.remove("kingsley")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# clear data
users.clear()
print(users)

# Using the list constructor to create a list
mylist = list(["0bi", 3,5,54,5])
print(mylist)
